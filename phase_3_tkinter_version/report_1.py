import tkinter as tk
from db_and_sql_handler import USE_DATABASE_SQL, CONN

cursor = CONN.cursor()
cursor.execute(USE_DATABASE_SQL)

SQL_QUERY_1 = 'SELECT manufacturer_name, COUNT(*) AS appliances_number FROM Appliance GROUP BY manufacturer_name ORDER BY appliances_number DESC LIMIT 25'
SQL_QUERY_2 = "SELECT appliance_type, COUNT(*) AS appliance_count FROM Appliance WHERE manufacturer_name = '{name}' GROUP BY appliance.appliance_type"

# report 1 window frame
class Report1(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        self.parent = parent
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Report 1", font=("Verdana", 25))
        label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        label = tk.Label(self, text="Manufacturer", font=("Verdana", 15))
        label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        label = tk.Label(self, text="Raw Count", font=("Verdana", 15))
        label.grid(row=1, column=1, padx=10, pady=10, sticky="W")

        # importing ViewReports here resolves circular import issue
        from view_reports_page import ViewReports
        cursor.execute(SQL_QUERY_1)
        r_set = cursor.fetchall()
        num_rows = len(r_set)
        start_row = 2
        # Going through the query results
        for r in range(num_rows):
            manufacture_name = r_set[r][0]
            count  = r_set[r][1]

            name_label = tk.Label(self, text=manufacture_name)
            name_label.grid(row = start_row + r, column=0)

            count_label = tk.Label(self, text=count)
            count_label.grid(row = start_row + r, column=1)

            drilldown_button = tk.Button(self, text='View Drilldown Report',command=lambda manufacture_name=manufacture_name: self.open_drilldown(manufacture_name))
            drilldown_button.grid(row=start_row + r, column=2)

        button_row = 2 + num_rows
        next_button = tk.Button(self, text="Return to View Reports", command=lambda: self.controller.show_frame(ViewReports))
        next_button.grid(row=button_row, column=0, padx=10, pady=10)

    def open_drilldown(self, manufacturer_name):
        # print(manufacturer_name)
        child = tk.Toplevel(self.parent)
        child.geometry('500x500')
        query = SQL_QUERY_2.format(name=manufacturer_name)
        child.title(manufacturer_name)
        title_label = tk.Label(child, text=manufacturer_name, font=("Verdana", 25))
        title_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        title_label = tk.Label(child, text='Appliance Type', font=("Verdana", 25))
        title_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        title_label = tk.Label(child, text='Raw Count', font=("Verdana", 25))
        title_label.grid(row=1, column=1, padx=10, pady=10, sticky="W")

        cursor.execute(query)
        result = cursor.fetchall()
        rows = len(result)

        def convert(type):
            if type == 'water_heater':
                return 'Water Heater'
            elif type == 'air_handler':
                return 'Air Handler'
        for i in range(rows):
            appliance_type = convert(result[i][0])
            number = result[i][1]
            appliance_type_label = tk.Label(child, text=appliance_type)
            number_label = tk.Label(child, text=number)
            appliance_type_label.grid(row=2 + i, column=0, padx=10, pady=10, sticky="W")
            number_label.grid(row=2 + i, column=1, padx=10, pady=10, sticky="W")
