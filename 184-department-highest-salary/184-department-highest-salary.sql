# Write your MySQL query statement below
Select Department.name as Department, employee.name as Employee, salary
from employee
join Department 
on Employee.DepartmentId =  Department.Id

where
(Employee.DepartmentId,Salary) IN
(select DepartmentId, MAX(Salary)

from 
Employee
Group By DepartmentId )
;
