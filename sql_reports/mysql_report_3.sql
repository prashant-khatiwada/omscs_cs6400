-- Shown individual Table each for Heater, Heat Pump and Air Conditioner

-- AC
SELECT
    household_types,
    COUNT(AirConditioner.appliance_number) AS count,
    ROUND(AVG(Appliance.btu_rating)) AS average_btu,
	ROUND(AVG(AirConditioner.eer),1) AS average_eer
FROM
    AirConditioner
INNER JOIN Appliance ON AirConditioner.email = Appliance.email
INNER JOIN Household ON AirConditioner.email = Household.email
GROUP BY
    Household.household_types
ORDER BY
    household_types


-- Heater
SELECT
    household_types,
    COUNT(Heater.appliance_number) AS count,
    ROUND(AVG(Appliance.btu_rating)) AS average_btu,
    (SELECT energy_source FROM Heater RIGHT JOIN Household ON Heater.email = Household.email
	GROUP BY energy_source ORDER BY COUNT(*) DESC LIMIT 1 ) AS common_source
FROM
    Heater
INNER JOIN Appliance ON Heater.email = Appliance.email
INNER JOIN Household ON Heater.email = Household.email
GROUP BY
    Household.household_types
ORDER BY
    household_types



-- HeatPump
SELECT
    Household.household_types,
    COUNT(HeatPump.appliance_number) AS count,  -- THIS DISPLAYS A VERY LARGE NUMBER
    ROUND(AVG(Appliance.btu_rating)) AS average_btu,
	ROUND(AVG(HeatPump.seer), 1) AS average_seer, 
	ROUND(AVG(HeatPump.hspf), 1) AS average_hspf
FROM
    HeatPump 
    INNER JOIN Appliance ON HeatPump.email = Appliance.email
    INNER JOIN Household ON HeatPump.email = Household.email
GROUP BY
    Household.household_types
ORDER BY
    household_types
