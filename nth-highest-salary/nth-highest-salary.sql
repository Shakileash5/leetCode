CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
        Select Distinct Salary from
      (SELECT Salary, dense_rank() over(order by Salary desc) as rnk
      FROM Employee) as emp
      where rnk = N 
  );
END