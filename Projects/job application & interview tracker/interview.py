import data

def schedule_interview(job_id, round_name, date, time, status, notes):

    if job_id not in data.applications:
        return None

    if data.interviews:
        interview_id = max(data.interviews.keys()) + 1
    else:
        interview_id = 1

    data.interviews[interview_id] = {
        "job_id": job_id,
        "round": round_name,
        "date": date,
        "time": time,
        "status": status,
        "notes": notes
    }

    return interview_id