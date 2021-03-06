# Write your MySQL query statement below

#select Distinct l1.Num as "ConsecutiveNums" from Logs as l1 join logs as l2 on l2.id+1 = l1.id join logs as l3 on  l3.id = l2.id+2 where l2.num = l1.num and l3.num = l1.num;

#Select Distinct logA.Num as "ConsecutiveNums" from (Select id,Num, LEAD(num,1) OVER(order by id) as num2, LEAD(num,2) OVER(order by id) as num3 from Logs) as logA where logA.Num = logA.num2 and logA.num2 = logA.num3;

select distinct l1.num as "ConsecutiveNums" from logs as l1, logs as l2, logs as l3 
    where l1.id = l2.id+1 and l2.id = l3.id + 1 and l1.num = l2.num and l2.num = l3.num;