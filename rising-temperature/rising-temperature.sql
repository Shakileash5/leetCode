# Write your MySQL query statement below
Select Distinct W2.id from Weather W1 , Weather W2 where W1.recordDate + INTERVAL 1 DAY = W2.recordDate  and W1.Temperature < W2.Temperature;