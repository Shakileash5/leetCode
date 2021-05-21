# Write your MySQL query statement below
select distinct c.class from (select distinct student,class from courses) c group by c.class having count(*)>=5; 