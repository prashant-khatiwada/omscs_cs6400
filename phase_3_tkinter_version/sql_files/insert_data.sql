-- Insert into Address
INSERT INTO Address (postal_code, latitude, longitude, city, state) VALUES (30303, 33.7529, -84.3903, 'Atlanta', 'GA');
INSERT INTO Address (postal_code, latitude, longitude, city, state) VALUES (30310, 33.7363, -84.4278, 'Atlanta', 'GA');
INSERT INTO Address (postal_code, latitude, longitude, city, state) VALUES (10001, 40.7506, -73.9973, 'New York', 'NY');
INSERT INTO Address (postal_code, latitude, longitude, city, state) VALUES (90210, 34.1030, -118.4108, 'Beverly Hills', 'CA');
INSERT INTO Address (postal_code, latitude, longitude, city, state) VALUES (60602, 41.8836, -87.6226, 'Chicago', 'IL');
INSERT INTO Address (postal_code, latitude, longitude, city, state) VALUES (77002, 29.7599, -95.3667, 'Houston', 'TX');
INSERT INTO Address (postal_code, latitude, longitude, city, state) VALUES (20001, 38.9085, -77.0177, 'Washington', 'DC');
INSERT INTO Address (postal_code, latitude, longitude, city, state) VALUES (02108, 42.3584, -71.0598, 'Boston', 'MA');
INSERT INTO Address (postal_code, latitude, longitude, city, state) VALUES (94102, 37.7793, -122.4193, 'San Francisco', 'CA');
INSERT INTO Address (postal_code, latitude, longitude, city, state) VALUES (75201, 32.7876, -96.7994, 'Dallas', 'TX');
INSERT INTO Address (postal_code, latitude, longitude, city, state) VALUES (33131, 25.7627, -80.1918, 'Miami', 'FL');
INSERT INTO Address (postal_code, latitude, longitude, city, state) VALUES (19107, 39.9517, -75.1573, 'Philadelphia', 'PA');
INSERT INTO Address (postal_code, latitude, longitude, city, state) VALUES (98101, 47.6101, -122.3332, 'Seattle', 'WA');
INSERT INTO Address (postal_code, latitude, longitude, city, state) VALUES (80202, 39.7489, -104.9966, 'Denver', 'CO');
INSERT INTO Address (postal_code, latitude, longitude, city, state) VALUES (92101, 32.7195, -117.1653, 'San Diego', 'CA');
INSERT INTO Address (postal_code, latitude, longitude, city, state) VALUES (97205, 45.5202, -122.6870, 'Portland', 'OR');
INSERT INTO Address (postal_code, latitude, longitude, city, state) VALUES (89101, 36.1749, -115.1372, 'Las Vegas', 'NV');
INSERT INTO Address (postal_code, latitude, longitude, city, state) VALUES (43215, 39.9612, -82.9988, 'Columbus', 'OH');
INSERT INTO Address (postal_code, latitude, longitude, city, state) VALUES (90012, 34.0550, -118.2405, 'Los Angeles', 'CA');
INSERT INTO Address (postal_code, latitude, longitude, city, state) VALUES (53202, 43.0446, -87.9163, 'Milwaukee', 'WI');
INSERT INTO Address (postal_code, latitude, longitude, city, state) VALUES (36879, 33.702657, -84.439127, 'Atlanta', 'GA');
INSERT INTO Address (postal_code, latitude, longitude, city, state) VALUES (30334, 32.733511, -85.55322, 'Waverly', 'AL');
INSERT INTO Address (postal_code, latitude, longitude, city, state) VALUES (92232, 33.026203, -115.28458, 'Calexico', 'CA');
INSERT INTO Address (postal_code, latitude, longitude, city, state) VALUES (89317, 38.835421, -115.02628, 'Lund', 'NV');
INSERT INTO Address (postal_code, latitude, longitude, city, state) VALUES (82718, 43.939968, -105.52445, 'Gillette', 'WY');
INSERT INTO Address (postal_code, latitude, longitude, city, state) VALUES (81624, 39.220166, -107.93414, 'Collbran', 'CO');
INSERT INTO Address (postal_code, latitude, longitude, city, state) VALUES (97304, 44.970181, -123.08033, 'Salem', 'OR');

