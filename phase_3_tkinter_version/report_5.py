from report_1 import *
import tkinter as tk

from db_and_sql_handler import USE_DATABASE_SQL, CONN

cursor = CONN.cursor()
cursor.execute(USE_DATABASE_SQL)

QUERY_1 = 'SELECT Address.state, COUNT(*) AS count ' \
          'FROM Household ' \
          'JOIN Address ON Household.postal_code = Address.postal_code ' \
          'LEFT JOIN PublicUtility ON Household.email = PublicUtility.email ' \
          'WHERE PublicUtility.public_utility = "Off-The-Grid" ' \
          'GROUP BY Address.state ' \
          'HAVING count = ( ' \
          'SELECT MAX(count) ' \
          'FROM ( ' \
          'SELECT COUNT(*) AS count ' \
          'FROM Household ' \
          'JOIN Address ON Household.postal_code = Address.postal_code ' \
          'LEFT JOIN PublicUtility ON Household.email = PublicUtility.email ' \
          'WHERE PublicUtility.public_utility = "Off-The-Grid" ' \
          'GROUP BY Address.state ) AS t )' \
          'ORDER BY count'

QUERY_2 = "SELECT COUNT(CASE WHEN PublicUtility.public_utility = 'Off-The-Grid' THEN 1 END) AS off_grid_count, " \
          "ROUND(AVG(CASE WHEN PublicUtility.public_utility = 'Off-The-Grid' THEN PowerGeneration.battery_storage_capacity END)) AS average_battery_storage_capacity " \
          "FROM Household JOIN PublicUtility ON Household.email = PublicUtility.email " \
          "LEFT JOIN PowerGeneration ON Household.email = PowerGeneration.email " \
          "WHERE PublicUtility.public_utility = 'Off-The-Grid';"

QUERY_3 = "SELECT " \
          "CONCAT(ROUND(((SELECT COUNT( *) AS total_count " \
          "FROM PowerGeneration " \
          "WHERE PowerGeneration.email IN " \
          "( SELECT email " \
          "FROM PowerGeneration " \
          "GROUP BY email " \
          "HAVING COUNT(DISTINCT generation_type) > 1 " \
          ")) / COUNT(*)) *100, 1), '%') " \
          "AS mixed_percentage, " \
          "CONCAT(ROUND((SUM(CASE WHEN generation_type = 'solar-electric' THEN 1 ELSE 0 END) / COUNT(*)) * 100, 1), '%') AS solar_electric_percentage, " \
          "CONCAT(ROUND(((SUM(CASE WHEN generation_type = 'wind' THEN 1 ELSE 0 END)) / COUNT(*)) * 100, 1), '%') AS wind_percentage " \
          "FROM PowerGeneration JOIN Household ON Household.email = PowerGeneration.email " \
          "JOIN PublicUtility ON Household.email = PublicUtility.email " \
          "WHERE PublicUtility.public_utility = 'Off-The-Grid'"

QUERY_4 = "SELECT ROUND(AVG(CASE WHEN PublicUtility.public_utility != 'Off-The-Grid' THEN WaterHeater.capacity END), 1) AS grid_avg_capacity, " \
          "ROUND(AVG(CASE WHEN PublicUtility.public_utility = 'Off-The-Grid' THEN WaterHeater.capacity END), 1) AS off_grid_avg_capacity " \
          "FROM Household JOIN PowerGeneration ON Household.email = PowerGeneration.email " \
          "LEFT JOIN PublicUtility ON Household.email = PublicUtility.email JOIN Appliance ON Household.email = Appliance.email " \
          "LEFT JOIN WaterHeater ON Appliance.appliance_number = WaterHeater.appliance_number AND Appliance.email = WaterHeater.email;"

QUERY_5 = "SELECT Appliance.appliance_type, " \
          "ROUND(MIN(Appliance.btu_rating), 0) AS min_btu, " \
          "ROUND(AVG(Appliance.btu_rating), 0) AS avg_btu, " \
          "ROUND(MAX(Appliance.btu_rating), 0) AS max_btu " \
          "FROM Household " \
          "JOIN PowerGeneration ON Household.email = PowerGeneration.email " \
          "LEFT JOIN PublicUtility ON Household.email = PublicUtility.email " \
          "JOIN Appliance ON Household.email = Appliance.email " \
          "WHERE PublicUtility.public_utility = 'Off-The-Grid' " \
          "GROUP BY Appliance.appliance_type;"

