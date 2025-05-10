import time
import typer
from datetime import datetime, timedelta
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
from rich.progress import Progress, BarColumn, TimeRemainingColumn


app = typer.Typer()
console = Console()

def show_welcome():
    """Muestra un mensaje de bienvenida."""
    print("Hola 🤠!!")
    console.clear()
    console.print(
        Panel.fit(
            Text("🐍 TEMPORIZADOR PARA PYTHONERS 🐍", justify="center", style="bold bright_cyan"),
            subtitle="By @12aptor",
            border_style="bright_magenta",
        )
    )
    console.print("\n")
    console.print(Panel(
        "[bold bright_green]Instrucciones:[/]\n\n"
        "1. Ingresa el tiempo en uno de estos formatos:\n"
        "   - MM:SS (ej. 20:00)\n"
        "2. Presiona Enter para iniciar el temporizador.\n",
        title="¿Cómo usarlo?",
        border_style="bright_blue",
    ))

def display_time(total_seconds):
    """Muestra el temporiador con una interfaz"""
    start_time = datetime.now()
    end_time = start_time + timedelta(seconds=total_seconds)

    with Progress(
        "[progress.description]{task.description}",
        BarColumn(),
        "[progress.percentage]{task.percentage:>3.0f}%",
        TimeRemainingColumn(),
        console=console,
        refresh_per_second=10
    ) as progress:
        task = progress.add_task("[cyan]Tiempo restante", total=total_seconds)

        while True:
            elapsed_time = (datetime.now() - start_time).total_seconds()
            remaining = total_seconds - elapsed_time
            progress.update(
                task,
                advance=1,
                description=f"[cyan]Tiempo restante: [bold]{timedelta(seconds=int(remaining))}[/]"
            )
            time.sleep(1)

def parse_time(time_str):
    """Convierte una cadena de tiempo en un timedelta."""
    parts = time_str.split(":")
    m, s = parts
    return timedelta(minutes=int(m), seconds=int(s))

@app.command()
def start(time_str):
    show_welcome()
    time_delta = parse_time(time_str)
    total_seconds = int(time_delta.total_seconds())
    display_time(total_seconds)

app()