from prefect import task

@task
def load_jobs():
    print("CARGA DE OFERTAS DE LINKEDIN")