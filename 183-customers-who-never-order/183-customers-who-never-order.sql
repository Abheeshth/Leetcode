# Write your MySQL query statement below
Select name as Customers 
FROM Customers
where id Not IN
(
SELECT customerId 
    from Orders
);