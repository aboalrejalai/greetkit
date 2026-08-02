import typer
from greetkit_cli._console import BannerGroup
from greetkit_cli.commands import init, status, upgrade

app = typer.Typer(
    cls=BannerGroup,
    help="GreetKit Intent-Driven Development CLI"
)

app.add_typer(init.app)
app.add_typer(status.app)
app.add_typer(upgrade.app)

@app.callback()
def callback():
    """
    GreetKit Intent-Driven Development CLI
    """
    pass

if __name__ == "__main__":
    app()
