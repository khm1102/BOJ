select
    car_id,
    case
        when max(case when '2022-10-16' >= start_date and '2022-10-16' <= end_date then 1 else 0 end) = 1 then '대여중'
        else '대여 가능'
    end as availability
from
    car_rental_company_rental_history
group by
    car_id
order by
    car_id desc;