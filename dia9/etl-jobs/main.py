from prefect import flow
from etl.extract import extract_jobs
from etl.transform import transform_jobs
from etl.load import load_jobs

@flow
def etl_pipeline():
    print("PIPELINE DE ETL LINKEDIN")
    jobs = extract_jobs()
    print(jobs)
    jobs_transformed = transform_jobs(jobs)
    print(jobs_transformed)
    load_jobs()
    print("ETL COMPLETADO")
    
etl_pipeline()