select 
    product_id,
    coalesce(
        (
            select p2.new_price
            from Products p2
            where p2.product_id = p.product_id
            and p2.change_date <= '2019-08-16'
            order by p2.change_date desc
            limit 1
        ),10
    ) as price
from Products p
group by product_id
