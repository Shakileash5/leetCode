CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  set N = N-1;
  RETURN (
      # Write your MySQL query statement below.
      # Select Distinct Salary from
      #(SELECT Salary, dense_rank() over(order by Salary desc) as rnk
      #FROM Employee) as emp
      #where rnk = N 
       #select distinct salary 
       # from 
       #     ( select salary,dense_rank() over( order by salary desc) as ran from Employee ) as emp
       # where 
       #     ran = N
      select DISTINCT salary from employee order by salary desc limit 1 offset N
  );
END