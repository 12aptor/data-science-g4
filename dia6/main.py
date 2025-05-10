import typer
from rich.panel import Panel
from rich.console import Console
from rich.text import Text

app = typer.Typer()
console = Console()

def show_welcome():
    """Muestra un mensaje de bienvenida."""
    print("Hola 🤠!!")
    console.clear()
    console.print(
        Panel.fit(
            Text("🐍 TEMPORIZADOR PARA PYTHONERS 🐍", justify="center", style="bold bright_cyan"),
        )
    )
    

@app.command()
def start():
    show_welcome()

app()