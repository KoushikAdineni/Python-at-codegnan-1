import data
def get_status_report() -> dict:
    report = {}
    for job in data.applications.values():
        status = job["status"]
        report[status] = report.get(status, 0) + 1
    return report
