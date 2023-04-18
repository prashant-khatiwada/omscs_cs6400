import tkinter as tk
from db_and_sql_handler import USE_DATABASE_SQL, CONN

cursor = CONN.cursor()
cursor.execute(USE_DATABASE_SQL)

Air_condtioner_query = 'SELECT ' \
                       'household_types, ' \
                       'COUNT(AirConditioner.appliance_number) AS count, ' \
                       'ROUND(AVG(Appliance.btu_rating)) AS average_btu, ' \
                       'ROUND(AVG(AirConditioner.eer),1) AS average_eer ' \
                       'FROM AirConditioner ' \
                       'INNER JOIN Appliance ON AirConditioner.email = Appliance.email ' \
                       'INNER JOIN Household ON AirConditioner.email = Household.email ' \
                       'GROUP BY Household.household_types ' \
                       'ORDER BY household_types'

Heater_query = 'SELECT household_types, ' \
               'COUNT(Heater.appliance_number) AS count, ' \
               'ROUND(AVG(Appliance.btu_rating)) AS average_btu, ' \
               '(SELECT energy_source FROM Heater RIGHT JOIN Household ON Heater.email = Household.email GROUP BY energy_source ORDER BY COUNT(*) DESC LIMIT 1 ) ' \
               'AS common_source ' \
               'FROM Heater ' \
               'INNER JOIN Appliance ON Heater.email = Appliance.email ' \
               'INNER JOIN Household ON Heater.email = Household.email ' \
               'GROUP BY Household.household_types ' \
               'ORDER BY household_types'

HeatPump_query = 'SELECT Household.household_types, ' \
                 'COUNT(HeatPump.appliance_number) AS count, ' \
                 'ROUND(AVG(Appliance.btu_rating)) AS average_btu, ' \
                 'ROUND(AVG(HeatPump.seer), 1) AS average_seer,  ' \
                 'ROUND(AVG(HeatPump.hspf), 1) AS average_hsbf FROM HeatPump ' \
                 'INNER JOIN Appliance ON HeatPump.email = Appliance.email ' \
                 'INNER JOIN Household ON HeatPump.email = Household.email ' \
                 'GROUP BY Household.household_types ' \
                 'ORDER BY household_types'

