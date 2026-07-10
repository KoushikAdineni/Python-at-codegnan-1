import data

def delete_job(job_id):

    if job_id in data.applications:

        del data.applications[job_id]

    

        remove = []

        for interview_id, interview in data.interviews.items():

            if interview["job_id"] == job_id:

                remove.append(interview_id)

        for interview_id in remove:

            del data.interviews[interview_id]

        return True

    return False