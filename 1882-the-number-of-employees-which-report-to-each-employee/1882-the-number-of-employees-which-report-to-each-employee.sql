# Write your MySQL query statement below
SELECT  
    e.employee_id, 
    e.name,  
    COUNT(e1.reports_to) AS reports_count, 
    ROUND(AVG(e1.age * 1.0), 0) AS average_age  
FROM 
    Employees e 
    INNER JOIN Employees e1 ON e.employee_id = e1.reports_to 
WHERE 
    e1.reports_to IS NOT NULL 
GROUP BY 
    e.employee_id, e.name 
ORDER BY 
    e.employee_id;