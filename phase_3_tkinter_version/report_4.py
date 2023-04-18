import tkinter as tk
from db_and_sql_handler import USE_DATABASE_SQL, CONN

cursor = CONN.cursor()
cursor.execute(USE_DATABASE_SQL)

SQL_QUERY_1 = 'SELECT Address.state AS state, ' \
              'IFNULL(ROUND(AVG(WaterHeater.capacity)), 0) AS avg_capacity, ' \
              'IFNULL(ROUND(AVG(Appliance.btu_rating)), 0) AS avg_btu, ' \
              'IFNULL(ROUND(AVG(WaterHeater.temperature), 10), 0) AS avg_temp, ' \
              'IFNULL(COUNT(CASE WHEN WaterHeater.temperature IS NOT NULL THEN 1 END), 0) ' \
              'AS temp_set, IFNULL(COUNT(CASE WHEN WaterHeater.temperature IS NULL THEN 1 END), 0) ' \
              'AS temp_no_set ' \
              'FROM Household ' \
              'LEFT JOIN Address ON Household.postal_code = Address.postal_code ' \
              'LEFT JOIN WaterHeater ON Household.email = WaterHeater.email ' \
              'LEFT JOIN Appliance ON WaterHeater.email = Appliance.email ' \
              'AND WaterHeater.appliance_number = Appliance.appliance_number ' \
              'GROUP BY Address.state ' \
              'ORDER BY Address.state ASC;'

SQL_QUERY_2 = 'SELECT WaterHeater.energy_source AS EnergySource, ' \
              'ROUND(MIN(WaterHeater.capacity),0) AS MinCapacity, ' \
              'ROUND(AVG(WaterHeater.capacity),0) AS AvgCapacity, ' \
              'ROUND(MAX(WaterHeater.capacity),0) AS MaxCapacity, ' \
              'ROUND(MIN(WaterHeater.temperature),10) AS MinTemp, ' \
              'ROUND(AVG(WaterHeater.temperature), 10) AS AvgTemp, ' \
              'ROUND(MAX(WaterHeater.temperature),10) AS MaxTemp ' \
              'FROM WaterHeater ' \
              'INNER JOIN Appliance ON WaterHeater.email = Appliance.email  ' \
              'INNER JOIN Household ON Household.email = WaterHeater.email ' \
              'INNER JOIN Address ON Household.postal_code = Address.postal_code   ' \
              'WHERE Address.state = "{state}" ' \
              'GROUP BY WaterHeater.energy_source ' \
              'ORDER BY WaterHeater.energy_source ASC;'

