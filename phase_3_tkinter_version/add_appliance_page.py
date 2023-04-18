from tkinter import *
import tkinter as tk
from appliance_list_page import ApplianceList
from db_and_sql_handler import USE_DATABASE_SQL, CONN
from db_and_sql_handler import retrieve_shared_data_json


'''
Things to check out::
BUG:: if check box then change appliance type, the box frame does not get destroyed
LISTS:: email passing, appliance_number increment
'''


#shared_data = retrieve_shared_data_json()
cursor = CONN.cursor()
cursor.execute(USE_DATABASE_SQL)

#email = 'johndoe@gmail.com'
appliance_number = 1

def insert_appliance_info(controller, params):
    #get inputs
    appliance_type = params['appliance_type'].get()
    model_name = params['model_name'].get()
    manufacturer_name = params['manufacturer_name'].get()
    btu_rating = params['btu_rating'].get()
    shared_data = retrieve_shared_data_json()
    email = shared_data["input_email"]

    if appliance_type == 'Air handler':
        try:
            eer = params['eer'].get()
        except:
            eer = "Null"
        try:
            seer = params['seer'].get()
        except:
            seer = "Null"
        try:
            hsbf = params['hsbf'].get()
        except:
            hsbf = "Null"
        try:
            energy_source_air = params['energy_source_air'].get()
        except:
            energy_source_air = "Null"

        print("INSERT INTO Appliance (email, appliance_type, btu_rating, model_name, manufacturer_name) VALUES ('%s','%s','%s','%s','%s');",(email, appliance_type, btu_rating, model_name, manufacturer_name))
        print("INSERT INTO AirConditioner (email, appliance_number, eer) VALUES ('%s','%s','%s');",(email, appliance_number, eer)) #Appliance number
        print("INSERT INTO Heater (email, appliance_number, energy_source) VALUES ('%s','%s','%s');",(email, appliance_number, energy_source_air))
        print("INSERT INTO HeatPump (email, appliance_number, seer, hsbf) VALUES ('%s','%s','%s','%s');",(email, appliance_number, seer, hsbf))
        '''
        cursor.execute("INSERT INTO Appliance (email, appliance_type, btu_rating, model_name, manufacturer_name) VALUES ('%s','%s','%s','%s','%s');",(email, appliance_type, btu_rating, model_name, manufacturer_name))
        cursor.execute("INSERT INTO AirConditioner (email, appliance_number, eer) VALUES ('%s','%s','%s');",(email, appliance_number, eer))
        cursor.execute("INSERT INTO Heater (email, appliance_number, energy_source) VALUES ('%s','%s','%s');",(email, appliance_number, energy_source_air))
        cursor.execute("INSERT INTO HeatPump (email, appliance_number, seer, hsbf) VALUES ('%s','%s','%s','%s');",(email, appliance_number, seer, hsbf))
        '''
    else: #Water Heater
        energy_source_water = params['energy_source_water'].get()
        capacity = params['capacity'].get()
        temperature = params['temperature'].get()
        print("INSERT INTO Appliance (email, appliance_type, btu_rating, model_name, manufacturer_name) VALUES ('%s','%s','%s','%s','%s');",(email, appliance_type, btu_rating, model_name, manufacturer_name))
        print("INSERT INTO WaterHeater (email, appliance_number, energy_source, temperature, capacity) VALUES ('%s','%s','%s','%s','%s');",(email, appliance_number, energy_source_water, temperature, capacity))
        '''
        cursor.execute("INSERT INTO Appliance (email, appliance_type, btu_rating, model_name, manufacturer_name) VALUES ('%s','%s','%s','%s','%s');",(email, appliance_type, btu_rating, model_name, manufacturer_name))
        cursor.execute("INSERT INTO WaterHeater (email, appliance_number, energy_source, temperature, capacity) VALUES ('%s','%s','%s','%s','%s');",(email, appliance_number, energy_source_water, temperature, capacity))
        '''

def get_manufacturer_list():
    manufacturer_list = []
    cursor.execute("SELECT * FROM Manufacturer")
    query_result = cursor.fetchall()
    for query in query_result:
        manufacturer_list.append(query[0])
    return manufacturer_list

