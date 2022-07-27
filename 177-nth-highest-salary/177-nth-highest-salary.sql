CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
declare m int;
set M = N-1;
  RETURN (
      # Write your MySQL query statement below.
      select distinct salary 
      from employee 
      ORDER BY Salary DESC
      limit 1 offset M
      
  );
END