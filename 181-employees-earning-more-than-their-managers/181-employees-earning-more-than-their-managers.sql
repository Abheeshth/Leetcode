# Write your MySQL query statement below
select a.name as employee
from employee as a, employee as b
where a.ManagerId = b.Id
And a.Salary >b.Salary;