-- Insert into Household
INSERT INTO Household (email, square_footage, household_types, postal_code)VALUES ('johndoe@gmail.com', 2000, 'Single-Family', 10001);
INSERT INTO Household (email, square_footage, household_types, postal_code)VALUES ('janedoe@yahoo.com', 1500, 'Apartment', 90210);
INSERT INTO Household (email, square_footage, household_types, postal_code)VALUES ('brianjones@gmail.com', 1800, 'Condo', 60602);
INSERT INTO Household (email, square_footage, household_types, postal_code)VALUES ('sarahsmith@gmail.com', 2500, 'Single-Family', 77002);
INSERT INTO Household (email, square_footage, household_types, postal_code)VALUES ('davidwilson@gmail.com', 1000, 'Apartment', 20001);
INSERT INTO Household (email, square_footage, household_types, postal_code)VALUES ('elizabethbrown@yahoo.com', 1200, 'Apartment', 02108);
INSERT INTO Household (email, square_footage, household_types, postal_code)VALUES ('robertmiller@gmail.com', 3000, 'Single-Family', 94102);
INSERT INTO Household (email, square_footage, household_types, postal_code)VALUES ('carolynlee@yahoo.com', 2200, 'Condo', 75201);
INSERT INTO Household (email, square_footage, household_types, postal_code)VALUES ('peterwang@gmail.com', 2000, 'Single-Family', 33131);
INSERT INTO Household (email, square_footage, household_types, postal_code)VALUES ('melissajohnson@yahoo.com', 1800, 'Apartment', 19107);
INSERT INTO Household (email, square_footage, household_types, postal_code)VALUES ('jenniferbrown@gmail.com', 1500, 'Apartment', 98101);
INSERT INTO Household (email, square_footage, household_types, postal_code)VALUES ('adamjones@yahoo.com', 2100, 'Condo', 30303);
INSERT INTO Household (email, square_footage, household_types, postal_code)VALUES ('monicalee@gmail.com', 2200, 'Single-Family', 80202);
INSERT INTO Household (email, square_footage, household_types, postal_code)VALUES ('stevewilson@yahoo.com', 1800, 'Condo', 92101);
INSERT INTO Household (email, square_footage, household_types, postal_code)VALUES ('jessicamiller@gmail.com', 2500, 'Single-Family', 97205);

-- Insert PowerGeneration 
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity)VALUES ('johndoe@gmail.com', 'Solar', 1000, 500);
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity)VALUES ('janedoe@yahoo.com', 'Wind', 500, NULL);
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity)VALUES ('brianjones@gmail.com', 'Solar', 800, 250);
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity)VALUES ('sarahsmith@gmail.com', 'Solar', 1200, 750);
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity)VALUES ('davidwilson@gmail.com', 'Wind', 600, NULL);
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity)VALUES ('elizabethbrown@yahoo.com', 'Solar', 700, 150);
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity)VALUES ('robertmiller@gmail.com', 'Wind', 800, NULL);
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity)VALUES ('carolynlee@yahoo.com', 'Solar', 900, 400);
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity)VALUES ('peterwang@gmail.com', 'Solar', 1500, 1000);
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity)VALUES ('melissajohnson@yahoo.com', 'Wind', 700, NULL);
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity)VALUES ('jenniferbrown@gmail.com', 'Solar', 800, 200);
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity)VALUES ('adamjones@yahoo.com', 'Wind', 900, NULL);
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity)VALUES ('monicalee@gmail.com', 'Solar', 1100, 300);
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity)VALUES ('stevewilson@yahoo.com', 'Solar', 1000, 500);
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity)VALUES ('jessicamiller@gmail.com', 'Wind', 1000, NULL);

