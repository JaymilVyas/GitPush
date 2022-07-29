-- Database Operations
show databases
create database JimmyTask7Dress
use JimmyTask7Dress

-- Q1.: Create a  table attribute dataset and dress dataset
-- Q2.: Do a bulk load for these two table for respective dataset 
select * from attributedataset
select * from dresssales

-- Q6.: In sql task try to perform left join operation with attrubute dataset and dress dataset on column Dress_ID
select *
from attributedataset a
left join dresssales b on a.Dress_ID=b.Dress_ID

-- Q7.: Write a sql query to find out how many unique dress that we have based on dress id
select count(DISTINCT Dress_ID)'unique dress count'
from attributedataset

-- Q8.: Try to find out how mnay dress is having recommendation 0
select *
from attributedataset
where Recommendation=1

-- Q9.: Try to find out total dress sell for individual dress id
select Dress_ID,
(`29-08-2013`+`31-08-2013`+`09-02-2013`+`09-04-2013`+`09-06-2013`+`09-08-2013`+`09-10-2013`+`09-12-2013`+`14-09-2013`+`16-09-2013`+`18-09-2013`+`20-09-2013`+
`22-09-2013`+`24-09-2013`+`26-09-2013`+`28-09-2013`+`30-09-2013`+`10-02-2013`+`10-04-2013`+`10-06-2013`+`10-08-2010`+`10-10-2013`+`10-12-2013`)'Total Dress Sale'
from dresssales

-- Q10.: Try to find out a third highest most selling dress id
select Dress_ID,
(`29-08-2013`+`31-08-2013`+`09-02-2013`+`09-04-2013`+`09-06-2013`+`09-08-2013`+`09-10-2013`+`09-12-2013`+`14-09-2013`+`16-09-2013`+`18-09-2013`+`20-09-2013`+
`22-09-2013`+`24-09-2013`+`26-09-2013`+`28-09-2013`+`30-09-2013`+`10-02-2013`+`10-04-2013`+`10-06-2013`+`10-08-2010`+`10-10-2013`+`10-12-2013`)'Total Dress Sale'
from dresssales
order by 2 desc