# 'SET @search = "{state}"; ' \
# report 4 window frame
class Report4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        label = tk.Label(self, text="Report 4", font=("Verdana", 25))
        label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        label = tk.Label(self, text="State", font=("Verdana", 10))
        label.grid(row=1, column=0, sticky="W")

        label = tk.Label(self, text="Average Water Heater Capacity", font=("Verdana", 10))
        label.grid(row=1, column=1, sticky="W")

        label = tk.Label(self, text="Average Water Heater BTUs", font=("Verdana", 10))
        label.grid(row=1, column=2, sticky="W")

        label = tk.Label(self, text="Average Water Heater Temperature Settings", font=("Verdana", 10))
        label.grid(row=1, column=3, sticky="W")

        label = tk.Label(self, text="Count of Water Heater with Temp Settings", font=("Verdana", 10))
        label.grid(row=1, column=4, sticky="W")

        label = tk.Label(self, text="Count of Water Heater with No Temp Settings", font=("Verdana", 10))
        label.grid(row=1, column=5, sticky="W")

        start_row = 2
        cursor.execute(SQL_QUERY_1)
        query_1_result = cursor.fetchall()
        num_rows = len(query_1_result)
        for r in range(num_rows):
            state = query_1_result[r][0]
            avg_water_heater_capacity = query_1_result[r][1]
            avg_water_heater_BTUs = query_1_result[r][2]
            avg_water_heater_temperature_setting = query_1_result[r][3]
            count_water_heaters_with_setting = query_1_result[r][4]
            count_water_heaters_with_no_setting = query_1_result[r][5]

            state_label = tk.Label(self, text=state, font=("Verdana", 10))
            state_label.grid(row=start_row + r, column=0, sticky="W")

            avg_water_heater_capacity_label = tk.Label(self, text=avg_water_heater_capacity, font=("Verdana", 10))
            avg_water_heater_capacity_label.grid(row=start_row + r, column=1, sticky="W")

            avg_water_heater_BTUs_label = tk.Label(self, text=avg_water_heater_BTUs, font=("Verdana", 10))
            avg_water_heater_BTUs_label.grid(row=start_row + r, column=2, sticky="W")

            avg_water_heater_temperature_setting_label = tk.Label(self, text=avg_water_heater_temperature_setting, font=("Verdana", 10))
            avg_water_heater_temperature_setting_label.grid(row=start_row + r, column=3, sticky="W")

            count_water_heaters_with_setting_label = tk.Label(self, text=count_water_heaters_with_setting,font=("Verdana", 10))
            count_water_heaters_with_setting_label.grid(row=start_row + r, column=4, sticky="W")

            count_water_heaters_with_no_setting_label = tk.Label(self, text=count_water_heaters_with_no_setting,font=("Verdana", 10))
            count_water_heaters_with_no_setting_label.grid(row=start_row + r, column=5, sticky="W")

            drilldown_button = tk.Button(self, text='View Drilldown Report',command=lambda state=state: self.open_drilldown(state))
            drilldown_button.grid(row=start_row + r, column=6)

        start_row += num_rows
        from view_reports_page import ViewReports
        next_button = tk.Button(self, text="Return to View Reports", command=lambda: controller.show_frame(ViewReports))
        next_button.grid(row=start_row, column=0, padx=10, pady=10)

    def open_drilldown(self, state):
        child = tk.Toplevel(self.parent)
        child.geometry('500x500')
        query = SQL_QUERY_2.format(state=state)
        child.title(state)
        title_label = tk.Label(child, text=state, font=("Verdana", 25))
        title_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")
        cursor.execute(query)
        result = cursor.fetchall()
        num_rows = len(result)
        print(result)

        label = tk.Label(child, text="Minimum Water Heater Capacity", font=("Verdana", 10))
        label.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        label = tk.Label(child, text="Average Water Heater Capacity", font=("Verdana", 10))
        label.grid(row=3, column=0, padx=10, pady=10, sticky="W")

        label = tk.Label(child, text="Maximum Water Heater Capacity", font=("Verdana", 10))
        label.grid(row=4, column=0, padx=10, pady=10, sticky="W")

        label = tk.Label(child, text="Minimum Temperature Setting", font=("Verdana", 10))
        label.grid(row=5, column=0, padx=10, pady=10, sticky="W")

        label = tk.Label(child, text="Average Temperature Setting", font=("Verdana", 10))
        label.grid(row=6, column=0, padx=10, pady=10, sticky="W")

        label = tk.Label(child, text="Maximum Temperature Setting", font=("Verdana", 10))
        label.grid(row=7, column=0, padx=10, pady=10, sticky="W")

        for r in range(num_rows):
            energy_source = result[r][0]
            energy_source_label = tk.Label(child, text=energy_source, font=("Verdana", 10))
            energy_source_label.grid(row=1, column=r + 1, sticky="W")

            min_water_heater_capacity = result[r][1]
            min_water_heater_capacity_label = tk.Label(child, text=min_water_heater_capacity, font=("Verdana", 10))
            min_water_heater_capacity_label.grid(row=2, column=r + 1, sticky="W")

            avg_water_heater_capacity = result[r][2]
            avg_water_heater_capacity_label = tk.Label(child, text=avg_water_heater_capacity, font=("Verdana", 10))
            avg_water_heater_capacity_label.grid(row=3, column=r + 1, sticky="W")

            max_water_heater_capacity = result[r][3]
            max_water_heater_capacity_label = tk.Label(child, text=max_water_heater_capacity, font=("Verdana", 10))
            max_water_heater_capacity_label.grid(row=4, column=r + 1, sticky="W")

            min_temperature_setting = result[r][4]
            min_temperature_setting_label = tk.Label(child, text=min_temperature_setting, font=("Verdana", 10))
            min_temperature_setting_label.grid(row=5, column=r + 1, sticky="W")

            avg_temperature_setting = result[r][5]
            avg_temperature_setting_label = tk.Label(child, text=avg_temperature_setting, font=("Verdana", 10))
            avg_temperature_setting_label.grid(row=6, column=r + 1, sticky="W")

            max_temperature_setting = result[r][6]
            max_temperature_setting_label = tk.Label(child, text=max_temperature_setting, font=("Verdana", 10))
            max_temperature_setting_label.grid(row=7, column=r + 1, sticky="W")


