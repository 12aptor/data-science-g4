from prefect import flow
from etl.extract import extract_jobs


@flow
def etl_pipeline():
    jobs = extract_jobs()
    print(jobs)

if __name__ == "__main__":
    etl_pipeline()
