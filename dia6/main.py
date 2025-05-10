import typer

app = typer.Typer()

@app.command()
def start():
    print("Hola 😎!!")

app()