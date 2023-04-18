import tkinter as tk
from main_page import MainPage
from household_info_page import HouseholdInfo
from add_appliance_page import AddAppliance
from appliance_list_page import ApplianceList
from add_power_generation_page import AddPowerGeneration
from power_generation_list_page import PowerGenerationList
from submission_complete_page import SubmissionComplete
from view_reports_page import ViewReports
from report_1 import Report1
from report_2 import Report2
from report_3 import Report3
from report_4 import Report4
from report_5 import Report5
from report_6 import Report6
from db_and_sql_handler import (
    execute_sql_script_file, drop_and_create_database, 
    check_and_remove_shared_data_json,
    USE_DATABASE_SQL, CONN,
)


class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.shared_data = []  # Initialize shared_data
         
        # creating a container
        container = tk.Frame(self) 
        self.title("Alternakraft")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
  
        # initializing frames to an empty array
        self.frames = {}

        # list of pages
        self.page_lists = [MainPage, HouseholdInfo, AddAppliance, ApplianceList, 
                           AddPowerGeneration, PowerGenerationList, SubmissionComplete, ViewReports, 
                           Report1, Report2, Report3, Report4, Report5, Report6] 
  
        # iterating through page lists
        for page in self.page_lists:
            frame = page(container, self)
  
            # initialize frame of object from page lists
            self.frames[page] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
        self.show_frame(MainPage)
  
    # to display the current frame passed as parameter
    def show_frame(self, cont):
        if isinstance(cont, str):
            frame_class = next((page for page in self.page_lists if page.__name__ == cont), None)
            if frame_class is None:
                raise ValueError(f"Frame class with name '{cont}' not found")
            frame = self.frames[frame_class]
        else:
            frame = self.frames[cont]

        frame.tkraise()
        if hasattr(frame, "refresh"):
            frame.refresh()  # Call the refresh method if it exists
    
    #To share data among frames
    def store_data(self, data):
        if data not in self.shared_data:
            self.shared_data.append(data)
    
    def get_data(self):
        return self.shared_data
    
    def remove_data(self, data):
        if data in self.shared_data:
            self.shared_data.remove(data)
    
    def clear_inputs(self, frame_name):
        frame = self.frames[next((page for page in self.page_lists if page.__name__ == frame_name), None)]
        if frame is not None:
            frame.clear_inputs()
        else:
            raise ValueError(f"Frame class with name '{frame_name}' not found")

# delete shared_data.json file
def delete_shared_data_json():
    check_and_remove_shared_data_json()
    app.destroy()

##### Driver Code #####
drop_and_create_database(CONN)
cursor = CONN.cursor()
cursor.execute(USE_DATABASE_SQL)

# # execute create_table_schema.sql file to create tables
# execute_sql_script_file(cursor, 'sql_files/create_table_schema.sql')
#
# # execute insert_data.sql file to insert example data
# execute_sql_script_file(cursor, 'sql_files/insert_data.sql')

# execute create_table_schema_demo.sql file to create tables for demo
execute_sql_script_file(cursor, 'sql_files/create_table_schema_demo.sql')

# execute insert_address_data_demo.sql file to create tables for demo
execute_sql_script_file(cursor, 'sql_files/insert_address_data_demo.sql')

# execute insert_household_data_demo.sql file to create tables for demo
execute_sql_script_file(cursor, 'sql_files/insert_household_data_demo.sql')

# execute insert_heating_data_demo.sql file to create tables for demo
execute_sql_script_file(cursor, 'sql_files/insert_heating_data_demo.sql')

# execute insert_cooling_data_demo.sql file to create tables for demo
execute_sql_script_file(cursor, 'sql_files/insert_cooling_data_demo.sql')

# execute insert_public_utility_data_demo.sql file to create tables for demo
execute_sql_script_file(cursor, 'sql_files/insert_public_utility_data_demo.sql')

# execute insert_power_generation_data_demo.sql file to create tables for demo
execute_sql_script_file(cursor, 'sql_files/insert_power_generation_data_demo.sql')

# execute insert_manufacturer_data_demo.sql file to create tables for demo
execute_sql_script_file(cursor, 'sql_files/insert_manufacturer_data_demo.sql')

# execute insert_appliance_data_demo.sql file to create tables for demo
execute_sql_script_file(cursor, 'sql_files/insert_appliance_data_demo.sql')

# execute insert_heater_data_demo.sql file to create tables for demo
execute_sql_script_file(cursor, 'sql_files/insert_heater_data_demo.sql')

# execute insert_air_conditioner_data_demo.sql file to create tables for demo
execute_sql_script_file(cursor, 'sql_files/insert_air_conditioner_data_demo.sql')

# execute insert_water_heater_data_demo.sql file to create tables for demo
execute_sql_script_file(cursor, 'sql_files/insert_water_heater_data_demo.sql')

# execute insert_water_heater_data_demo.sql file to create tables for demo
execute_sql_script_file(cursor, 'sql_files/insert_heat_pump_data_demo.sql')


# when change in db tables are made, must commit the change
CONN.commit()

app = tkinterApp()
#protocol to delete shared_data.json file when exits window
app.protocol("WM_DELETE_WINDOW", delete_shared_data_json)
app.mainloop()