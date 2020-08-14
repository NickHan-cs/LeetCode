# Write your MySQL query statement below
select a.Id from Weather a, Weather b where DATEDIFF(a.RecordDate, b.RecordDate)=1 and a.Temperature>b.Temperature; 