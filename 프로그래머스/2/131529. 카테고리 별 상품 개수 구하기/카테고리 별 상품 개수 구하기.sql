select category, count(product_id) as products
from (select *, substr(product_code, 1, 2) as category
from product) as sub
group by category