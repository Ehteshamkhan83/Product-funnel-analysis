CREATE DATABASE ecommerce_analysis;

USE ecommerce_analysis;


-- Daily user activity trend 

SELECT TOP 10
    CAST(REPLACE(event_time,' UTC','') AS DATE) AS event_date,
    COUNT(*) AS total_events
FROM events_data
GROUP BY CAST(REPLACE(event_time,' UTC','') AS DATE)
ORDER BY event_date;

-- Identify most active users

SELECT TOP 10
    user_id,
    COUNT(*) AS total_actions
FROM events_data
GROUP BY user_id
ORDER BY total_actions DESC;


-- Top performing brands

SELECT TOP 10
    brand,
    COUNT(*) AS purchases
FROM events_data
WHERE event_type='purchase'
GROUP BY brand
ORDER BY purchases DESC;

-- Average purchase price

SELECT 
    AVG(price) AS avg_purchase_price
FROM events_data
WHERE event_type='purchase';

