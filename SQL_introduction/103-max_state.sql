-- script that displays the max temp
SELECT state,
MAX(value) max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC
