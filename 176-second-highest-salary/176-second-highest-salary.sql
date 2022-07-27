# Write your MySQL query statement below
Select 
IFNULL(
    (Select Distinct salary 
from Employee 
order by salary desc
limit 1 offset 1),NULL) AS SecondHighestSalary

