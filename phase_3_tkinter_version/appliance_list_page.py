import tkinter as tk
from tkinter import ttk
from tkinter import *
from add_power_generation_page import AddPowerGeneration
from db_and_sql_handler import USE_DATABASE_SQL, CONN

cursor = CONN.cursor()
cursor.execute(USE_DATABASE_SQL)

email = "johndoe@gmail.com"

"""
BUG: cursor.excute does not proc the email
"""

def query_appliance_list(email_address):
    appliance_lists = []
    cursor.execute("SELECT appliance_number, CAST(appliance_type AS UNSIGNED INTEGER) AS appliance_type, manufacturer_name, model_name FROM Appliance WHERE email='johndoe@gmail.com' ORDER BY appliance_number ASC")
    query_result = cursor.fetchall()
    for query in query_result:
        appliance_lists.append(query)
    return query_result

# appliance list page window frame
class ApplianceList(tk.Frame):
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Appliances", font=("Verdana", 25))
        label.grid(row=0, column=0, padx=10, pady=10, sticky="W")
        
        label2 = tk.Label(self, text="You have added the following appliances to your hosuehold:", font=("Verdana", 18))
        label2.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        '''
        for i in range(total_rows):
            for j in range(total_cols):
                self.e = Entry(parent, width=20, fg='blue',font=('Arial',16,'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, appliance_lists[i][j])
        '''
        query_results = query_appliance_list(email)
        self.create_appliance_list(query_results)

        add_appliance_label = tk.Label(self, text="+Add Another Appliance", fg='blue', font=("Verdana", 10))
        add_appliance_label.grid(row=9, column=0, padx=5, pady=5, sticky="W")
        from add_appliance_page import AddAppliance
        add_appliance_label.bind("<Button-1>", lambda e: [controller.show_frame(AddAppliance), self.refresh()])

        next_button = tk.Button(self, text="Next", command=lambda: controller.show_frame(AddPowerGeneration))
        next_button.grid(row=10, column=0, padx=10, pady=10)
    
    def create_appliance_list(self, query_results):
        total_rows = len(query_results)
        total_cols = len(query_results[0])
        '''[(1, 1, 'GE', 'Model A'), (6, 0, 'LG', 'Model B')]'''
        s = ttk.Style()
        s.theme_use('clam')
        self.tree = ttk.Treeview(self, column=("c1", "c2", "c3", "c4", "c5"), show='headings', height=5)
        self.tree.column("# 1", anchor=CENTER)
        self.tree.heading("# 1", text="Appliance #")
        self.tree.column("# 2", anchor=CENTER)
        self.tree.heading("# 2", text="Type")
        self.tree.column("# 3", anchor=CENTER)
        self.tree.heading("# 3", text="Manufacturer")
        self.tree.column("# 4", anchor=CENTER)
        self.tree.heading("# 4", text="Model")
        self.tree.column("# 5", anchor=CENTER)
        self.tree.heading("# 5", text="")

        #print("appliance_list[0][3] should be GE:::", appliance_lists[0][3])   
        for i in range(0, len(query_results)):
            appliance_number = i+1
            appliance_id = query_results[i][0]
            appliance_type = query_results[i][1]
            manufacturer = query_results[i][2]
            model = query_results[i][3]
            delete_button = tk.Label(self, text="delete", fg='blue', font=("Verdana", 10))
            self.tree.bind("<<TreeviewSelect>>", self.delete)
            self.tree.insert('', 'end', text="1", values=(appliance_number, appliance_type, manufacturer, model, delete_button.cget("text"), appliance_id))
        # Insert the data in Treeview widget
        #tree.insert('', 'end', text="1", values=('1', 'Joe', 'Nash', 'Melfragerator', 'delete'))
        self.tree.grid(row=2, column=0, padx=10, pady=10, sticky="W")
    
    def delete(self, event):
        selected_item = self.tree.selection()[0] ## get selected item
        curr_item_info = self.tree.item(self.tree.focus())
        print('selected_item::', selected_item)
        print('curr_item_info::', curr_item_info['values'])
        self.tree.delete(selected_item)

    def selectItem(self, event):
        curItem = self.tree.item(self.tree.focus())
        col = self.tree.identify_column(event.x)
        row = self.tree.identify_row(event.y)
        print ('curItem = ', curItem)
        print ('col = ', col)
        print('row = ', row)

        if col == '#0':
            cell_value = curItem['text']
        elif col == '#1':
            cell_value = curItem['values'][0]
        elif col == '#2':
            cell_value = curItem['values'][1]
        elif col == '#3':
            cell_value = curItem['values'][2]
        print ('cell_value = ', cell_value)

    def refresh(self):
        print("yet to refresh")