# add appliance page window frame
class AddAppliance(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        self.dropdown_lists = {
            'appliance_type' : ['Air handler', 'Water heater'],
            'manufacturer' : get_manufacturer_list(),
            'energy_source_appliance' : ['Electric', 'Gas', 'Fuel oil'],
            'energy_source_water_heater' : [ 'Electric', 'Gas', 'Thermosolar', 'Heat pump']
        }
        self.params = {
            'appliance_type': None,
            'manufacturer_name': None,
            'model_name': None,
            'eer': None,
            'energy_source_water': None,
            'energy_source_air': None,
            'capacity': None,
            'btu_rating': None,
            'temperature': None,
            'seer': None,
            'hsbf': None
        }
        
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Add Appliance", font=("Verdana", 25))
        label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        # Labels
        # label of Appliance Type (dropdown)
        label_appliance_type = tk.Label(self, text="Appliance Type:", font=("Verdana", 15))
        label_appliance_type.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        # label of Manufacturer (dropdown)
        label_manufacturer = tk.Label(self, text="Manufacturer:", font=("Verdana", 15))
        label_manufacturer.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        # label of Model Name
        label_model_name = tk.Label(self, text="Model Name:", font=("Verdana", 15))
        label_model_name.grid(row=3, column=0, padx=10, pady=10, sticky="W")

        # water heater labels
        self.label_energy_source_water_heater = tk.Label(self, text="Energy Source:", font=("Verdana", 15))
        self.label_capacity = tk.Label(self, text="Capacity (gallons):", font=("Verdana", 15))
        self.label_BTU = tk.Label(self, text="BTU Rating:", font=("Verdana", 15))
        self.label_temp = tk.Label(self, text="Temperature:", font=("Verdana", 15))
        self.energy_source_water_heater = tk.StringVar()  # Add this line here.
        self.energy_source_water_heater.set(self.dropdown_lists['energy_source_water_heater'][0])
        self.input_energy_source_water_heater = tk.OptionMenu(self, self.energy_source_water_heater, *self.dropdown_lists['energy_source_water_heater'])
        self.input_capacity = tk.Entry(self, textvariable=tk.IntVar())
        self.input_BTU = tk.Entry(self, textvariable=tk.IntVar())
        self.input_temp = tk.Entry(self, textvariable=tk.IntVar())

        # Entry Fields
        # dropdown field of home type
        self.appliance_type = tk.StringVar()
        self.appliance_type.set(self.dropdown_lists['appliance_type'][0])
        input_appliance_type = tk.OptionMenu(self, self.appliance_type, *self.dropdown_lists['appliance_type'], command=self.create_appliance_type)
        input_appliance_type.grid(row=1, column=1, padx=10, pady=10, sticky="W")
        
        # Default first dropdown as appliance type
        #self.get_appliance_type()

        # dropdown field of Manufacturer (dropdown)
        self.manufacturer = tk.StringVar()
        self.manufacturer.set(self.dropdown_lists['manufacturer'][0])
        input_manufacturer = tk.OptionMenu(self, self.manufacturer, *self.dropdown_lists['manufacturer'])
        input_manufacturer.grid(row=2, column=1, padx=10, pady=10, sticky="W")
        
        # entry field of Model Name
        self.input_model_name = tk.Entry(self, textvariable=tk.StringVar())
        #input_model_name.insert(END, '')
        self.input_model_name.grid(row=3, column=1, padx=10, pady=10, sticky="W")
        
        # list box
        self.list_box = tk.Listbox(self)
        self.list_box.grid(row=6, column=0, padx=10, pady=10)

        # air_conditioner checkbox
        self.air_conditioner = tk.IntVar()
        self.checkbox_air_conditioner = tk.Checkbutton(self.list_box, text="Air Conditioner", variable=self.air_conditioner, onvalue=1, offvalue=0, command=lambda: self.configure_air_inputs(self.air_conditioner, "Air Conditioner"))
        self.checkbox_air_conditioner.grid(row=0, column=0, padx=5, pady=5, sticky="W")

        # heater checkbox
        self.heater = tk.IntVar()
        self.checkbox_heater = tk.Checkbutton(self.list_box, text="Heater", variable=self.heater, onvalue=1, offvalue=0, command=lambda: self.configure_air_inputs(self.heater, "Heater"))
        self.checkbox_heater.grid(row=1, column=0, padx=5, pady=5, sticky="W")

        # heat_pump checkbox
        self.heat_pump = tk.IntVar()
        self.checkbox_heat_pump = tk.Checkbutton(self.list_box, text="Heat Pump", variable=self.heat_pump, onvalue=1, offvalue=0, command=lambda: self.configure_air_inputs(self.heat_pump, "Heat Pump"))
        self.checkbox_heat_pump.grid(row=2, column=0, padx=5, pady=5, sticky="W")

        self.label_BTU = tk.Label(self, text="BTU Rating:", font=("Verdana", 15))
        self.label_BTU.grid(row=5, column=0, padx=10, pady=10, sticky="W")
        self.input_BTU = tk.Entry(self, textvariable=tk.IntVar())
        self.input_BTU.grid(row=5, column=1, padx=10, pady=10, sticky="W")
        
        self.params['appliance_type'] = self.appliance_type
        self.params['manufacturer_name'] = self.manufacturer
        self.params['model_name'] = self.input_model_name
        self.params['btu_rating'] = self.input_BTU

        next_button = tk.Button(self, text="Add", command=lambda:  [insert_appliance_info(self.controller, self.params), controller.show_frame(ApplianceList)])
        next_button.grid(row=11, column=0, padx=10, pady=10)

        reset_button = tk.Button(self, text="Reset", command=self.clear_inputs)
        reset_button.grid(row=12, column=0, padx=10, pady=10)            

    def configure_air_inputs(self, input, selection):
        check_status = input.get()
        #print(selection, check_status)
        if selection == "Air Conditioner": #EER
            if check_status == 1:
                self.label_energy_efficiency_ratio = tk.Label(self, text="Energy Efficiency Ratio:", font=("Verdana", 10))
                self.input_energy_efficiency_ratio = tk.Entry(self, textvariable=tk.IntVar())
                self.label_energy_efficiency_ratio.grid(row=7, column=0, padx=5, pady=5, sticky="W")
                self.input_energy_efficiency_ratio.grid(row=7, column=1, padx=5, pady=5, sticky="W")
                self.params['eer'] = self.input_energy_efficiency_ratio
            elif check_status == 0:
                self.label_energy_efficiency_ratio.destroy()
                self.input_energy_efficiency_ratio.destroy()
                self.params['eer'] = None
        elif selection == "Heater":
            if check_status == 1:
                self.label_energy_source_air_handler = tk.Label(self, text="Energy Source:", font=("Verdana", 10))
                self.label_energy_source_air_handler.grid(row=8, column=0, padx=10, pady=10, sticky="W")
                
                self.energy_source_air_handler = tk.StringVar()
                self.energy_source_air_handler.set(self.dropdown_lists['energy_source_appliance'][0])
                self.input_energy_source_air_handler = tk.OptionMenu(self, self.energy_source_air_handler, *self.dropdown_lists['energy_source_appliance'])
                self.input_energy_source_air_handler.grid(row=8, column=1, padx=10, pady=10, sticky="W")
                self.params['energy_source_air'] = self.energy_source_air_handler
                print("energy source updated:::", self.params['energy_source_air'].get())
            elif check_status == 0:
                self.label_energy_source_air_handler.destroy()
                self.input_energy_source_air_handler.destroy()
                self.params['energy_source_air'] = None
        elif selection == "Heat Pump": #SEER & HSPF
            if check_status == 1:
                self.label_seasonal_energy_efficiency_rating = tk.Label(self, text="Seasonal Energy Efficiency Rating:", font=("Verdana", 10))
                self.input_seasonal_energy_efficiency_rating = tk.Entry(self, textvariable=tk.IntVar())
                self.label_heating_seasonal_performance_factor = tk.Label(self, text="Heating Seasonal Performance Factor:", font=("Verdana", 10))
                self.input_heating_seasonal_performance_factor = tk.Entry(self, textvariable=tk.IntVar())
                self.label_seasonal_energy_efficiency_rating.grid(row=9, column=0, padx=5, pady=5, sticky="W")
                self.input_seasonal_energy_efficiency_rating.grid(row=9, column=1, padx=5, pady=5, sticky="W")
                self.label_heating_seasonal_performance_factor.grid(row=10, column=0, padx=5, pady=5, sticky="W")
                self.input_heating_seasonal_performance_factor.grid(row=10, column=1, padx=5, pady=5, sticky="W")
                self.params['seer']=self.input_seasonal_energy_efficiency_rating
                self.params['hsbf']=self.input_heating_seasonal_performance_factor
            elif check_status == 0:
                self.label_seasonal_energy_efficiency_rating.destroy()
                self.input_seasonal_energy_efficiency_rating.destroy()
                self.label_heating_seasonal_performance_factor.destroy()
                self.input_heating_seasonal_performance_factor.destroy()
                self.params['seer']=None
                self.params['hsbf']=None
        
    
    def create_appliance_type(self, selection):
        # destroy water heater
        self.label_energy_source_water_heater.destroy()
        self.label_capacity.destroy()
        self.label_BTU.destroy()
        self.input_energy_source_water_heater.destroy()
        self.input_capacity.destroy()
        self.input_BTU.destroy()
        self.input_temp.destroy()
        self.label_temp.destroy()

        # destroy air handler
        self.list_box.destroy()

        if selection == 'Air handler':
            self.label_BTU = tk.Label(self, text="BTU Rating:", font=("Verdana", 15))
            self.label_BTU.grid(row=5, column=0, padx=10, pady=10, sticky="W")
            self.input_BTU = tk.Entry(self, textvariable=tk.IntVar())
            self.input_BTU.grid(row=5, column=1, padx=10, pady=10, sticky="W")

            # list box
            self.list_box = tk.Listbox(self)
            self.list_box.grid(row=6, column=0, padx=10, pady=10)

            # air_conditioner checkbox
            self.air_conditioner = tk.IntVar()
            self.checkbox_air_conditioner = tk.Checkbutton(self.list_box, text="Air Conditioner", variable=self.air_conditioner, onvalue=1, offvalue=0, command=lambda: self.configure_air_inputs(self.air_conditioner, "Air Conditioner"))
            self.checkbox_air_conditioner.grid(row=0, column=0, padx=5, pady=5, sticky="W")

            # heater checkbox
            self.heater = tk.IntVar()
            self.checkbox_heater = tk.Checkbutton(self.list_box, text="Heater", variable=self.heater, onvalue=1, offvalue=0, command=lambda: self.configure_air_inputs(self.heater, "Heater"))
            self.checkbox_heater.grid(row=1, column=0, padx=5, pady=5, sticky="W")

            # heat_pump checkbox
            self.heat_pump = tk.IntVar()
            self.checkbox_heat_pump = tk.Checkbutton(self.list_box, text="Heat Pump", variable=self.heat_pump, onvalue=1, offvalue=0, command=lambda: self.configure_air_inputs(self.heat_pump, "Heat Pump"))
            self.checkbox_heat_pump.grid(row=2, column=0, padx=5, pady=5, sticky="W")

            # input parameters
            self.params['appliance_type'] = self.appliance_type
            self.params['manufacturer_name'] = self.manufacturer
            self.params['model_name'] = self.input_model_name
            self.params['btu_rating'] = self.input_BTU

            next_button = tk.Button(self, text="Add", command=lambda:  insert_appliance_info(self.controller, self.params))
            next_button.grid(row=11, column=0, padx=10, pady=10)


        elif selection == 'Water heater':
            # water heater labels
            self.label_energy_source_water_heater = tk.Label(self, text="Energy Source:", font=("Verdana", 15))
            self.label_capacity = tk.Label(self, text="Capacity (gallons):", font=("Verdana", 15))
            
            self.label_BTU = tk.Label(self, text="BTU Rating:", font=("Verdana", 15))

            self.label_temp = tk.Label(self, text="Temperature:", font=("Verdana", 15))
            self.energy_source_water_heater = tk.StringVar()
            self.energy_source_water_heater.set(self.dropdown_lists['energy_source_water_heater'][0])
            self.input_energy_source_water_heater = tk.OptionMenu(self, self.energy_source_water_heater, *self.dropdown_lists['energy_source_water_heater'])
            self.input_capacity = tk.Entry(self, textvariable=tk.IntVar())
            self.input_BTU = tk.Entry(self, textvariable=tk.IntVar())
            self.input_temp = tk.Entry(self, textvariable=tk.IntVar())

            # position inputs and labels for water heater
            self.label_energy_source_water_heater.grid(row=4, column=0, padx=10, pady=10, sticky="W")
            self.label_capacity.grid(row=5, column=0, padx=10, pady=10, sticky="W")
            self.label_BTU.grid(row=6, column=0, padx=10, pady=10, sticky="W")
            self.label_temp.grid(row=7, column=0, padx=10, pady=10, sticky="W")

            self.input_energy_source_water_heater.grid(row=4, column=1, padx=10, pady=10, sticky="W")
            self.input_capacity.grid(row=5, column=1, padx=10, pady=10, sticky="W")
            
            self.input_BTU.grid(row=6, column=1, padx=10, pady=10, sticky="W")
            self.input_temp.grid(row=7, column=1, padx=10, pady=10, sticky="W")

            self.params['appliance_type'] = self.appliance_type
            self.params['manufacturer_name'] = self.manufacturer
            self.params['model_name'] = self.input_model_name

            self.params['energy_source_water'] = self.energy_source_water_heater
            self.params['btu_rating'] = self.input_BTU
            self.params['capacity'] = self.input_capacity
            self.params['temperature'] = self.input_temp

            next_button = tk.Button(self, text="Add", command=lambda:  insert_appliance_info(self.controller, self.params))
            next_button.grid(row=11, column=0, padx=10, pady=10)            

    def clear_inputs(self):
        self.appliance_type.set(self.dropdown_lists['appliance_type'][0])
        self.manufacturer.set(self.dropdown_lists['manufacturer'][0])
        self.input_model_name.delete(0, 'end')
        self.input_BTU.delete(0, 'end')
        self.energy_source_water_heater.set(self.dropdown_lists['energy_source_water_heater'][0])
        self.input_capacity.delete(0, 'end')
        self.input_temp.delete(0, 'end')
        self.air_conditioner.set(0)
        self.heater.set(0)
        self.heat_pump.set(0)
        #self.remove_air_inputs()
    
    def destroy_page(self):
        self.destroy()