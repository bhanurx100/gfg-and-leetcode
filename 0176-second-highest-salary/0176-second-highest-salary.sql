# Write your MySQL query statement below
SELECT DISTINCT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE Salary< (SELECT MAX(salary) FROM Employee)