import search
import data

def search_by_company(company_name):

    result = {}

    for job_id, job in data.applications.items():

        if job["company"].lower() == company_name.lower():

            result[job_id] = job

    return result