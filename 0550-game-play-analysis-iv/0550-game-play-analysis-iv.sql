# Write your MySQL query statement below
select
    round(
        count(distinct a2.player_id) / count(distinct a1.player_id)
    ,2) as fraction
from Activity a1
left join Activity a2
on a1.player_id = a2.player_id
and datediff(a2.event_date, a1.event_date) = 1 
where a1.event_date = (
    select min(a3.event_date)
    from Activity a3
    where a1.player_id = a3.player_id  
)