with a as (
select car_id, daily_fee
from car_rental_company_car
where car_type = "트럭"
), b as (
select duration_type, discount_rate
from car_rental_company_discount_plan
where car_type = "트럭"
), c as (
select rh.history_id, a.daily_fee, datediff(rh.end_date, rh.start_date)+1 rent_duration, 
(case
	 when datediff(rh.end_date, rh.start_date)+1 > 90 then "90일 이상"
	 when datediff(rh.end_date, rh.start_date)+1 > 30 then "30일 이상"
	 when datediff(rh.end_date, rh.start_date)+1 > 7 then "7일 이상"
	 else "해당 없음"
 end) duration_type
 from a join car_rental_company_rental_history rh on a.car_id = rh.car_id
)
select c.history_id, 
round((1-(0.01*coalesce(b.discount_rate, 0)))*c.daily_fee*c.rent_duration) as FEE
from c left join b on c.duration_type = b.duration_type
order by FEE desc, history_id desc