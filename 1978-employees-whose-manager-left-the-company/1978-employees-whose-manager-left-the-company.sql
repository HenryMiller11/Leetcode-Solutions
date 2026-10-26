# Write your MySQL query statement below
select
    employee_id
from Employees
where salary < 30000
and manager_id not in(
    select employee_id
    from EMployees
)
order by employee_id