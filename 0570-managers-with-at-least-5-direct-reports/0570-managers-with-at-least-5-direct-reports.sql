# Write your MySQL query statement below
select E1.name from Employee E1
join (select managerId,count(*) as directReports
    from Employee 
    group by managerId
    having count(*) >=5)
    E2 on E1.id=E2.managerid