# report 3 window frame
class Report3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Report 3", font=("Verdana", 25))
        label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        # First Table Row Names
        label = tk.Label(self, text="Air Conditioners Count", font=("Verdana", 15))
        label.grid(row=1, column=1, padx=10, pady=10, sticky="W")

        label = tk.Label(self, text="Average Air Conditioner BTUs", font=("Verdana", 15))
        label.grid(row=1, column=2, padx=10, pady=10, sticky="W")

        label = tk.Label(self, text="Average EER", font=("Verdana", 15))
        label.grid(row=1, column=3, padx=10, pady=10, sticky="W")

        # First Query
        cursor.execute(Air_condtioner_query)
        air_conditioner_result = cursor.fetchall()
        query_1_row = len(air_conditioner_result)

        start_row = 2
        # Creating First Table
        for r in range(query_1_row):
            householdType = air_conditioner_result[r][0]
            count = air_conditioner_result[r][1]
            average_btu_rating = air_conditioner_result[r][2]
            average_eer = air_conditioner_result[r][3]
            # First Table Col Names
            householdType_label = tk.Label(self, text=householdType, font=("Verdana", 15))
            householdType_label.grid(row=start_row + r, column=0, padx=10, pady=10, sticky="W")

            count_label = tk.Label(self, text=count, font=("Verdana", 15))
            count_label.grid(row=start_row + r, column=1, padx=10, pady=10, sticky="W")

            average_btu_rating_label = tk.Label(self, text=average_btu_rating, font=("Verdana", 15))
            average_btu_rating_label.grid(row=start_row + r, column=2, padx=10, pady=10, sticky="W")

            average_eer = tk.Label(self, text=average_eer, font=("Verdana", 15))
            average_eer.grid(row=start_row + r, column=3, padx=10, pady=10, sticky="W")
        #
        start_row = start_row + query_1_row

        # Second Table
        h_label = tk.Label(self, text="Heaters Count", font=("Verdana", 15))
        h_label.grid(row=start_row, column=1, padx=10, pady=10, sticky="W")

        h_label = tk.Label(self, text="Average Heater BTUs", font=("Verdana", 15))
        h_label.grid(row=start_row, column=2, padx=10, pady=10, sticky="W")

        h_label = tk.Label(self, text="Most Common Energy Source", font=("Verdana", 15))
        h_label.grid(row=start_row, column=3, padx=10, pady=10, sticky="W")

        #Second Query
        cursor.execute(Heater_query)
        Heater_query_result = cursor.fetchall()
        query_2_row = len(Heater_query_result)
        start_row += 1

        for r in range(query_2_row):
            householdType = Heater_query_result[r][0]
            count = Heater_query_result[r][1]
            average_btu_rating = Heater_query_result[r][2]
            most_common_energy_source = Heater_query_result[r][3]

            # First Table Col Names
            householdType_label = tk.Label(self, text=householdType, font=("Verdana", 15))
            householdType_label.grid(row=start_row + r, column=0, padx=10, pady=10, sticky="W")

            count_label = tk.Label(self, text=count, font=("Verdana", 15))
            count_label.grid(row=start_row + r, column=1, padx=10, pady=10, sticky="W")

            average_btu_rating_label = tk.Label(self, text=average_btu_rating, font=("Verdana", 15))
            average_btu_rating_label.grid(row=start_row + r, column=2, padx=10, pady=10, sticky="W")


            most_common_energy_source = '' if most_common_energy_source is None else most_common_energy_source
            most_common_energy_source_label = tk.Label(self, text=most_common_energy_source, font=("Verdana", 15))
            most_common_energy_source_label.grid(row=start_row + r, column=3, padx=10, pady=10, sticky="W")
        #
        # # Table 3
        cursor.execute(HeatPump_query)
        HeatPump_query_result = cursor.fetchall()
        query_3_row = len(HeatPump_query_result)
        start_row = start_row + query_2_row

        ht_label = tk.Label(self, text="Heat Pump Count", font=("Verdana", 15))
        ht_label.grid(row=start_row, column=1, padx=10, pady=10, sticky="W")

        ht_label = tk.Label(self, text="Average HeatPump BTUs", font=("Verdana", 15))
        ht_label.grid(row=start_row, column=2, padx=10, pady=10, sticky="W")

        ht_label = tk.Label(self, text="Average SEER", font=("Verdana", 15))
        ht_label.grid(row=start_row, column=3, padx=10, pady=10, sticky="W")

        ht_label = tk.Label(self, text="Average SEER", font=("Verdana", 15))
        ht_label.grid(row=start_row, column=4, padx=10, pady=10, sticky="W")

        start_row += 1

        for r in range(query_3_row):
            householdType = HeatPump_query_result[r][0]
            count = HeatPump_query_result[r][1]
            average_btu_rating = HeatPump_query_result[r][2]
            average_seer = HeatPump_query_result[r][3]
            average_hspf = HeatPump_query_result[r][4]
            # First Table Col Names
            householdType_label = tk.Label(self, text=householdType, font=("Verdana", 15))
            householdType_label.grid(row=start_row + r, column=0, padx=10, pady=10, sticky="W")

            count_label = tk.Label(self, text=count, font=("Verdana", 15))
            count_label.grid(row=start_row + r, column=1, padx=10, pady=10, sticky="W")

            average_btu_rating_label = tk.Label(self, text=average_btu_rating, font=("Verdana", 15))
            average_btu_rating_label.grid(row=start_row + r, column=2, padx=10, pady=10, sticky="W")

            average_seer_label = tk.Label(self, text=average_seer, font=("Verdana", 15))
            average_seer_label.grid(row=start_row + r, column=3, padx=10, pady=10, sticky="W")

            average_hspf_label = tk.Label(self, text=average_hspf, font=("Verdana", 15))
            average_hspf_label.grid(row=start_row + r, column=4, padx=10, pady=10, sticky="W")
        #
        # # importing ViewReports here resolves circular import issue
        start_row = start_row + query_3_row
        from view_reports_page import ViewReports
        next_button = tk.Button(self, text="Return to View Reports", command=lambda: controller.show_frame(ViewReports))
        next_button.grid(row=start_row, column=0, padx=10, pady=10)