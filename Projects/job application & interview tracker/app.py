import data
import jobs
import interview
import update
import delete
import search
import report



if __name__ == "__main__":
    print("Welcome to Job Application & Interview Tracker")
    
    while True:
        print("\nServices:")
        print("1. View All Jobs")
        print("2. Add Job Application")
        print("3. Schedule Interview")
        print("4. Update Job Status")
        print("5. Delete Job Application")
        print("6. Search by Company")
        print("7. Status Breakdown Report")
        print("8. Logout")
        
        choice = int(input("Select choice (1-8): "))



        
        if choice == 1:
            if not data.applications:

               print("No Job Applications Found.")
            else:
               print(" JOB APPLICATIONS ")

               for job_id, job in data.applications.items():
                   print(f"""
            Job ID       : {job_id}
            Company      : {job['company']}
            Role         : {job['role']}
            Status       : {job['status']}
            Applied Date : {job['applied_date']}
            Salary       : {job['salary']}
            ----------------------------------------
            """)
            

        elif choice == 2:
            company = input("Enter Company Name: ")
            role = input("Enter Role: ")
            status = input("Enter Status: ")
            date = input("Enter Applied Date (YYYY-MM-DD): ")
            salary = int(input("Enter Salary: "))
            res = jobs.add_job(company, role, status, date, salary)
            print(f"Successfully added Job with ID: {res}")

        elif choice == 3:
            job_id = int(input("Enter Job ID: "))
            round_name = input("Enter Interview Round: ")
            date = input("Enter Date: ")
            time = input("Enter Time: ")
            status = input("Enter Status: ")
            notes = input("Enter Notes: ")
            res = interview.schedule_interview(job_id, round_name, date, time, status, notes)
            print(f"Successfully scheduled Interview with ID: {res}")

        elif choice == 4:
            job_id = int(input("Enter Job ID to update: "))
            new_status = input("Enter New Status: ")
            res = update.update_job(job_id, new_status)
            print(f"Update status: {res}")

        elif choice == 5:
            job_id = int(input("Enter Job ID to delete: "))
            res = delete.delete_job(job_id)
            print(f"Deletion status: {res}")

        elif choice == 6:
            company = input("Enter company name to search: ")
            res = search.search_by_company(company)
            print(res)

        elif choice == 7:
            res = report.get_status_report()
            print(res)

        elif choice == 8:
            print("Logged out successfully!")
            break
        else:
            print("Invalid Choice!")
