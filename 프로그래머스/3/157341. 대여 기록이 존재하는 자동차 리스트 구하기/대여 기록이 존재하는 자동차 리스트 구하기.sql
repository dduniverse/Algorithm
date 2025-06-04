select distinct(a.car_id)
from car_rental_company_car a
inner join car_rental_company_rental_history b
on a.car_id = b.car_id
where MONTH(b.start_date) = 10 and a.car_type = '세단'
order by car_id desc