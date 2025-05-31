from prefect import task
import requests
from bs4 import BeautifulSoup

@task
def extract_jobs():
    print("EXTRACCIÓN DE OFERTAS DE LINKEDIN")
    url = "https://www.linkedin.com/jobs/search/?keywords=python"  # Reemplaza por URL real
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    job_cards = soup.select(".base-search-card__info")
    print(f"Se encontraron {len(job_cards)} ofertas laborales.")

    jobs = []

    for job_card in job_cards:
        title_tag = job_card.select_one(".base-search-card__title")
        location_tag = job_card.select_one(".job-search-card__location")
        link_tag = job_card.select_one(".hidden-nested-link")
        date_tag = job_card.select_one("time.job-search-card__listdate")

        job = {
            "title": title_tag.text.strip() if title_tag else None,
            "location": location_tag.text.strip() if location_tag else None,
            "link": link_tag["href"].strip() if link_tag else None,
            "date": date_tag["datetime"] if date_tag and date_tag.has_attr("datetime") else None
        }

        jobs.append(job)
        
    return jobs