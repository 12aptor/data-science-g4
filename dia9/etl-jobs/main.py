from prefect import flow
from etl.extract import extract_jobs
from etl.transform import transform_jobs
from etl.load import load_jobs

@flow
def etl_pipeline():
    print("PIPELINE DE ETL LINKEDIN")
    jobs = extract_jobs()
    jobs_transformed = transform_jobs(jobs)
    load_jobs(jobs_transformed)
    print("ETL COMPLETADO")
    
etl_pipeline()