--costo por ubicacion
SELECT LeakID,
	Plant,
	Location,
	SUM(Annual_Cost) AS Location_cost
 FROM fact_leaks
 GROUP BY Plant, Location