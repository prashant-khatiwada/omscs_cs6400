import tkinter as tk
from power_generation_list_page import PowerGenerationList
from db_and_sql_handler import USE_DATABASE_SQL, DROP_DATABASE_SQL, CREATE_DATABASE_SQL, CONN

cursor = CONN.cursor()

def insert_power_gen_info(params):
    cursor.execute("SET @max_number := (SELECT COALESCE(MAX(power_generation_number), 0) FROM powergeneration);")
    cursor.execute("""
    INSERT INTO powergeneration (email, power_generation_number, generation_type , monthly_power_generated, battery_storage_capacity)
    VALUES (
      'adamjones@yahoo.com',
      @max_number + 1,
      %s,
      %s,
      %s
    );
""", (params['power_generation_type'], params['monthly_kwh'], params['storage_kwh']))
    CONN.commit()
    cursor.execute("SELECT @max_number + 1;")
    return cursor.fetchone()[0]  # Return the new power_generation_number


# add power generation page window frame
class AddPowerGeneration(tk.Frame):
    def __init__(self, parent, controller):
        self.dropdown_lists = {
            'power_generation_type' : ['Solar-electric', 'Wind'],
        }
        self.params = {
        }
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Add power generation", font=("Verdana", 25))
        label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        label2 = tk.Label(self, text="Please provide power generation details.", font=("Verdana", 15))
        label2.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        #Label of Power Generation Energy Source (dropdown)
        label_power_gen_energy_source = tk.Label(self, text="Type:", font=("Verdana", 15))
        label_power_gen_energy_source.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        ## Label of Monthly KwH (dropdown)
        label_monthly_kwh = tk.Label(self, text="Monthly kWh:", font=("Verdana", 15))
        label_monthly_kwh.grid(row=3, column=0, padx=5, pady=10, sticky="W")

        ## Label of Storage KwH (dropdown)
        label_storage_kwh = tk.Label(self, text="Storage kWh:", font=("Verdana", 15))
        label_storage_kwh.grid(row=4, column=0, padx=5, pady=10, sticky="W")

        # Dropdown field of Power Generation Energy Source
        power_generation_type = tk.StringVar()
        power_generation_type.set(self.dropdown_lists['power_generation_type'][0])
        input_power_generation_type = tk.OptionMenu(self, power_generation_type, *self.dropdown_lists['power_generation_type'])
        input_power_generation_type.grid(row=2, column=1, padx=10, pady=10, sticky="W")

        monthly_kwh = tk.Entry(self, textvariable=tk.IntVar())
        monthly_kwh.grid(row=3, column=1, padx=10, pady=10, sticky="W")

        storage_kwh = tk.Entry(self, textvariable=tk.IntVar())
        storage_kwh.grid(row=4, column=1, padx=10, pady=10, sticky="W")

        # input parameters
        self.params['power_generation_type'] = power_generation_type
        self.params['monthly_kwh'] = monthly_kwh
        self.params['storage_kwh'] = storage_kwh

        skip_button = tk.Button(self, text="Skip", command=lambda: controller.show_frame(PowerGenerationList))
        skip_button.grid(row=2, column=2, padx=10, pady=10)

        add_button = tk.Button(self, text="Add", command=self.save_data)
        add_button.grid(row=3, column=2, padx=10, pady=10)

        next_button = tk.Button(self, text="Next", command=self.save_data_and_show_next_frame)
        next_button.grid(row=5, column=0, padx=10, pady=10)
    
    def clear_inputs(self):
        self.params['power_generation_type'].set(self.dropdown_lists['power_generation_type'][0])
        self.params['monthly_kwh'].delete(0, tk.END)
        self.params['storage_kwh'].delete(0, tk.END)
    
    def save_data(self):
        data = {
            'power_generation_type': self.params['power_generation_type'].get(),
            'monthly_kwh': self.params['monthly_kwh'].get(),
            'storage_kwh': self.params['storage_kwh'].get()
        }
        # Check if the data is not empty
        if all(value for value in data.values()):
            power_generation_number = insert_power_gen_info(data)
            data['power_generation_number'] = power_generation_number
            self.controller.store_data(data)
        else:
            print("Data is not complete.")

    def save_data_and_show_next_frame(self):
        #self.save_data()
        self.controller.frames[PowerGenerationList].refresh()  # Refresh the PowerGenerationList frame
        self.controller.show_frame(PowerGenerationList)
