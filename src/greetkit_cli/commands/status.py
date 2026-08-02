import typer
from pathlib import Path
from rich.console import Console

console = Console()
app = typer.Typer(help="Check GreetKit project status")

@app.command("status")
def status(
    path: Path = typer.Argument(Path("."), help="Path to check", file_okay=False, dir_okay=True, resolve_path=True)
):
    """
    Check the status and integrity of the current GreetKit project.
    """
    console.print(f"Checking GreetKit status in [bold cyan]{path}[/bold cyan]...")
    
    components = [
        ".specs",
        ".plan",
        ".agents",
        "skills",
        "templates"
    ]
    
    missing = []
    for c in components:
        if not (path / c).exists():
            missing.append(c)
            
    if missing:
        console.print(f"[bold red]Warning: Missing components:[/bold red] {', '.join(missing)}")
        console.print("Run [bold cyan]greetkit init[/bold cyan] to scaffold missing directories.")
    else:
        console.print("[bold green]Project structure is intact![/bold green]")
        
    # Check skills presence
    skills_dir = path / "skills"
    if skills_dir.exists():
        console.print("\n[bold]Installed Skills:[/bold]")
        for skill_dir in skills_dir.iterdir():
            if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
                console.print(f"  - [green]{skill_dir.name}[/green]")
    
    console.print("\n[bold cyan]Status check complete.[/bold cyan]")
