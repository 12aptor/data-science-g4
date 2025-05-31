from prefect import flow
from etl.extract import extract_jobs
from etl.transform import transform_jobs
from etl.load import load_jobs

@flow
def etl_pipeline():
    print("PIPELINE DE ETL LINKEDIN")
    extract_jobs()
    transform_jobs()
    load_jobs()
    print("ETL COMPLETADO")
    
etl_pipeline()