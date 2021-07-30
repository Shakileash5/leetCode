# Write your MySQL query statement below
#Select  Customers.Name as Customers from Customers Left Join Orders on Customers.id = Orders.CustomerId where Orders.CustomerId is Null; 

select name as "Customers" from Customers where id not in (select customerId from orders);
#select C1.name as "Customers" from Customers C1 left join orders C2 on C1.id = C2.CustomerId ;