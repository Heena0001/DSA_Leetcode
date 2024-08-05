SELECT 
    user_id, 
    IFNULL(ROUND(SUM(action='confirmed') / COUNT(*), 2), 0) AS confirmation_rate
FROM 
    Signups
LEFT JOIN 
    Confirmations USING (user_id)
GROUP BY 
    user_id;
