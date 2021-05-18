# Write your MySQL query statement below
#select name from (select Id,name,salary,managerId from Employee where managerId is not Null) as worker
#where worker.salary > (SELECT salary FROM Employee LIMIT managerId,1) 
#select worker.name as Employee from (select Id,name,salary,managerId from Employee) as worker join (select id,name,salary from Employee ) as manager on worker.managerid = manager.id where worker.salary > manager.salary;

select e.name as 'Employee' from (select id,name,managerId,salary from Employee) as e join
    (select id,name,salary from employee) as m on e.managerId = m.id
    where e.salary>m.salary;