import tkinter as tk
from submission_complete_page import SubmissionComplete
from db_and_sql_handler import USE_DATABASE_SQL, DROP_DATABASE_SQL, CREATE_DATABASE_SQL, CONN
from functools import partial

# power generation list page window frame
class PowerGenerationList(tk.Frame):
    def __init__(self, parent, controller):
        self.params = {
        }
        tk.Frame.__init__(self, parent)
        self.controller = controller
        shared_data = self.controller.get_data()
        print(shared_data)
        
        self.initialize_widgets()

        # Process shared_data and display it in the frame
        self.show_power_generation_list(shared_data)
    
    def initialize_widgets(self):
        label = tk.Label(self, text="Power generation", font=("Verdana", 25))
        label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        label2 = tk.Label(self, text="You have added these to your household:", font=("Verdana", 15))
        label2.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        self.next_button = tk.Button(self, text="Finish", command=lambda: self.controller.show_frame(SubmissionComplete))
        self.add_more_button = tk.Button(self, text="Add more power", command=self.show_add_power_generation_frame)
    
    def show_add_power_generation_frame(self):
        self.controller.clear_inputs("AddPowerGeneration")
        self.controller.show_frame("AddPowerGeneration")
    
    def refresh(self):
        shared_data = self.controller.get_data()
        print(shared_data)

        # Remove all existing power generation labels and delete buttons
        for label in self.power_gen_labels:
            label.destroy()

        for button in self.delete_buttons:
            button.destroy()

        # Clear the power_gen_labels and delete_buttons lists
        self.power_gen_labels.clear()
        self.delete_buttons.clear()

        # Get the power_generation_numbers from the shared_data
        power_generation_numbers = [data['power_generation_number'] for data in shared_data if data]
        # Process shared_data and display it in the frame
        self.show_power_generation_list(shared_data)

        last_row = 2 + len(shared_data)
        self.next_button.grid(row=last_row, column=0, padx=10, pady=10)
        self.add_more_button.grid(row=last_row + 1, column=0, padx=10, pady=10)
    
    def delete_record(self, index, power_gen_info):
        cursor = CONN.cursor()
        cursor.execute("DELETE FROM powergeneration WHERE power_generation_number = %s", (power_gen_info['power_generation_number'],))
        CONN.commit()

        # Remove the deleted record from the shared_data
        self.controller.remove_data(power_gen_info)

        # Remove the label and button associated with the deleted record
        self.power_gen_labels[index - 1].destroy()
        self.delete_buttons[index - 1].destroy()

        # Update the remaining labels and buttons
        for i in range(index, len(self.power_gen_labels)):
            self.power_gen_labels[i].grid_forget()
            self.delete_buttons[i].grid_forget()
            self.power_gen_labels[i].grid(row=i, column=0, padx=10, pady=5, sticky="W")
            self.delete_buttons[i].grid(row=i, column=1, padx=10, pady=5)

        self.refresh()
    
    def show_power_generation_list(self, power_generation_list):
        self.power_gen_labels = []
        self.delete_buttons = []
        for index, power_gen_info in enumerate(power_generation_list, start=1):
            label_text = f"{index}. {power_gen_info['power_generation_type']} - {power_gen_info['monthly_kwh']} kWh/month - {power_gen_info['storage_kwh']} kWh storage"
            label = tk.Label(self, text=label_text, font=("Verdana", 12))
            label.grid(row=1 + index, column=0, padx=10, pady=5, sticky="W")
            self.power_gen_labels.append(label)

            delete_button = tk.Button(self, text="Delete", command=partial(self.delete_record, index, power_gen_info))
            delete_button.grid(row=1 + index, column=1, padx=10, pady=5)
            self.delete_buttons.append(delete_button)
        
        # Update the row and column of the "Finish" button
        last_row = 2 + len(power_generation_list)
        self.next_button.grid(row=last_row, column=0, padx=10, pady=10)
        self.add_more_button.grid(row=last_row + 1, column=0, padx=10, pady=10)
    

  