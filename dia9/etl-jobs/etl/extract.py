from prefect import task

@task
def extract_jobs():
    print("EXTRACCIÓN DE OFERTAS DE LINKEDIN")