# Write your MySQL query statement belowsel
select name as customers from customers
where id not in (select customerid from orders)