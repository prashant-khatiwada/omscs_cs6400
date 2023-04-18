import tkinter as tk
from household_info_page import HouseholdInfo
from view_reports_page import ViewReports
from db_and_sql_handler import check_and_remove_shared_data_json

# main page window frame
class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # remove shared data json file if it exists
        check_and_remove_shared_data_json()
        
        # label of main page framework
        label_title = tk.Label(self, text="Welcome to Alternakraft!", font=("Verdana", 40))
         
        # page title position
        label_title.place(relx=0.5, rely=0.2, anchor="center")

        # label of description
        label_description = tk.Label(self, text="Please choose what you'd like to do:", font=("Verdana", 20))

        # description position
        label_description.place(relx=0.5, rely=0.4, anchor='center')
        
        # button that navigates to household information page
        button_to_household = tk.Button(self, text="Enter my houshold info", command=lambda : controller.show_frame(HouseholdInfo))
     
        # button to household position
        button_to_household.place(relx=0.5, rely=0.6, anchor="center")

        # button that navigates to view reports page
        button_to_reports = tk.Button(self, text="View reports/query data", command=lambda : controller.show_frame(ViewReports))
     
        # button to reports position
        button_to_reports.place(relx=0.5, rely=0.7, anchor="center")

        ########################################################################
        from add_appliance_page import AddAppliance
        from appliance_list_page import ApplianceList
        # button that navigates to household information page
        button_to_appliance_TEMP = tk.Button(self, text="appliance_TEMP", command=lambda : controller.show_frame(AddAppliance))
        # button to household position
        button_to_appliance_TEMP.place(relx=0.5, rely=0.8, anchor="center")

        # button that navigates to household information page
        button_to_appliance_list_TEMP = tk.Button(self, text="appliance_list_TEMP", command=lambda : controller.show_frame(ApplianceList))
        # button to household position
        button_to_appliance_list_TEMP.place(relx=0.5, rely=0.9, anchor="center")
        ########################################################################
        

# third window frame add appliance
class SubmissionComplete(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Submission complete!", font=("Verdana", 25))
        label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        next_button = tk.Button(self, text="Return to the main menu", command=lambda: controller.show_frame(MainPage))
        next_button.grid(row=1, column=0, padx=10, pady=10)