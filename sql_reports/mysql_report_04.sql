
-- PART ONE
-- Water heater statistics by ALL state
SELECT
    Address.state AS state,
    IFNULL(ROUND(AVG(WaterHeater.capacity)), 0) AS avg_capacity,
    IFNULL(ROUND(AVG(Appliance.btu_rating)), 0) AS avg_btu,
    IFNULL(ROUND(AVG(WaterHeater.temperature), 1), 0) AS avg_temp,
    IFNULL(COUNT(CASE WHEN WaterHeater.temperature IS NOT NULL THEN 1 END), 0) AS temp_set,
    IFNULL(COUNT(CASE WHEN WaterHeater.temperature IS NULL THEN 1 END), 0) AS temp_no_set
FROM
    Household
    LEFT JOIN Address ON Household.postal_code = Address.postal_code
    LEFT JOIN WaterHeater ON Household.email = WaterHeater.email
    LEFT JOIN Appliance ON WaterHeater.email = Appliance.email AND WaterHeater.appliance_number = Appliance.appliance_number
GROUP BY 
	Address.state
ORDER BY 
	Address.state ASC;



-- PART 2 - DRILLDOWN
-- FOR A PARTICULAR STATE
SET @search = 'CA'; -- replace with user input

SELECT
    Address.state AS State,
    WaterHeater.energy_source AS EnergySource,
    -- capacity
    ROUND(MIN(WaterHeater.capacity),0) AS MinCapacity,
    ROUND(AVG(WaterHeater.capacity),0) AS AvgCapacity,
    ROUND(MAX(WaterHeater.capacity),0) AS MaxCapacity,
    -- temp
    ROUND(MIN(WaterHeater.temperature),1) AS MinTemp,
    ROUND(AVG(WaterHeater.temperature), 1) AS AvgTemp,
    ROUND(MAX(WaterHeater.temperature),1) AS MaxTemp
FROM
    WaterHeater
    INNER JOIN Appliance ON WaterHeater.email = Appliance.email 
    INNER JOIN Household ON Household.email = WaterHeater.email
    INNER JOIN Address ON Household.postal_code = Address.postal_code   
WHERE 
    Address.state = @search
GROUP BY 
    WaterHeater.energy_source
ORDER BY 
    WaterHeater.energy_source ASC;