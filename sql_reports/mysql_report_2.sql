-- Manufacturer/model search
SET
    @search = 'te'; -- replace with user input
SELECT
    manufacturer_name,
    model_name
FROM
    Appliance
WHERE
    manufacturer_name LIKE @search OR model_name LIKE @search
ORDER BY
    manufacturer_name ASC,
    model_name ASC;
	