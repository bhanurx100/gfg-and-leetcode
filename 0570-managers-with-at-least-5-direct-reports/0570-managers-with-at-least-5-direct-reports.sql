select name from Employee
where Id in (select managerId from Employee
group by managerId
having count(*)>=5)