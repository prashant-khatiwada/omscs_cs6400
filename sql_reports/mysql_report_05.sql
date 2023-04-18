-- Table 01
-- the state with the most off-the-grid households 
SELECT Address.state, COUNT(*) AS count
FROM Household
  JOIN Address ON Household.postal_code = Address.postal_code
  LEFT JOIN PublicUtility ON Household.email = PublicUtility.email
WHERE PublicUtility.public_utility = 'Off-The-Grid'
GROUP BY Address.state
-- if max count in more than 1 state
HAVING count = (
  SELECT MAX(count)
FROM (
    SELECT COUNT(*) AS count
  FROM Household
    JOIN Address ON Household.postal_code = Address.postal_code
    LEFT JOIN PublicUtility ON Household.email = PublicUtility.email
  WHERE PublicUtility.public_utility = 'Off-The-Grid'
  GROUP BY Address.state
  ) AS t
)
ORDER BY count;


-- NOTICE - NOT SURE WHICH TABLE 02 is required, so made both.
-- Table 02 - for all state (all data)
-- Non state specific
SELECT
  generation_type,
  COUNT(*) AS total_count,
  ROUND(COUNT(*) / (SELECT COUNT(*) FROM PowerGeneration WHERE generation_type IN ('solar-electric', 'wind')) * 100, 1) as percentage
FROM PowerGeneration
  JOIN Household ON Household.email = PowerGeneration.email
  JOIN PublicUtility ON Household.email = PublicUtility.email
WHERE  PublicUtility.public_utility = 'Off-The-Grid'
GROUP BY PowerGeneration.generation_type;

-- Table 02 - for state specific
-- State specific
SELECT 
  Address.state AS state, 
  ROUND(AVG(PowerGeneration.battery_storage_capacity)) AS average_battery_capacity
FROM Household
  LEFT JOIN Address ON Household.postal_code = Address.postal_code
  LEFT JOIN PowerGeneration ON Household.email = PowerGeneration.email
  LEFT JOIN PublicUtility ON Household.email = PublicUtility.email
WHERE PublicUtility.public_utility = 'Off-The-Grid'
GROUP BY state;


-- Table 03 (mixed NOT substracted from both solar_electric and wind)
SELECT 
    CONCAT(ROUND(((SELECT COUNT(*) AS total_count
        FROM PowerGeneration
        WHERE PowerGeneration.email IN (
            SELECT email
            FROM PowerGeneration
            GROUP BY email
            HAVING COUNT(DISTINCT generation_type) > 1
        )
    ) / COUNT(*)) * 100, 1), '%') AS mixed_percentage,
    
    CONCAT(ROUND((SUM(CASE WHEN generation_type = 'solar-electric' THEN 1 ELSE 0 END) / COUNT(*)) * 100, 1), '%') AS solar_electric_percentage,
    
    CONCAT(ROUND(( (SUM(CASE WHEN generation_type = 'wind' THEN 1 ELSE 0 END)) / COUNT(*)) * 100, 1), '%') AS wind_percentage
    
FROM PowerGeneration
  JOIN Household ON Household.email = PowerGeneration.email
  JOIN PublicUtility ON Household.email = PublicUtility.email
WHERE PublicUtility.public_utility = 'Off-The-Grid';




-- Table 03 (mixed substracted from both solar_electric and wind)
SELECT 
    CONCAT(ROUND(((SELECT COUNT(*) AS total_count
        FROM PowerGeneration
        WHERE PowerGeneration.email IN (
            SELECT email
            FROM PowerGeneration
            GROUP BY email
            HAVING COUNT(DISTINCT generation_type) > 1
        )
    ) / COUNT(*)) * 100, 1), '%') AS mixed_percentage,
    
    CONCAT(ROUND(((SUM(CASE WHEN generation_type = 'solar-electric' THEN 1 ELSE 0 END)-(SELECT COUNT(*) AS total_count
        FROM PowerGeneration
        WHERE PowerGeneration.email IN (
            SELECT email
            FROM PowerGeneration
            GROUP BY email
            HAVING COUNT(DISTINCT generation_type) > 1
        )
    )) / COUNT(*)) * 100, 1), '%') AS se_only_percentage,
    
    CONCAT(ROUND(( (SUM(CASE WHEN generation_type = 'wind' THEN 1 ELSE 0 END) - (SELECT COUNT(*) AS total_count
        FROM PowerGeneration
        WHERE PowerGeneration.email IN (
            SELECT email
            FROM PowerGeneration
            GROUP BY email
            HAVING COUNT(DISTINCT generation_type) > 1
        )
    )) / COUNT(*)) * 100, 1), '%') AS wind_only_percentage    
    
FROM PowerGeneration
  JOIN Household ON Household.email = PowerGeneration.email
  JOIN PublicUtility ON Household.email = PublicUtility.email
WHERE PublicUtility.public_utility = 'Off-The-Grid';






-- Table 04
-- average water heater gallon capacity Off-the-grid Vs Not
SELECT
  ROUND(AVG(CASE WHEN PublicUtility.public_utility != 'Off-The-Grid' THEN WaterHeater.capacity END), 1) AS grid_avg_capacity,
  ROUND(AVG(CASE WHEN PublicUtility.public_utility = 'Off-The-Grid' THEN WaterHeater.capacity END), 1) AS off_grid_avg_capacity
FROM Household
  JOIN PowerGeneration ON Household.email = PowerGeneration.email
  LEFT JOIN PublicUtility ON Household.email = PublicUtility.email
  JOIN Appliance ON Household.email = Appliance.email
  LEFT JOIN WaterHeater ON Appliance.appliance_number = WaterHeater.appliance_number AND Appliance.email = WaterHeater.email;



-- Table 05
-- minimum, average and maximum (as whole numbers, rounded) BTUs for all OFF GRID
SELECT
  Appliance.appliance_type,
  ROUND(MIN(Appliance.btu_rating), 0) AS min_btu,
  ROUND(AVG(Appliance.btu_rating), 0) AS avg_btu,
  ROUND(MAX(Appliance.btu_rating), 0) AS max_btu
FROM Household
  JOIN PowerGeneration ON Household.email = PowerGeneration.email
  LEFT JOIN PublicUtility ON Household.email = PublicUtility.email
  JOIN Appliance ON Household.email = Appliance.email
WHERE PublicUtility.public_utility = 'Off-The-Grid'
GROUP BY Appliance.appliance_type;
