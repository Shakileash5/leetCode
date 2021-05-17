# Write your MySQL query statement below
select Score, dense_rank() over(order by score desc) as 'Rank' from scores;