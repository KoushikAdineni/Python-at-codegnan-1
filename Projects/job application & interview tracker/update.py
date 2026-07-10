import data

def update_job(job_id, new_status):

    if job_id in data.applications:

        data.applications[job_id]["status"] = new_status

        return True

    return False