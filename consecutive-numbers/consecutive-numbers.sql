# Write your MySQL query statement below

#select Distinct l1.Num as "ConsecutiveNums" from Logs as l1, logs as l2, logs as l3 where l2.id+1 = l1.id and l3.id = l1.id+2 and l2.num = l1.num and l3.num = l1.num;

Select Distinct logA.Num as "ConsecutiveNums" from (Select id,Num, LEAD(num,1) OVER(order by id) as num2, LEAD(num,2) OVER(order by id) as num3 from Logs) as logA where logA.Num = logA.num2 and logA.num2 = logA.num3;