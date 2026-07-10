import data

def add_job(company, role, status, applied_date, salary):

    if data.applications:
        job_id = max(data.applications.keys()) + 1
    else:
        job_id = 101

    data.applications[job_id] = {
        "company": company,
        "role": role,
        "status": status,
        "applied_date": applied_date,
        "salary": salary
    }

    return job_id