CREATE TABLE Household (
	email varchar(250) NOT NULL,
	square_footage INT(10) NOT NULL,
	household_types varchar(60) NOT NULL,
    	postal_code INT(5) NOT NULL,
    	PRIMARY KEY(email)
);

CREATE TABLE Address (
	postal_code INT(5) NOT NULL,
	latitude DECIMAL(8,6) NOT NULL,
	longitude DECIMAL(9,6) NOT NULL,
	city varchar(250) NOT NULL,
   	state varchar(2) NOT NULL,
   	PRIMARY KEY(postal_code)
);

-- Changed - No AUTO INCREMENT in power_generation_number
CREATE TABLE PowerGeneration (
	email varchar(250) NOT NULL,
	power_generation_number INT(5) NOT NULL,
	generation_type varchar(60) NOT NULL,
    	monthly_power_generated INT(9) NOT NULL,
    	battery_storage_capacity INT(9) NULL,
    	PRIMARY KEY(email, power_generation_number),
    	KEY (power_generation_number)
);

-- Changed - appliance_type from binary to varchar (20)
-- Changed - No AUTO INCREMENT in appliance_number
CREATE TABLE Appliance (
	email varchar(250) NOT NULL,
	appliance_number INT(9) NOT NULL,
	appliance_type varchar(20) NOT NULL,
	btu_rating INT(9) NOT NULL,
    	model_name varchar(250) NOT NULL,
    	manufacturer_name varchar(250) NOT NULL,
    	PRIMARY KEY(email, appliance_number),
    	KEY (appliance_number)
);

CREATE TABLE Manufacturer (
    	manufacturer_name varchar(250) NOT NULL,
    	PRIMARY KEY(manufacturer_name)
);

-- Changed - since public_utility is a part of PRIMARY KEY
-- all the inserts with '' (empty string) has been changed to 'off-the-grid'
CREATE TABLE PublicUtility (
	email varchar(250) NOT NULL,
    	public_utility varchar(30) NOT NULL,
    	PRIMARY KEY(email, public_utility)
);

CREATE TABLE Heating (
	email varchar(250) NOT NULL,
    	temperature INT(9) NULL,
    	UNIQUE KEY(email, temperature)
);

CREATE TABLE Cooling (
	email varchar(250) NOT NULL,
    	temperature INT(9) NULL,
    	UNIQUE KEY(email, temperature)
);

-- Changed - Some of the temperature values in demo data are NULL
-- Changed temperature value form NOT NULL to NULL
CREATE TABLE WaterHeater (
	email varchar(250) NOT NULL,
	appliance_number INT(9) NOT NULL,
	energy_source varchar(250) NOT NULL,
    	temperature INT(9) NULL,
    	capacity DECIMAL(13,10) NOT NULL,
    	PRIMARY KEY(email, appliance_number)
);

CREATE TABLE AirConditioner (
	email varchar(250) NOT NULL,
	appliance_number INT(9) NOT NULL,
	eer DECIMAL(12,10) NULL,
    	PRIMARY KEY(email, appliance_number)
);

CREATE TABLE Heater (
	email varchar(250) NOT NULL,
	appliance_number INT(9) NOT NULL,
	energy_source varchar(250) NOT NULL,
    	PRIMARY KEY(email, appliance_number)
);

CREATE TABLE HeatPump (
	email varchar(250) NOT NULL,
	appliance_number INT(9) NOT NULL,
	seer DECIMAL(12,10) NOT NULL,
	hspf DECIMAL(12,10) NOT NULL,
    	PRIMARY KEY(email, appliance_number)
);

ALTER TABLE Household
    ADD CONSTRAINT fk_Household_postal_code_Address_postal_code
    FOREIGN KEY (postal_code) REFERENCES Address(postal_code);

ALTER TABLE PowerGeneration
    ADD CONSTRAINT fk_PowerGeneration_email_Household_email
    FOREIGN KEY (email) REFERENCES Household(email);

ALTER TABLE Appliance
    ADD CONSTRAINT fk_Appliance_email_Household_email
    FOREIGN KEY (email) REFERENCES Household(email),
    ADD CONSTRAINT fk_Appliance_manufacturer_name_Manufacturer_manufacturer_name
    FOREIGN KEY (manufacturer_name) REFERENCES Manufacturer(manufacturer_name);

ALTER TABLE PublicUtility
    ADD CONSTRAINT fk_PublicUtility_email_Household_email
    FOREIGN KEY (email) REFERENCES Household(email);

ALTER TABLE Heating
    ADD CONSTRAINT fk_Heating_email_Household_email
    FOREIGN KEY (email) REFERENCES Household(email);

ALTER TABLE Cooling
    ADD CONSTRAINT fk_Cooling_email_Household_email
    FOREIGN KEY (email) REFERENCES Household(email);

ALTER TABLE WaterHeater
    ADD CONSTRAINT fk_WaterHeater_appliance_number_Appliance_appliance_number
    FOREIGN KEY (`email`, appliance_number) REFERENCES Appliance(email, appliance_number);

ALTER TABLE AirConditioner
    ADD CONSTRAINT fk_AirConditioner_appliance_number_Appliance_appliance_number
     FOREIGN KEY (`email`, appliance_number) REFERENCES Appliance(email, appliance_number);

ALTER TABLE Heater
    ADD CONSTRAINT fk_Heater_appliance_number_Appliance_appliance_number
    FOREIGN KEY (`email`, appliance_number) REFERENCES Appliance(email, appliance_number);

ALTER TABLE HeatPump
    ADD CONSTRAINT fk_HeatPump_appliance_number_Appliance_appliance_number
    FOREIGN KEY (`email`, appliance_number) REFERENCES Appliance(email, appliance_number);