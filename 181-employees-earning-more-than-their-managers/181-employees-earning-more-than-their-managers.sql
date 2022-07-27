# Write your MySQL query statement below
select a.name as employee
from employee as a
join employee as b
on a.ManagerId = b.Id
And a.Salary >b.Salary;
