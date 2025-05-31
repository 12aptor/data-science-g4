from prefect import task

@task
def transform_jobs():
    print("TRANSFORMACIÓN DE OFERTAS DE LINKEDIN")