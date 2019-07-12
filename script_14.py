class Employee:
    count = 0
    

# Create instances
hcl_emp = Employee()
tcs_emp = Employee()
cts_emp = Employee()

# Modify the class variables of each instance
hcl_emp.count = 100000000
tcs_emp.count = 20000
cts_emp.count = 10000

# There is no effect on class variables gets modified
# by instances
print( Employee.count )     # 0
print( hcl_emp.count  )     # 100000000
print( tcs_emp.count  )     # 20000
print( cts_emp.count  )     # 10000