# report 5 window frame
class Report5(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        self.parent = parent
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Report 5", font=("Verdana", 25))
        label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        # Table 1
        label = tk.Label(self, text="State with Most off-the-grid household", font=("Verdana", 15))
        label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        label = tk.Label(self, text="Count of HouseHold", font=("Verdana", 15))
        label.grid(row=1, column=1, padx=10, pady=10, sticky="W")

        # Table 1 Query
        cursor.execute(QUERY_1)
        query_1_result = cursor.fetchall()
        num_of_rows_query_1_result = len(query_1_result)

        query_1_start_row = 2

        for r in range(num_of_rows_query_1_result):
            state = query_1_result[r][0]
            count = query_1_result[r][1]

            state_label = tk.Label(self, text=state, font=("Verdana, 15"))
            state_label.grid(row = query_1_start_row + r, column= 0, padx=10, pady=10, sticky="W")

            count_label = tk.Label(self, text=count, font=("Verdana, 15"))
            count_label.grid(row = query_1_start_row + r, column= 1, padx=10, pady=10, sticky="W")

        query_2_start_row = query_1_start_row + num_of_rows_query_1_result

        # Table 2 Query
        cursor.execute(QUERY_2)
        query_2_result = cursor.fetchall()
        num_of_rows_query_2_result = len(query_2_result)

        # Table 2
        label = tk.Label(self, text="Average Battery storage capacity for all households", font=("Verdana", 15))
        label.grid(row=query_2_start_row, column=0, padx=10, pady=10, sticky="W")

        query_2_start_row += 1

        label = tk.Label(self, text=query_2_result[0][1], font=("Verdana", 15))
        label.grid(row=query_2_start_row, column=0, padx=10, pady=10, sticky="W")
        #
        # Table 3 Query
        query_3_start_row = query_2_start_row + num_of_rows_query_2_result
        cursor.execute(QUERY_3)
        query_3_result = cursor.fetchall()
        num_of_rows_query_3_result = len(query_3_result)

        # Table 3
        label = tk.Label(self, text="Mixed Percentage", font=("Verdana", 15))
        label.grid(row=query_3_start_row, column=0, padx=10, pady=10, sticky="W")

        label = tk.Label(self, text="Solar-electric Percentage", font=("Verdana", 15))
        label.grid(row=query_3_start_row, column=1, padx=10, pady=10, sticky="W")

        label = tk.Label(self, text="Wind Percentage", font=("Verdana", 15))
        label.grid(row=query_3_start_row, column=2, padx=10, pady=10, sticky="W")

        query_3_start_row += 1

        label = tk.Label(self, text=query_3_result[0][0], font=("Verdana", 15))
        label.grid(row=query_3_start_row, column=0, padx=10, pady=10, sticky="W")

        label = tk.Label(self, text=query_3_result[0][1], font=("Verdana", 15))
        label.grid(row=query_3_start_row, column=1, padx=10, pady=10, sticky="W")

        label = tk.Label(self, text=query_3_result[0][2], font=("Verdana", 15))
        label.grid(row=query_3_start_row, column=2, padx=10, pady=10, sticky="W")
        #
        # Table 4 Query
        query_4_start_row = query_3_start_row + num_of_rows_query_3_result
        cursor.execute(QUERY_4)
        query_4_result = cursor.fetchall()
        num_of_rows_query_4_result = len(query_4_result)

        # Table 4
        label = tk.Label(self, text="Average Water heater gallon capacity for 'on-the-grid' households", font=("Verdana", 15))
        label.grid(row=query_4_start_row, column=0, padx=10, pady=10, sticky="W")

        label = tk.Label(self, text="Average Water heater gallon capacity for 'off-the-grid' households", font=("Verdana", 15))
        label.grid(row=query_4_start_row, column=1, padx=10, pady=10, sticky="W")

        query_4_start_row += 1

        label = tk.Label(self, text=query_4_result[0][0], font=("Verdana", 15))
        label.grid(row=query_4_start_row, column=0, padx=10, pady=10, sticky="W")

        label = tk.Label(self, text=query_4_result[0][1], font=("Verdana", 15))
        label.grid(row=query_4_start_row, column=1, padx=10, pady=10, sticky="W")

        # Table 5 Query
        query_5_start_row = query_4_start_row + num_of_rows_query_4_result
        cursor.execute(QUERY_5)
        query_5_result = cursor.fetchall()
        num_of_rows_query_5_result = len(query_5_result)
        print(query_5_result)

        # Table 5
        label = tk.Label(self, text="Appliance Type", font=("Verdana", 15))
        label.grid(row=query_5_start_row, column=0, padx=10, pady=10, sticky="W")

        label = tk.Label(self, text="Min BTU", font=("Verdana", 15))
        label.grid(row=query_5_start_row, column=1, padx=10, pady=10, sticky="W")

        label = tk.Label(self, text="Average BTU", font=("Verdana", 15))
        label.grid(row=query_5_start_row, column=2, padx=10, pady=10, sticky="W")

        label = tk.Label(self, text="Max BTU", font=("Verdana", 15))
        label.grid(row=query_5_start_row, column=3, padx=10, pady=10, sticky="W")

        query_5_start_row += 1

        def convert(type):
            if type == 'water_heater':
                return 'Water Heater'
            elif type == 'air_handler':
                return 'Air Handler'

        for r in range(num_of_rows_query_5_result):
            appliance_type = convert(query_5_result[r][0])
            min_btu = query_5_result[r][1]
            avg_btu = query_5_result[r][2]
            max_btu = query_5_result[r][3]

            appliance_type_label = tk.Label(self, text=appliance_type, font=("Verdana, 15"))
            appliance_type_label.grid(row = query_5_start_row + r, column= 0, padx=10, pady=10, sticky="W")

            min_btu_label = tk.Label(self, text=min_btu, font=("Verdana, 15"))
            min_btu_label.grid(row = query_5_start_row + r, column= 1, padx=10, pady=10, sticky="W")

            avg_btu_label = tk.Label(self, text=avg_btu, font=("Verdana, 15"))
            avg_btu_label.grid(row = query_5_start_row + r, column= 2, padx=10, pady=10, sticky="W")

            max_btu_label = tk.Label(self, text=max_btu, font=("Verdana, 15"))
            max_btu_label.grid(row = query_5_start_row + r, column= 3, padx=10, pady=10, sticky="W")

        next_row = query_5_start_row + num_of_rows_query_5_result
        # importing ViewReports here resolves circular import issue
        from view_reports_page import ViewReports
        next_button = tk.Button(self, text="Return to View Reports", command=lambda: controller.show_frame(ViewReports))
        next_button.grid(row=next_row, column=0, padx=10, pady=10)

