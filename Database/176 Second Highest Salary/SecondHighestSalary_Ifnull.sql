# Write your MySQL query statement below
select ifnull(
	(select distinct Salary from Employee order by Salary DESC limit 1 offset 1), null
) as SecondHighestSalary;