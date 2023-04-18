import tkinter as tk
from tkinter import *
from tkinter import messagebox
from add_appliance_page import AddAppliance
from db_and_sql_handler import (
    USE_DATABASE_SQL, DROP_DATABASE_SQL,
    CREATE_DATABASE_SQL, CONN,
    create_or_add_shared_data_json)

ERROR_MESSAGE_TITLE = "Household Info Error"
EMAIL_EMPTY_INPUT_ERROR_MESSAGE = "Please provide an email address!"
EMAIL_EXISTS_ERROR_MESSAGE = "Email already exists!"
POSTAL_CODE_EMPTY_INPUT_ERROR_MESSAGE = "Please provide postal code!"
POSTAL_CODE_NOT_EXISTS_ERROR_MESSAGE = "Postal code does not exist!"
SQUARE_FOOTAGE_ERROR_MESSAGE = "Square footage must be greater than 0!"
SQUARE_FOOTAGE_TYPE_ERROR_MESSAGE = "Squre footage must be a whole number"

cursor = CONN.cursor()
cursor.execute(DROP_DATABASE_SQL)
cursor.execute(CREATE_DATABASE_SQL)
cursor.execute(USE_DATABASE_SQL)


def household_info_execute_command(controller, params):
    # get input values
    input_email = params["input_email"].get()
    input_postal = params["input_postal"].get()
    input_home_type = params["input_home_type"].get()
    input_square_footage = params["input_square_footage"].get()

    input_heating = params["input_heating"].get()
    checkbox_heating = params["checkbox_heating"].get()

    input_cooling = params["input_cooling"].get()
    checkbox_cooling = params["checkbox_cooling"].get()

    checkbox_electric = params["checkbox_electric"].get()
    checkbox_gas = params["checkbox_gas"].get()
    checkbox_steam = params["checkbox_steam"].get()
    checkbox_fuel_oil = params["checkbox_fuel_oil"].get()

    # validate email
    if input_email == "":
        messagebox.showerror(ERROR_MESSAGE_TITLE, EMAIL_EMPTY_INPUT_ERROR_MESSAGE)
        return False
    cursor.execute("SELECT email FROM Household WHERE email=%s",(input_email,))
    query_result = cursor.fetchall()
    if len(query_result) > 0:
        messagebox.showerror(ERROR_MESSAGE_TITLE, EMAIL_EXISTS_ERROR_MESSAGE)
        return False
    
    # validate postal code
    if input_postal == "":
        messagebox.showerror(ERROR_MESSAGE_TITLE, POSTAL_CODE_EMPTY_INPUT_ERROR_MESSAGE)
        return False
    cursor.execute("SELECT postal_code FROM Address WHERE postal_code=%s",(input_postal,))
    query_result = cursor.fetchall()
    if len(query_result) < 1:
        messagebox.showerror(ERROR_MESSAGE_TITLE, POSTAL_CODE_NOT_EXISTS_ERROR_MESSAGE)
        return False
    
    # validate square footage
    try:
        square_footage_cast = int(input_square_footage)
    except ValueError:
        messagebox.showerror(ERROR_MESSAGE_TITLE, SQUARE_FOOTAGE_TYPE_ERROR_MESSAGE)
    if square_footage_cast == 0:
        messagebox.showerror(ERROR_MESSAGE_TITLE, SQUARE_FOOTAGE_ERROR_MESSAGE)
        return False

    # execute insertion to Household table
    cursor.execute(
        "INSERT INTO Household (email, square_footage, household_types, postal_code) \
            VALUES (%s,%s,%s,%s)",(input_email, square_footage_cast, input_home_type, input_postal)
    )

    # execute insertion to Heating table if checkbox_heating is offvalue
    if checkbox_heating == 0:
        cursor.execute("INSERT INTO Heating (email, temperature) VALUES (%s,%s)",(input_email, input_heating))
    else:
        cursor.execute("INSERT INTO Heating (email, temperature) VALUES (%s,NULL)",(input_email,))

    # execute insertion to Cooling table if checkbox_cooling is offvalue
    if checkbox_cooling == 0:
        cursor.execute("INSERT INTO Cooling (email, temperature) VALUES (%s,%s)",(input_email, input_cooling))
    else:
        cursor.execute("INSERT INTO Cooling (email, temperature) VALUES (%s,NULL)",(input_email,))
    
    # execute insertion to PublicUtility table if checkbox_electric is onvalue
    if checkbox_electric == 1:
        cursor.execute("INSERT INTO PublicUtility (email, public_utility) VALUES (%s,'Electric')",(input_email,))

    # execute insertion to PublicUtility table if checkbox_gas is onvalue
    if checkbox_gas == 1:
        cursor.execute("INSERT INTO PublicUtility (email, public_utility) VALUES (%s,'Gas')",(input_email,))

    # execute insertion to PublicUtility table if checkbox_steam is onvalue
    if checkbox_steam == 1:
        cursor.execute("INSERT INTO PublicUtility (email, public_utility) VALUES (%s,'Steam')",(input_email,))

    # execute insertion to PublicUtility table if checkbox_fuel_oil is onvalue
    if checkbox_fuel_oil == 1:
        cursor.execute("INSERT INTO PublicUtility (email, public_utility) VALUES (%s,'Fuel oil')",(input_email,))

    # commit updates
    CONN.commit()

    # create json file and store email to share it among other frames
    data = {
        "input_email": input_email
    }
    create_or_add_shared_data_json(data)

    controller.show_frame(AddAppliance)


