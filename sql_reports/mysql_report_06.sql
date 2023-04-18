SET @center_postal_code = '30310'; -- replace with user input
SET @search_radius = 250; -- replace with user input

SELECT 
		Household.household_types,
        COUNT(*) AS household_count,
        -- Household types
        SUM(CASE WHEN household_types = 'House' THEN 1 ELSE 0 END) AS type_house,
    	SUM(CASE WHEN household_types = 'Apartment' THEN 1 ELSE 0 END) AS type_apartment,
	    SUM(CASE WHEN household_types = 'Townhome' THEN 1 ELSE 0 END) AS type_townhome,
    	SUM(CASE WHEN household_types = 'Condominium' THEN 1 ELSE 0 END) type_condominium,
    	SUM(CASE WHEN household_types = 'Mobile Home' THEN 1 ELSE 0 END) AS type_mobile_home,
		-- Temperature
        ROUND(AVG(Household.square_footage)) AS Avg_Sq_Ft, 
    	COALESCE(ROUND(AVG(Heating.temperature), 1), 0.0) AS Avg_Heating_Temp, 
    	COALESCE(ROUND(AVG(Cooling.temperature), 1), 0.0) AS Avg_Cooling_Temp,
        -- Public Utility
        GROUP_CONCAT(DISTINCT PublicUtility.public_utility SEPARATOR ',') AS used_public_utilities,
        COALESCE(SUM(CASE WHEN PublicUtility.public_utility = 'Off-The-Grid' THEN 1 ELSE 0 END), 0) AS off_grid_count,
        -- Power Generation
        COALESCE(SUM(CASE WHEN PowerGeneration.generation_type IS NOT NULL THEN 1 ELSE 0 END), 0) AS power_generation_count,
        (SELECT GROUP_CONCAT(DISTINCT generation_type SEPARATOR ',') as generation_types
        FROM PowerGeneration
			GROUP BY PowerGeneration.generation_type
			ORDER BY COUNT(*) DESC LIMIT 1) as Most_Common_Method,
		-- Remaining
        COALESCE(ROUND(AVG(CASE WHEN PowerGeneration.monthly_power_generated IS NOT NULL THEN PowerGeneration.monthly_power_generated END)), 0) AS avg_monthly_power_generated,
		COALESCE(SUM(CASE WHEN PowerGeneration.battery_storage_capacity IS NOT NULL THEN 1 ELSE 0 END), 0) AS battery_storage_count
    FROM Household 
    JOIN Address ON Household.postal_code = Address.postal_code
    LEFT JOIN PublicUtility ON Household.email = PublicUtility.email
    LEFT JOIN Heating  ON Household.email = Heating.email
    LEFT JOIN Cooling ON Household.email = Cooling.email
    LEFT JOIN PowerGeneration ON Household.email = PowerGeneration.email
    WHERE Address.postal_code IN (
        SELECT postal_code 
FROM Address 
WHERE postal_code <> @center_postal_code 
    AND (3958.75 * 2 * ATAN2(
        SQRT(
            SIN(RADIANS(latitude - (SELECT latitude FROM Address WHERE postal_code = @center_postal_code))) * SIN(RADIANS(latitude - (SELECT latitude FROM Address WHERE postal_code = @center_postal_code)))
            + COS(RADIANS(latitude)) * COS(RADIANS((SELECT latitude FROM Address WHERE postal_code = @center_postal_code))) * SIN(RADIANS(longitude - (SELECT longitude FROM Address WHERE postal_code = @center_postal_code))) * SIN(RADIANS(longitude - (SELECT longitude FROM Address WHERE postal_code = @center_postal_code)))
        ),
        SQRT(
            1 - SIN(RADIANS(latitude - (SELECT latitude FROM Address WHERE postal_code = @center_postal_code))) * SIN(RADIANS(latitude - (SELECT latitude FROM Address WHERE postal_code = @center_postal_code)))
            - COS(RADIANS(latitude)) * COS(RADIANS((SELECT latitude FROM Address WHERE postal_code = @center_postal_code))) * SIN(RADIANS(longitude - (SELECT longitude FROM Address WHERE postal_code = @center_postal_code))) * SIN(RADIANS(longitude - (SELECT longitude FROM Address WHERE postal_code = @center_postal_code)))
        )
    )) <= @search_radius

    )
    
    GROUP BY Household.household_types;

