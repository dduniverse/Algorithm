select mcdp_cd as 진료과코드, count(mcdp_cd) as 5월예약건수
from appointment
where apnt_ymd > '2022-04-30' and apnt_ymd < '2022-06-01'
group by mcdp_cd
order by 5월예약건수 asc, 진료과코드 asc