# household information page window frame
class HouseholdInfo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        # label of household info page framework
        label_household = tk.Label(self, text="Enter household info", font=("Verdana", 25))
        label_household.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        # label of email address
        label_email = tk.Label(self, text="Please enter your email address:", font=("Verdana", 15))
        label_email.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        # entry field of email address
        self.input_email = tk.Entry(self, textvariable=tk.StringVar())
        self.input_email.grid(row=1, column=1, padx=10, pady=10, sticky="W")

        # label of postal code
        label_postal = tk.Label(self, text="Please enter your five digit postal code:", font=("Verdana", 15))
        label_postal.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        # entry field of postal code
        self.input_postal = tk.Entry(self, textvariable=tk.StringVar())
        self.input_postal.grid(row=2, column=1, padx=10, pady=10, sticky="W")

        # label of household details
        label_household_details = tk.Label(self, text="Please enter the following details for your hosehold.", font=("Verdana", 15))
        label_household_details.grid(row=3, column=0, padx=10, pady=10, sticky="W")

        # label of home type
        label_home_type = tk.Label(self, text="Home type:", font=("Verdana", 15))
        label_home_type.grid(row=4, column=0, padx=10, pady=10, sticky="W")

        # home type dropdown
        self.home_type_lists = [
            "House",
            "Apartment",
            "TownHome",
            "Condominium",
            "MobileHome"
        ]

        # dropdown field of home type
        self.home_data_type = tk.StringVar()
        self.home_data_type.set(self.home_type_lists[0])
        input_home_type = tk.OptionMenu(self, self.home_data_type, *self.home_type_lists)
        input_home_type.grid(row=4, column=1, padx=10, pady=10, sticky="W")

        # label of square footage
        label_square_footage = tk.Label(self, text="Square footage:", font=("Verdana", 15))
        label_square_footage.grid(row=5, column=0, padx=10, pady=10, sticky="W")

        # entry field of square footage
        self.input_square_footage = tk.Entry(self, textvariable=tk.IntVar())
        self.input_square_footage.grid(row=5, column=1, padx=10, pady=10, sticky="W")

        # label of thermostat heating
        label_heating = tk.Label(self, text="Thermostat setting for heating:", font=("Verdana", 15))
        label_heating.grid(row=6, column=0, padx=10, pady=10, sticky="W")

        # enntry field of thermostat heating
        self.input_heating = tk.Entry(self, textvariable=tk.IntVar())
        self.input_heating.grid(row=6, column=1, padx=10, pady=10, sticky="W")

        # No heat checkbox
        self.heating_data_type = tk.IntVar()
        checkbox_heating = tk.Checkbutton(self, text='No heat', variable=self.heating_data_type, onvalue=1, offvalue=0)
        checkbox_heating.grid(row=6, column=2, padx=10, pady=10, sticky="W")

        # label of thermostat cooling
        label_cooling = tk.Label(self, text="Thermostat setting for cooling:", font=("Verdana", 15))
        label_cooling.grid(row=7, column=0, padx=10, pady=10, sticky="W")

        # enntry field of thermostat cooling
        self.input_cooling = tk.Entry(self, textvariable=tk.IntVar())
        self.input_cooling.grid(row=7, column=1, padx=10, pady=10, sticky="W")

        # No cooling checkbox
        self.cooling_data_type = tk.IntVar()
        checkbox_cooling = tk.Checkbutton(self, text='No cooling', variable=self.cooling_data_type, onvalue=1, offvalue=0)
        checkbox_cooling.grid(row=7, column=2, padx=10, pady=10, sticky="W")

        # label of public utilities
        label_public_utilities = tk.Label(self, text="Public utilities:\n(if none, leave unchecked)", font=("Verdana", 15))
        label_public_utilities.grid(row=8, column=0, padx=10, pady=10, sticky="W")
        
        # create listbox of public utilities
        list_box = tk.Listbox(self)
        list_box.grid(row=8, column=1, padx=10, pady=10)

        # electric checkbox
        self.electric_data_type = tk.IntVar()
        checkbox_electric = tk.Checkbutton(list_box, text="Electric", variable=self.electric_data_type, onvalue=1, offvalue=0)
        checkbox_electric.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        # gas checkbox
        self.gas_data_type = tk.IntVar()
        checkbox_gas = tk.Checkbutton(list_box, text="Gas", variable=self.gas_data_type, onvalue=1, offvalue=0)
        checkbox_gas.grid(row=0, column=1, padx=10, pady=10, sticky="W")

        # steam checkbox
        self.steam_data_type = tk.IntVar()
        checkbox_steam = tk.Checkbutton(list_box, text="Steam", variable=self.steam_data_type, onvalue=1, offvalue=0)
        checkbox_steam.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        # Fuel oil checkbox
        self.fuel_oil_data_type = tk.IntVar()
        checkbox_fuel_oil = tk.Checkbutton(list_box, text="Fuel oil", variable=self.fuel_oil_data_type, onvalue=1, offvalue=0)
        checkbox_fuel_oil.grid(row=1, column=1, padx=10, pady=10, sticky="W")

        # get all the input parameters
        self.params = {
            "input_email": self.input_email, "input_postal": self.input_postal,
            "input_home_type": self.home_data_type, "input_square_footage": self.input_square_footage,
            "input_heating": self.input_heating, "checkbox_heating": self.heating_data_type,
            "input_cooling": self.input_cooling, "checkbox_cooling": self.cooling_data_type,
            "checkbox_electric": self.electric_data_type, "checkbox_gas": self.gas_data_type,
            "checkbox_steam": self.steam_data_type, "checkbox_fuel_oil": self.fuel_oil_data_type
        }

        # next button to execute insertion and navigate to add appliance page
        next_button = tk.Button(self, text="Next", command=lambda: household_info_execute_command(self.controller, self.params))
        next_button.grid(row=8, column=2, padx=10, pady=10)

    # def clear_input_data(self):
    #     self.input_email.delete(first=0, last=250)
    #     self.input_postal.delete(first=0, last=250)
    #     self.home_data_type.set(self.home_type_lists[0])
    #     self.input_square_footage.delete(first=0, last=250)
    #     self.heating_data_type.set(0)
    #     self.input_cooling.delete(first=0, last=250)
    #     self.cooling_data_type.set(0)
    #     self.electric_data_type.set(0)
    #     self.gas_data_type.set(0)
    #     self.steam_data_type.set(0)
    #     self.fuel_oil_data_type.set(0)