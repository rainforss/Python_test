work_hours = [('Abby',100),('Billy',400),('Cassie',800)]

def findEmployeeHours(work_hours):
    current_max = 0
    employee_of_month = ''
    for employee,hours in work_hours:
        if hours>current_max:
            current_max=hours
            employee_of_month=employee




    return(employee_of_month,current_max)


# Unpack the returned turple, similar to javascript destructuring
name,hour = findEmployeeHours(work_hours)

print(name,hour)

