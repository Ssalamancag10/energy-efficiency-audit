--Top 10 fugas mas costosas
SELECT
LeakID,
Plant,
Location,
Annual_Cost
FROM fact_leaks
ORDER BY Annual_Cost DESC
LIMIT 10