# Write your MySQL query statement below
#Select DEmployee.Dname,DEmployee.EName,DEmployee.ESal From (Select Department.Name as DName,Employee.Name as EName,Employee.Salary as ESal from Employee INNER Join Department on Employee.DepartmentId = Department.Id ) as DEmployee group by DEmployee.Dname order by DEmployee.Dname;

Select DEmployee.Dname as Department,DEmployee.EName as Employee,DEmployee.ESal as Salary From (Select Department.Name as DName,Employee.Name as EName,Employee.Salary as ESal ,Employee.DepartmentId  as Id from Employee INNER Join Department on Employee.DepartmentId = Department.Id ) as DEmployee where (DEmployee.Id,DEmployee.ESal )In (Select DepartmentId,max(Salary) from Employee group by DepartmentId )