-- Heating
INSERT INTO Heating (email, temperature) VALUES ('johndoe@gmail.com', 75);
INSERT INTO Heating (email, temperature) VALUES ('janedoe@yahoo.com', 78);
INSERT INTO Heating (email, temperature) VALUES ('brianjones@gmail.com', 80);
INSERT INTO Heating (email, temperature) VALUES ('sarahsmith@gmail.com', 82);
INSERT INTO Heating (email, temperature) VALUES ('davidwilson@gmail.com', 70);
INSERT INTO Heating (email, temperature) VALUES ('elizabethbrown@yahoo.com', 82);
INSERT INTO Heating (email, temperature) VALUES ('robertmiller@gmail.com', 78);
INSERT INTO Heating (email, temperature) VALUES ('carolynlee@yahoo.com', 80);
INSERT INTO Heating (email, temperature) VALUES ('peterwang@gmail.com', 82);
INSERT INTO Heating (email, temperature) VALUES ('melissajohnson@yahoo.com', 74);
INSERT INTO Heating (email, temperature) VALUES ('jenniferbrown@gmail.com', 78);
INSERT INTO Heating (email, temperature) VALUES ('adamjones@yahoo.com', 80);
INSERT INTO Heating (email, temperature) VALUES ('monicalee@gmail.com', 80);
INSERT INTO Heating (email, temperature) VALUES ('stevewilson@yahoo.com', 82);
INSERT INTO Heating (email, temperature) VALUES ('jessicamiller@gmail.com', 85);

-- Cooling
INSERT INTO Cooling (email, temperature) VALUES ('johndoe@gmail.com', 65);
INSERT INTO Cooling (email, temperature) VALUES ('janedoe@yahoo.com', 68);
INSERT INTO Cooling (email, temperature) VALUES ('brianjones@gmail.com', 70);
INSERT INTO Cooling (email, temperature) VALUES ('sarahsmith@gmail.com', 72);
INSERT INTO Cooling (email, temperature) VALUES ('davidwilson@gmail.com', 60);
INSERT INTO Cooling (email, temperature) VALUES ('elizabethbrown@yahoo.com', 62);
INSERT INTO Cooling (email, temperature) VALUES ('robertmiller@gmail.com', 68);
INSERT INTO Cooling (email, temperature) VALUES ('carolynlee@yahoo.com', 70);
INSERT INTO Cooling (email, temperature) VALUES ('peterwang@gmail.com', 72);
INSERT INTO Cooling (email, temperature) VALUES ('melissajohnson@yahoo.com', 74);
INSERT INTO Cooling (email, temperature) VALUES ('jenniferbrown@gmail.com', 68);
INSERT INTO Cooling (email, temperature) VALUES ('adamjones@yahoo.com', 70);
INSERT INTO Cooling (email, temperature) VALUES ('monicalee@gmail.com', 60);
INSERT INTO Cooling (email, temperature) VALUES ('stevewilson@yahoo.com', 62);
INSERT INTO Cooling (email, temperature) VALUES ('jessicamiller@gmail.com', 65);


-- PublicUtility
INSERT INTO PublicUtility (email, public_utility) VALUES ('johndoe@gmail.com', 'Electric');
INSERT INTO PublicUtility (email, public_utility) VALUES ('johndoe@gmail.com', 'Gas');
INSERT INTO PublicUtility (email, public_utility) VALUES ('janedoe@yahoo.com', 'Steam');
INSERT INTO PublicUtility (email, public_utility) VALUES ('brianjones@gmail.com', 'Fuel Oil');
INSERT INTO PublicUtility (email, public_utility) VALUES ('sarahsmith@gmail.com', 'Off-The-Grid');
INSERT INTO PublicUtility (email, public_utility) VALUES ('davidwilson@gmail.com', 'Electric');
INSERT INTO PublicUtility (email, public_utility) VALUES ('elizabethbrown@yahoo.com', 'Gas');
INSERT INTO PublicUtility (email, public_utility) VALUES ('robertmiller@gmail.com', 'Off-The-Grid');
INSERT INTO PublicUtility (email, public_utility) VALUES ('carolynlee@yahoo.com', 'Electric');
INSERT INTO PublicUtility (email, public_utility) VALUES ('peterwang@gmail.com', 'Gas');
INSERT INTO PublicUtility (email, public_utility) VALUES ('melissajohnson@yahoo.com', 'Electric');
INSERT INTO PublicUtility (email, public_utility) VALUES ('jenniferbrown@gmail.com', 'Electric');
INSERT INTO PublicUtility (email, public_utility) VALUES ('adamjones@yahoo.com', 'Electric');
INSERT INTO PublicUtility (email, public_utility) VALUES ('monicalee@gmail.com', 'Off-The-Grid');
INSERT INTO PublicUtility (email, public_utility) VALUES ('stevewilson@yahoo.com', 'Fuel Oil');
INSERT INTO PublicUtility (email, public_utility) VALUES ('jessicamiller@gmail.com', 'Fuel Oil');

