# Write your MySQL query statement below
select
    c1.visited_on,
    sum(c2.amount) as amount,
    round(sum(c2.amount) / 7, 2) as average_amount
from (select distinct visited_on from Customer) c1
join Customer c2
on datediff(c1.visited_on, c2.visited_on) between 0 and 6
group by c1.visited_on
having count(distinct c2.visited_on) = 7
order by c1.visited_on