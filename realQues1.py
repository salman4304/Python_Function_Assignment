def salary_avg(all_salaries):
    total_salaries=sum(all_salaries)
    total_emp=len(all_salaries)
    return total_salaries/total_emp
salaries=[]
No_emp=int(input("Enter Number of Employee"))
for x in range(No_emp):
    salary=float(input("Please Enter Salary of Employee"))
    salaries.append(salary)
print(f"Salaries Average is",salary_avg(salaries))