-- PowerGeneration
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity) VALUES ('johndoe@gmail.com', 'Solar', 1000, 500);
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity) VALUES ('janedoe@yahoo.com', 'Wind', 1500, 1000);
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity) VALUES ('brianjones@gmail.com', 'Solar', 2000, NULL);
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity) VALUES ('sarahsmith@gmail.com', 'Solar', 3000, 750);
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity) VALUES ('davidwilson@gmail.com', 'Wind', 1200, 500);
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity) VALUES ('elizabethbrown@yahoo.com', 'Wind', 2500, NULL);
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity) VALUES ('robertmiller@gmail.com', 'Solar', 4000, 1000);
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity) VALUES ('carolynlee@yahoo.com', 'Wind', 1800, 500);
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity) VALUES ('peterwang@gmail.com', 'Solar', 3000, NULL);
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity) VALUES ('melissajohnson@yahoo.com', 'Solar', 2200, 750);
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity) VALUES ('jenniferbrown@gmail.com', 'Wind', 1200, 500);
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity) VALUES ('adamjones@yahoo.com', 'Solar', 2800, NULL);
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity) VALUES ('monicalee@gmail.com', 'Solar', 3500, 1000);
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity) VALUES ('stevewilson@yahoo.com', 'Wind', 2000, 750);
INSERT INTO PowerGeneration (email, generation_type, monthly_power_generated, battery_storage_capacity) VALUES ('jessicamiller@gmail.com', 'Wind', 4000, NULL);

-- Manufacture
INSERT INTO Manufacturer (manufacturer_name) VALUES ('GE');
INSERT INTO Manufacturer (manufacturer_name) VALUES ('Whirlpool');
INSERT INTO Manufacturer (manufacturer_name) VALUES ('LG');
INSERT INTO Manufacturer (manufacturer_name) VALUES ('Samsung');
INSERT INTO Manufacturer (manufacturer_name) VALUES ('Electrolux');
INSERT INTO Manufacturer (manufacturer_name) VALUES ('Bosch');
INSERT INTO Manufacturer (manufacturer_name) VALUES ('Maytag');
INSERT INTO Manufacturer (manufacturer_name) VALUES ('Frigidaire');
INSERT INTO Manufacturer (manufacturer_name) VALUES ('KitchenAid');
INSERT INTO Manufacturer (manufacturer_name) VALUES ('Kenmore');


