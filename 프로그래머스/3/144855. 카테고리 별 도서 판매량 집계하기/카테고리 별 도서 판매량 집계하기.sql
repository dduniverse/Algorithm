select a.category, sum(b.sales) as TOTAL_SALES
from book a
inner join book_sales b
on a.book_id = b.book_id
where YEAR(b.sales_date) = 2022 and MONTH(b.sales_date) = 01
group by a.category
order by a.category asc