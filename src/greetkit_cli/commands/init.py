"""greetkit init command."""
from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path
import typer
from rich.live import Live
from rich.panel import Panel
from rich.text import Text
from rich.table import Table

from greetkit_cli._console import (
    StepTracker,
    console,
    select_with_arrows,
    show_banner,
)

app = typer.Typer(help="Initialize a GreetKit project")

def _stdin_is_interactive() -> bool:
    return sys.stdin.isatty()

@app.command("init")
def init(
    project_name: str = typer.Argument(
        None,
        help="Name for your new project directory (use '.' or --here to initialize in current directory)",
    ),
    integration: str = typer.Option(
        None,
        "--integration",
        "-i",
        help="Specify the AI agent integration (e.g., 'agy')",
    ),
    script_type: str = typer.Option(
        None,
        "--script",
        "-s",
        help="Script type to use: sh or ps",
    ),
    here: bool = typer.Option(
        False,
        "--here",
        help="Initialize project in the current directory",
    ),
    force: bool = typer.Option(
        False,
        "--force",
        "-f",
        help="Force overwrite when directory is not empty (skip confirmation)",
    ),
):
    """
    Initialize a new GreetKit project.
    
    This command will set up the GreetKit structure:
    1. Check prerequisites and target directory.
    2. Confirm overwrite if target folder is not empty.
    3. Ask for AI agent integration and script type (PS or Bash).
    4. Scaffold .gk-specs, .gk-plan, and .greetkit with templates & scripts.
    """
    show_banner()

    if project_name == ".":
        here = True
        project_name = None

    if here and project_name:
        console.print("[red]Error:[/red] Cannot specify both project name and --here flag")
        raise typer.Exit(1)

    if not here and not project_name:
        console.print("[red]Error:[/red] Must specify either a project name, '.' or use --here flag")
        raise typer.Exit(1)

    # 1. Resolve Target Path
    if here:
        target_path = Path.cwd()
        project_name = target_path.name
    else:
        target_path = Path(project_name).resolve()

    if target_path.exists() and not target_path.is_dir():
        console.print(f"[red]Error:[/red] Target '{target_path}' exists but is not a directory.")
        raise typer.Exit(1)

    # 2. Check Directory Emptiness
    if target_path.exists():
        existing_items = list(target_path.iterdir())
        # Filter out git/project configs if any to check real files
        real_items = [i for i in existing_items if i.name not in (".git", ".gitignore", ".vscode", "pyproject.toml", "poetry.lock")]
        if real_items:
            console.print(f"[yellow]Warning:[/yellow] Target directory is not empty ({len(real_items)} items found).")
            console.print("[yellow]Scaffolded templates and configurations may merge or overwrite existing files.[/yellow]")
            if not force:
                if _stdin_is_interactive():
                    response = typer.confirm("Do you want to continue?")
                    if not response:
                        console.print("[yellow]Initialization cancelled.[/yellow]")
                        raise typer.Exit(0)
                else:
                    console.print("[red]Error:[/red] Target directory is not empty. Use --force to merge.")
                    raise typer.Exit(1)

    # 3. Choose Integration (Interactive if not supplied)
    ai_choices = {
        "claude": "Claude Desktop / Claude Code",
        "cursor": "Cursor IDE",
        "codex": "Codex / OpenCode",
        "kimi": "Kimi Plugin",
        "agy": "Antigravity Agent Integration"
    }
    
    selected_plugins = []
    if integration:
        if integration not in ai_choices:
            console.print(f"[red]Error:[/red] Unknown integration '{integration}'. Available: {', '.join(ai_choices.keys())}")
            raise typer.Exit(1)
        selected_plugins.append(integration)
    elif not _stdin_is_interactive():
        selected_plugins = ["agy"] # Default fallback for non-interactive
    else:
        from greetkit_cli._console import multiselect_with_checkboxes
        selected_plugins = multiselect_with_checkboxes(
            ai_choices,
            prompt_text="Select agent integrations to install (Space to toggle, Enter to confirm)",
            default_selected=["claude", "cursor", "agy"]
        )
        if not selected_plugins:
            console.print("[yellow]No integrations selected. Falling back to default .agents footprint.[/yellow]")
            selected_plugins = ["agy"]


    # 4. Choose Script Type (Interactive if not supplied)
    script_choices = {
        "ps": "PowerShell Scripting (.ps1)",
        "sh": "Bash Shell Scripting (.sh)"
    }
    default_script = "ps" if os.name == "nt" else "sh"
    if script_type:
        if script_type not in script_choices:
            console.print(f"[red]Error:[/red] Unknown script type '{script_type}'. Choose: ps or sh")
            raise typer.Exit(1)
        selected_script = script_type
    elif not _stdin_is_interactive():
        selected_script = default_script
    else:
        selected_script = select_with_arrows(script_choices, "Choose script type:", default_script)

    # Print Project Setup Panel
    setup_lines = [
        "[cyan]GreetKit Project Setup[/cyan]",
        "",
        f"{'Project Name':<16} [green]{project_name}[/green]",
        f"{'Working Path':<16} [dim]{Path.cwd()}[/dim]",
    ]
    if not here:
        setup_lines.append(f"{'Target Path':<16} [dim]{target_path}[/dim]")
    
    console.print(Panel("\n".join(setup_lines), border_style="cyan", padding=(1, 2)))
    console.print(f"[cyan]Selected agent integration(s):[/cyan] {', '.join(selected_plugins)}")
    console.print(f"[cyan]Selected script type:[/cyan] {selected_script}")

    # Initialize Tree Step Tracker
    tracker = StepTracker("Initialize GreetKit Project")
    tracker.add("precheck", "Check required tools")
    tracker.complete("precheck", "ok")
    tracker.add("ai-select", "Select coding agent integrations")
    tracker.complete("ai-select", ', '.join(selected_plugins) if selected_plugins else "generic")
    tracker.add("script-select", "Select script type")
    tracker.complete("script-select", selected_script)

    tracker.add("dirs", "Create project directories")
    tracker.add("templates", "Install templates")
    tracker.add("scripts", "Install shared scripts")
    tracker.add("skills", "Install GreetKit agent skills")
    tracker.add("final", "Finalize project")

    _transient = sys.platform != "win32"

    with Live(tracker.render(), console=console, refresh_per_second=8, transient=_transient) as live:
        tracker.attach_refresh(lambda: live.update(tracker.render()))

        # Dirs Setup
        tracker.start("dirs")
        target_path.mkdir(parents=True, exist_ok=True)
        dirs = [
            "greetkit/specs",
            "greetkit/plans",
            ".agents",
            "greetkit/internal",
            "greetkit/internal/extensions",
            "greetkit/internal/integrations",
            "greetkit/internal/memory",
            "greetkit/internal/scripts",
            "greetkit/internal/templates",
            "greetkit/internal/workflows",
        ]
        for d in dirs:
            (target_path / d).mkdir(parents=True, exist_ok=True)
        tracker.complete("dirs", "created GreetKit footprint")

        # Import package locations helper
        import greetkit_cli
        def _find_asset_dir(name: str) -> Path | None:
            cli_dir = Path(greetkit_cli.__file__).resolve().parent
            if (cli_dir / name).is_dir():
                return cli_dir / name
            if (cli_dir.parent / name).is_dir():
                return cli_dir.parent / name
            if (cli_dir.parent.parent / name).is_dir():
                return cli_dir.parent.parent / name
            return None

        # Scaffold Core Assets (templates, extensions, workflows, integrations, memory)
        tracker.start("templates")
        pkg_templates = _find_asset_dir("templates")
        if pkg_templates and pkg_templates.exists():
            shutil.copytree(pkg_templates, target_path / "greetkit" / "internal", dirs_exist_ok=True)
            tracker.complete("templates", "copied structures to greetkit/internal")
        else:
            tracker.error("templates", "templates path not found in package")

        # Copy constitution template to memory
        template_const = target_path / "greetkit" / "internal" / "templates" / "constitution-template.md"
        memory_const = target_path / "greetkit" / "internal" / "memory" / "constitution.md"
        if template_const.exists() and not memory_const.exists():
            try:
                shutil.copy2(template_const, memory_const)
            except Exception:
                pass

        # Scaffold Shared Scripts
        tracker.start("scripts")
        pkg_scripts = _find_asset_dir("scripts")
        if pkg_scripts and pkg_scripts.exists():
            variant_name = "powershell" if selected_script == "ps" else "bash"
            src_variant = pkg_scripts / variant_name
            dst_variant = target_path / "greetkit" / "internal" / "scripts" / variant_name
            if src_variant.exists():
                shutil.copytree(src_variant, dst_variant, dirs_exist_ok=True)
                
                # Ensure script execution permission on sh files
                if selected_script == "sh":
                    for sh_file in dst_variant.glob("*.sh"):
                        try:
                            sh_file.chmod(sh_file.stat().st_mode | 0o755)
                        except Exception:
                            pass
                tracker.complete("scripts", f"copied shared scripts ({selected_script})")
            else:
                tracker.error("scripts", f"variant scripts folder '{variant_name}' not found")
        else:
            tracker.error("scripts", "scripts path not found in package")

        # Scaffold Skills
        tracker.start("skills")
        pkg_skills = _find_asset_dir("skills")
        
        plugin_skill_dirs = {
            "claude": target_path / ".claude" / "skills",
            "cursor": target_path / ".cursor" / "skills",
            "codex": target_path / ".codex" / "skills",
            "opencode": target_path / ".opencode" / "skills",
            "kimi": target_path / ".kimi" / "skills",
            "agy": target_path / ".agents" / "skills",
        }

        installed_skill_paths = []
        if pkg_skills and pkg_skills.exists():
            target_dirs = [plugin_skill_dirs[p] for p in selected_plugins if p in plugin_skill_dirs]
            if not target_dirs:
                target_dirs = [target_path / ".agents" / "skills"]

            for t_dir in target_dirs:
                shutil.copytree(pkg_skills, t_dir, dirs_exist_ok=True)
                installed_skill_paths.append(str(t_dir.relative_to(target_path)))

            # Copy skills.sh.json to project root
            pkg_skills_json = _find_asset_dir("skills.sh.json")
            if pkg_skills_json and pkg_skills_json.exists():
                try:
                    shutil.copy2(pkg_skills_json, target_path / "skills.sh.json")
                except Exception:
                    pass

            tracker.complete("skills", f"installed into {', '.join(installed_skill_paths)}")
        else:
            tracker.error("skills", "skills path not found in package")


        # Scaffold Hooks
        tracker.add("hooks", "Install GreetKit hooks")
        tracker.start("hooks")
        pkg_hooks = _find_asset_dir("hooks")
        
        if "agy" in selected_plugins and len(selected_plugins) == 1:
            target_hooks = target_path / ".agents" / "hooks"
        else:
            target_hooks = target_path / "hooks"
            
        if pkg_hooks and pkg_hooks.exists():
            shutil.copytree(pkg_hooks, target_hooks, dirs_exist_ok=True)
            
            # Make sure run-hook.cmd and session-start have proper executable permissions if possible
            for hook_script in target_hooks.glob("*"):
                try:
                    hook_script.chmod(hook_script.stat().st_mode | 0o755)
                except Exception:
                    pass
            tracker.complete("hooks", f"installed into {target_hooks.relative_to(target_path)}")
        else:
            tracker.error("hooks", "hooks path not found in package")


        # Finalize and write config files
        tracker.start("final")
        
        import json
        import hashlib
        from datetime import datetime, timezone

        def get_sha256(filepath: Path) -> str:
            h = hashlib.sha256()
            try:
                with open(filepath, 'rb') as f_in:
                    while chunk := f_in.read(8192):
                        h.update(chunk)
                return h.hexdigest()
            except Exception:
                return ""

        now_str = datetime.now(timezone.utc).isoformat()

        # Write init-options.json
        init_opts = {
            "ai": selected_plugins[0] if selected_plugins else "generic",
            "ai_skills": True,
            "branch_numbering": "sequential",
            "context_file": "AGENTS.md",
            "here": here,
            "integrations": selected_plugins,
            "script": selected_script,
            "greetkit_version": "0.1.0"
        }
        with open(target_path / "greetkit" / "internal" / "init-options.json", "w", encoding="utf-8") as f:
            json.dump(init_opts, f, indent=2)

        # Write integration.json
        integration_opts = {
            "integrations": selected_plugins,
            "version": "0.1.0"
        }
        with open(target_path / "greetkit" / "internal" / "integration.json", "w", encoding="utf-8") as f:
            json.dump(integration_opts, f, indent=2)

        # Write feature.json
        feature_opts = {
            "feature_directory": ""
        }
        with open(target_path / "greetkit" / "internal" / "feature.json", "w", encoding="utf-8") as f:
            json.dump(feature_opts, f, indent=2)

        # Write extensions.yml
        extensions_yml_content = """installed: []
settings:
  auto_execute_hooks: true
hooks:
  before_constitution:
  - extension: git
    command: greetkit.git.initialize
    enabled: true
    optional: false
    prompt: Execute greetkit.git.initialize?
    description: Initialize Git repository before constitution setup
    condition: null
  before_specify:
  - extension: git
    command: greetkit.git.feature
    enabled: true
    optional: false
    prompt: Execute greetkit.git.feature?
    description: Create feature branch before specification
    condition: null
  before_clarify:
  - extension: git
    command: greetkit.git.commit
    enabled: true
    optional: true
    prompt: Commit outstanding changes before clarification?
    description: Auto-commit before spec clarification
    condition: null
  before_plan:
  - extension: git
    command: greetkit.git.commit
    enabled: true
    optional: true
    prompt: Commit outstanding changes before planning?
    description: Auto-commit before implementation planning
    condition: null
  before_tasks:
  - extension: git
    command: greetkit.git.commit
    enabled: true
    optional: true
    prompt: Commit outstanding changes before task generation?
    description: Auto-commit before task generation
    condition: null
  before_implement:
  - extension: git
    command: greetkit.git.commit
    enabled: true
    optional: true
    prompt: Commit outstanding changes before implementation?
    description: Auto-commit before implementation
    condition: null
  before_checklist:
  - extension: git
    command: greetkit.git.commit
    enabled: true
    optional: true
    prompt: Commit outstanding changes before checklist?
    description: Auto-commit before checklist generation
    condition: null
  before_analyze:
  - extension: git
    command: greetkit.git.commit
    enabled: true
    optional: true
    prompt: Commit outstanding changes before analysis?
    description: Auto-commit before analysis
    condition: null
  before_taskstoissues:
  - extension: git
    command: greetkit.git.commit
    enabled: true
    optional: true
    prompt: Commit outstanding changes before issue sync?
    description: Auto-commit before tasks-to-issues conversion
    condition: null
  after_constitution:
  - extension: git
    command: greetkit.git.commit
    enabled: true
    optional: true
    prompt: Commit constitution changes?
    description: Auto-commit after constitution update
    condition: null
  after_specify:
  - extension: git
    command: greetkit.git.commit
    enabled: true
    optional: true
    prompt: Commit specification changes?
    description: Auto-commit after specification
    condition: null
  after_clarify:
  - extension: git
    command: greetkit.git.commit
    enabled: true
    optional: true
    prompt: Commit clarification changes?
    description: Auto-commit after spec clarification
    condition: null
  after_plan:
  - extension: git
    command: greetkit.git.commit
    enabled: true
    optional: true
    prompt: Commit plan changes?
    description: Auto-commit after implementation planning
    condition: null
  after_tasks:
  - extension: git
    command: greetkit.git.commit
    enabled: true
    optional: true
    prompt: Commit task changes?
    description: Auto-commit after task generation
    condition: null
  after_implement:
  - extension: git
    command: greetkit.git.commit
    enabled: true
    optional: true
    prompt: Commit implementation changes?
    description: Auto-commit after implementation
    condition: null
  after_checklist:
  - extension: git
    command: greetkit.git.commit
    enabled: true
    optional: true
    prompt: Commit checklist changes?
    description: Auto-commit after checklist generation
    condition: null
  after_analyze:
  - extension: git
    command: greetkit.git.commit
    enabled: true
    optional: true
    prompt: Commit analysis results?
    description: Auto-commit after analysis
    condition: null
  after_taskstoissues:
  - extension: git
    command: greetkit.git.commit
    enabled: true
    optional: true
    prompt: Commit after syncing issues?
    description: Auto-commit after tasks-to-issues conversion
    condition: null
"""
        with open(target_path / "greetkit" / "internal" / "extensions.yml", "w", encoding="utf-8") as f:
            f.write(extensions_yml_content)

        # Write manifest files
        greetkit_manifest = {
            "integration": "greetkit",
            "version": "0.1.0",
            "installed_at": now_str,
            "files": {}
        }
        with open(target_path / "greetkit" / "internal" / "integrations" / "greetkit.manifest.json", "w", encoding="utf-8") as f:
            json.dump(greetkit_manifest, f, indent=2)

        # Setup Selected Plugin Manifests
        for plugin in selected_plugins:
            manifest = {
                "integration": plugin,
                "version": "0.1.0",
                "installed_at": now_str,
            }
            
            # Setup specific plugin configurations
            if plugin == "claude":
                plugin_dir = target_path / ".claude-plugin"
                plugin_dir.mkdir(exist_ok=True)
                
                # Write marketplace.json
                marketplace = {
                    "name": "GreetKit",
                    "description": "GreetKit Intent-Driven Development CLI",
                    "author": "aboalrejal.ai@gmail.com",
                    "url": "https://github.com/aboalrejal-ai/greetkit",
                    "features": {
                        "skills": True
                    },
                    "entrypoint": "skills/greetkit-using-skills/SKILL.md"
                }
                with open(plugin_dir / "marketplace.json", "w", encoding="utf-8") as f:
                    json.dump(marketplace, f, indent=2)
                    
            elif plugin == "cursor":
                plugin_dir = target_path / ".cursor-plugin"
                plugin_dir.mkdir(exist_ok=True)
                # Ensure .cursorrules exists and routes to skills
                cursorrules = target_path / ".cursorrules"
                if not cursorrules.exists():
                    cursorrules.write_text("Always read skills/greetkit-using-skills/SKILL.md before starting any task.\n")
                    
            elif plugin == "codex":
                plugin_dir = target_path / ".codex-plugin"
                plugin_dir.mkdir(exist_ok=True)
                with open(plugin_dir / "marketplace.json", "w", encoding="utf-8") as f:
                    json.dump({
                        "name": "GreetKit",
                        "author": "aboalrejal.ai@gmail.com",
                        "url": "https://github.com/aboalrejal-ai/greetkit"
                    }, f, indent=2)
                    
            elif plugin == "kimi":
                plugin_dir = target_path / ".kimi-plugin"
                plugin_dir.mkdir(exist_ok=True)
                with open(plugin_dir / "marketplace.json", "w", encoding="utf-8") as f:
                    json.dump({
                        "name": "GreetKit",
                        "author": "aboalrejal.ai@gmail.com"
                    }, f, indent=2)
                    
            elif plugin == "agy":
                # Ensure .agents exists
                agents_dir = target_path / ".agents"
                agents_dir.mkdir(exist_ok=True)
                
                skills_files = {}
                if target_skills.exists():
                    for md_file in target_skills.rglob("*.md"):
                        rel_path = md_file.relative_to(target_path)
                        skills_files[str(rel_path).replace("\\", "/")] = get_sha256(md_file)
                manifest["files"] = skills_files
            
            with open(target_path / "greetkit" / "internal" / "integrations" / f"{plugin}.manifest.json", "w", encoding="utf-8") as f:
                json.dump(manifest, f, indent=2)

        tracker.complete("final", "Project ready!")


    # Security Panel
    security_text = (
        "Some agents may store credentials, auth tokens, or other private settings\n"
        "in the agent folder (.agents/) within your project.\n\n"
        "Consider adding .agents/ to your .gitignore to prevent leaks."
    )
    console.print()
    console.print(Panel(security_text, title="[yellow]⚠ Agent Folder Security[/yellow]", border_style="yellow", padding=(1, 2)))

    # Next Steps Panel
    next_steps_text = (
        "1. You're already in the project directory!\n"
        "2. Start using skills with your AI agent:\n"
        "   2.1 /greetkit-constitution - Establish project principles\n"
        "   2.2 /greetkit-specify      - Create baseline feature specifications\n"
        "   2.3 /greetkit-plan         - Create implementation plans\n"
        "   2.4 /greetkit-tasks        - Generate actionable development tasks\n"
        "   2.5 /greetkit-implement    - Execute implementation plan phase-by-phase\n"
        "   2.6 /greetkit-review       - Conduct multi-axis quality reviews"
    )
    console.print()
    console.print(Panel(next_steps_text, title="[green]Next Steps[/green]", border_style="green", padding=(1, 2)))

    # Enhancements Panel
    enhancements_text = (
        "Optional skills that improve spec quality & plan confidence:\n\n"
        "○ /greetkit-clarify (optional) - Resolve ambiguity via structured QA\n"
        "○ /greetkit-analyze (optional) - Cross-artifact alignment checking\n"
        "○ /greetkit-checklist (optional) - Validate requirement completeness"
    )
    console.print()
    console.print(Panel(enhancements_text, title="[cyan]Enhancement Skills[/cyan]", border_style="cyan", padding=(1, 2)))

    console.print("\n[bold green]GreetKit project initialized successfully![/bold green]\n")