-- Appliances - WaterHeater
INSERT INTO Appliance (email, appliance_type, btu_rating, model_name, manufacturer_name) VALUES ('johndoe@gmail.com', 1, 10000, 'Model A', 'GE');
INSERT INTO Appliance (email, appliance_type, btu_rating, model_name, manufacturer_name)VALUES ('janedoe@yahoo.com', 1, 8000, 'Model C', 'Samsung');
INSERT INTO Appliance (email, appliance_type, btu_rating, model_name, manufacturer_name)VALUES ('brianjones@gmail.com', 1, 4000, 'Model D', 'Samsung');
INSERT INTO Appliance (email, appliance_type, btu_rating, model_name, manufacturer_name)VALUES ('sarahsmith@gmail.com', 1, 12000, 'Model E', 'KitchenAid');
INSERT INTO Appliance (email, appliance_type, btu_rating, model_name, manufacturer_name)VALUES ('davidwilson@gmail.com', 1, 5000, 'Model G', 'Kenmore');
-- Appliances - AirConditioner
INSERT INTO Appliance (email, appliance_type, btu_rating, model_name, manufacturer_name) VALUES ('johndoe@gmail.com', 0, 5000, 'Model B', 'LG');
INSERT INTO Appliance (email, appliance_type, btu_rating, model_name, manufacturer_name)VALUES ('elizabethbrown@yahoo.com', 0, 7000, 'Model H', 'KitchenAid');
INSERT INTO Appliance (email, appliance_type, btu_rating, model_name, manufacturer_name)VALUES ('robertmiller@gmail.com', 0, 6000, 'Model I', 'Kenmore');
INSERT INTO Appliance (email, appliance_type, btu_rating, model_name, manufacturer_name)VALUES ('carolynlee@yahoo.com', 0, 5000, 'Model J', 'Frigidaire');
-- Appliances - Heater
INSERT INTO Appliance (email, appliance_type, btu_rating, model_name, manufacturer_name)VALUES ('peterwang@gmail.com', 0, 11000, 'Model K', 'KitchenAid');
INSERT INTO Appliance (email, appliance_type, btu_rating, model_name, manufacturer_name)VALUES ('melissajohnson@yahoo.com', 0, 4500, 'Model M', 'Kenmore');
INSERT INTO Appliance (email, appliance_type, btu_rating, model_name, manufacturer_name)VALUES ('jenniferbrown@gmail.com', 0, 9000, 'Model N', 'Bosch');
-- Appliances - HeatPump
INSERT INTO Appliance (email, appliance_type, btu_rating, model_name, manufacturer_name)VALUES ('adamjones@yahoo.com', 0, 5500, 'Model O', 'Bosch');
INSERT INTO Appliance (email, appliance_type, btu_rating, model_name, manufacturer_name)VALUES ('sarahsmith@gmail.com', 0, 6000, 'Model F', 'Electrolux');
INSERT INTO Appliance (email, appliance_type, btu_rating, model_name, manufacturer_name) VALUES ('monicalee@gmail.com', 0, 7500, 'Model P', 'LG');
INSERT INTO Appliance (email, appliance_type, btu_rating, model_name, manufacturer_name)VALUES ('peterwang@gmail.com', 0, 8000, 'Model L', 'Frigidaire');



-- Water Heater
INSERT INTO WaterHeater (email, appliance_number, energy_source, temperature, capacity)VALUES ('johndoe@gmail.com', 1, 'Electric', 120, 50.0);
INSERT INTO WaterHeater (email, appliance_number, energy_source, temperature, capacity) VALUES ('janedoe@yahoo.com', 2, 'Gas', 140, 40.0);
INSERT INTO WaterHeater (email, appliance_number, energy_source, temperature, capacity) VALUES ('brianjones@gmail.com', 3, 'Electric', 130, 55.0);
INSERT INTO WaterHeater (email, appliance_number, energy_source, temperature, capacity) VALUES ('sarahsmith@gmail.com', 4, 'Gas', 125, 45.0);
INSERT INTO WaterHeater (email, appliance_number, energy_source, temperature, capacity) VALUES ('davidwilson@gmail.com', 5, 'Electric', 125, 45.0);

-- AirConditioner
INSERT INTO AirConditioner (email, appliance_number, eer) VALUES ('johndoe@gmail.com', 6, 12.5);
INSERT INTO AirConditioner (email, appliance_number, eer) VALUES ('elizabethbrown@yahoo.com', 7, 11.8);
INSERT INTO AirConditioner (email, appliance_number, eer) VALUES ('robertmiller@gmail.com', 8, 11.8);
INSERT INTO AirConditioner (email, appliance_number, eer) VALUES ('carolynlee@yahoo.com', 9, 14.6);

-- Heater
INSERT INTO Heater (email, appliance_number, energy_source) VALUES ('peterwang@gmail.com', 10, 'natural gas');
INSERT INTO Heater (email, appliance_number, energy_source) VALUES ('melissajohnson@yahoo.com', 11, 'propane');
INSERT INTO Heater (email, appliance_number, energy_source) VALUES ('jenniferbrown@gmail.com', 12, 'electric');

-- HeatPump
INSERT INTO HeatPump (email, appliance_number, seer, hsbf) VALUES ('adamjones@yahoo.com', 13, 15.5, 8.2);
INSERT INTO HeatPump (email, appliance_number, seer, hsbf) VALUES ('sarahsmith@gmail.com', 14, 16.2, 7.8);
INSERT INTO HeatPump (email, appliance_number, seer, hsbf) VALUES ('monicalee@gmail.com', 15, 17.8, 8.5);
INSERT INTO HeatPump (email, appliance_number, seer, hsbf) VALUES ('peterwang@gmail.com', 16, 14.9, 9.1);