# Write your MySQL query statement below
#select name from (select Id,name,salary,managerId from Employee where managerId is not Null) as worker
#where worker.salary > (SELECT salary FROM Employee LIMIT managerId,1) 
select worker.name as Employee from (select Id,name,salary,managerId from Employee) as worker join (select id,name,salary from Employee ) as manager on worker.managerid = manager.id where worker.salary > manager.salary;