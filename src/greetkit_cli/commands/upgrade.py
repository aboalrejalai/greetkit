import typer
import subprocess
import sys
from rich.console import Console

console = Console()
app = typer.Typer(help="Upgrade GreetKit CLI")

@app.command("upgrade")
def upgrade():
    """
    Upgrade the GreetKit CLI to the latest version.
    """
    console.print("Upgrading GreetKit...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "greetkit"])
        console.print("[bold green]Upgrade complete![/bold green]")
    except Exception as e:
        console.print(f"[bold red]Upgrade failed:[/bold red] {e}")
