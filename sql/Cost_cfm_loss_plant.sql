--costo y cfm perdido por planta
SELECT
Plant,
SUM(Annual_Cost) as Total_Loss,
sum(CFM_loss) as cfm_loss_plant
FROM fact_leaks
GROUP BY Plant
ORDER BY Total_Loss DESC