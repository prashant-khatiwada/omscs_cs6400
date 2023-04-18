
-- Top 25 popular manufacturers
SELECT manufacturer_name, COUNT(*) AS appliances_number FROM Appliance GROUP BY manufacturer_name ORDER BY appliances_number DESC LIMIT 25








-- Dropdown for top 25 manufacturer

SET @manufacturer_name = 'Raperewex Holdings'; -- replace with user input

SELECT appliance_type, COUNT(*) AS appliance_count 
									FROM Appliance
									WHERE manufacturer_name = @manufacturer_name
									GROUP BY appliance_type






