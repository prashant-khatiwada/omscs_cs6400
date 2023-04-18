import tkinter as tk
from tkinter import messagebox
from db_and_sql_handler import USE_DATABASE_SQL, CONN

ERROR_MESSAGE_TITLE = "Report 6 Input Error"
POSTALCODE_EMPTY_INPUT_ERROR_MESSAGE = "Please provide a postal code"
POSTALCODE_MISMATCH_ERROR_MESSAGE = "Postal code you provided does not exist in the database"
POSTALCODE_TYPE_ERROR_MESSAGE = "Postal code must be in numbers"
RADIUS_EMPTY_INPUT_ERROR_MESSAGE = "Please provide an input radius"
RADIUS_INVALID_INPUT_ERROR_MESSAGE = "The radius must be a positive integer"


cursor = CONN.cursor()
cursor.execute(USE_DATABASE_SQL)

SQL_QUERY_1 = "SELECT " \
              "Household.household_types," \
              "COUNT(*) AS household_count," \
              "SUM(CASE WHEN household_types = 'House' THEN 1 ELSE 0 END) AS type_house, " \
              "SUM(CASE WHEN household_types = 'Apartment' THEN 1 ELSE 0 END) AS type_apartment, " \
              "SUM(CASE WHEN household_types = 'Townhome' THEN 1 ELSE 0 END) AS type_townhome, " \
              "SUM(CASE WHEN household_types = 'Condominium' THEN 1 ELSE 0 END) type_condominium, " \
              "SUM(CASE WHEN household_types = 'Mobile Home' THEN 1 ELSE 0 END) AS type_mobile_home, " \
              "ROUND(AVG(Household.square_footage)) AS Avg_Sq_Ft, " \
              "COALESCE(ROUND(AVG(Heating.temperature), 1), 0.0) AS Avg_Heating_Temp, " \
              "COALESCE(ROUND(AVG(Cooling.temperature), 1), 0.0) AS Avg_Cooling_Temp, " \
              "GROUP_CONCAT(DISTINCT PublicUtility.public_utility SEPARATOR ',') AS used_public_utilities, " \
              "COALESCE(SUM(CASE WHEN PublicUtility.public_utility = 'Off-The-Grid' THEN 1 ELSE 0 END), 0) AS off_grid_count, " \
              "COALESCE(SUM(CASE WHEN PowerGeneration.generation_type IS NOT NULL THEN 1 ELSE 0 END), 0) AS power_generation_count, " \
              "(SELECT GROUP_CONCAT(DISTINCT generation_type SEPARATOR ',') as generation_types " \
              "FROM PowerGeneration " \
              "GROUP BY PowerGeneration.generation_type " \
              "ORDER BY COUNT(*) DESC LIMIT 1) as Most_Common_Method, " \
              "COALESCE(ROUND(AVG(CASE WHEN PowerGeneration.monthly_power_generated IS NOT NULL THEN PowerGeneration.monthly_power_generated END)), 0) AS avg_monthly_power_generated, " \
              "COALESCE(SUM(CASE WHEN PowerGeneration.battery_storage_capacity IS NOT NULL THEN 1 ELSE 0 END), 0) AS battery_storage_count " \
              "FROM Household " \
              "JOIN Address ON Household.postal_code = Address.postal_code " \
              "LEFT JOIN PublicUtility ON Household.email = PublicUtility.email " \
              "LEFT JOIN Heating  ON Household.email = Heating.email " \
              "LEFT JOIN Cooling ON Household.email = Cooling.email " \
              "LEFT JOIN PowerGeneration ON Household.email = PowerGeneration.email " \
              "    WHERE Address.postal_code IN ( " \
              "SELECT postal_code FROM Address WHERE postal_code <> {postal_code} " \
              "AND (3958.75 * 2 * ATAN2( SQRT( SIN(RADIANS(latitude - " \
              "(SELECT latitude FROM Address WHERE postal_code = {postal_code}))) * " \
              "SIN(RADIANS(latitude - (SELECT latitude FROM Address WHERE postal_code = {postal_code}))) " \
              "+ COS(RADIANS(latitude)) * COS(RADIANS((SELECT latitude FROM Address WHERE postal_code = {postal_code}))) " \
              "* SIN(RADIANS(longitude - (SELECT longitude FROM Address WHERE postal_code = {postal_code}))) " \
              "* SIN(RADIANS(longitude - (SELECT longitude FROM Address WHERE postal_code = {postal_code}))) ), " \
              "SQRT(1 - SIN(RADIANS(latitude - (SELECT latitude FROM Address WHERE postal_code = {postal_code}))) " \
              "* SIN(RADIANS(latitude - (SELECT latitude FROM Address WHERE postal_code = {postal_code}))) - " \
              "COS(RADIANS(latitude)) * COS(RADIANS((SELECT latitude FROM Address WHERE postal_code = {postal_code}))) " \
              "* SIN(RADIANS(longitude - (SELECT longitude FROM Address WHERE postal_code = {postal_code}))) " \
              "* SIN(RADIANS(longitude - (SELECT longitude FROM Address WHERE postal_code = {postal_code})))))) " \
              "<= {radius} )GROUP BY Household.household_types;"

# report 6 window frame
def validate_postal_code(postal_code):
    if postal_code == "":
        messagebox.showerror(ERROR_MESSAGE_TITLE, POSTALCODE_EMPTY_INPUT_ERROR_MESSAGE)
        return False
    try:
        postal_code_cast = int(postal_code)
    except:
        messagebox.showerror(ERROR_MESSAGE_TITLE, POSTALCODE_TYPE_ERROR_MESSAGE)
        ## CHECK if needs to return False or close() etc
    if not isinstance(postal_code_cast, int):
        messagebox.showerror(ERROR_MESSAGE_TITLE, POSTALCODE_TYPE_ERROR_MESSAGE)
        return False
    cursor.execute("SELECT postal_code FROM Address WHERE postal_code=%s",(postal_code,))
    query_result = cursor.fetchall()
    if len(query_result) < 1:
        messagebox.showerror(ERROR_MESSAGE_TITLE, POSTALCODE_MISMATCH_ERROR_MESSAGE)
        return False

def validate_radius(radius):
    if radius == "":
        messagebox.showerror(ERROR_MESSAGE_TITLE, RADIUS_EMPTY_INPUT_ERROR_MESSAGE)
        return False
    if not isinstance(radius, int) or radius < 0:
        messagebox.showerror(ERROR_MESSAGE_TITLE, RADIUS_EMPTY_INPUT_ERROR_MESSAGE)
        return False

## output variables available here
def search_radius_execute_command(controller, params):
    # search radius params: {'input_postal_code': ..., 'input_radius': ...}

    radius = params['input_radius'].get()
    postal_code = params['input_postal_code'].get()

    print("radius::", radius)
    print("postal_code::", postal_code)

    # Validate inputs
    validation_1 = validate_postal_code(postal_code)
    # TODO: Search backend via mysql
    if validation_1 is not False:
        query = SQL_QUERY_1.format(postal_code=postal_code, radius=radius)
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        print(len(result))
        print(len(result[0]))
    return



class Report6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        label = tk.Label(self, text="Report 6", font=("Verdana", 25))
        label.grid(row=0, column=0,  sticky="W")

        # Radius Dropdown
        radius_lists = [
            0,5,10,25,50,100,250
        ]

        # label of postal code
        label_postal_code = tk.Label(self, text="Please enter a postal code:", font=("Verdana", 15))
        label_postal_code.grid(row=1, column=0, padx=10, pady=10,  sticky="W")

        # label of radius
        label_radius = tk.Label(self, text="Please enter a radius:", font=("Verdana", 15))
        label_radius.grid(row=2, column=0, padx=10, pady=10,  sticky="W")

        # entry field of postal code
        input_postal_code = tk.Entry(self, textvariable=tk.StringVar())
        input_postal_code.grid(row=1, column=1, padx=10, pady=10,  sticky="W")

        # entry field of radius (dropdown)
        radius_type = tk.IntVar()
        radius_type.set(radius_lists[0])
        input_radius = tk.OptionMenu(self, radius_type, *radius_lists)
        input_radius.grid(row=2, column=1, padx=10, pady=10,  sticky="W")

        # input parameters
        params = {
            "input_postal_code": input_postal_code, 
            "input_radius": radius_type
        }

        # search button to execute insertion and navigate to add appliance page
        search_button = tk.Button(self, text="Search", command=lambda: self.search_radius_execute_command(params))
        search_button.grid(row=8, column=2, padx=10, pady=10)

        # back button to the reports page
        from view_reports_page import ViewReports
        back_button = tk.Button(self, text="Return to View Reports", command=lambda: controller.show_frame(ViewReports))
        back_button.grid(row=8, column=1, padx=10, pady=10)

    def search_radius_execute_command(self,params):
        # search radius params: {'input_postal_code': ..., 'input_radius': ...}
        radius = params['input_radius'].get()
        postal_code = params['input_postal_code'].get()

        print("radius::", radius)
        print("postal_code::", postal_code)

        # Validate inputs
        validation_1 = validate_postal_code(postal_code)

        query = SQL_QUERY_1.format(postal_code=postal_code, radius=radius)
        cursor.execute(query)
        result = cursor.fetchall()
        num_rows = len(result)


        # TODO: Search backend via mysql
        if validation_1 is not False:

            print(result)
            print(len(result))
            child = tk.Toplevel(self.parent)
            # child.geometry('1000x1000')
            pc_label = tk.Label(child, text="Postal Code", font=("Verdana", 10))
            pc_label.grid(row=0, column=0, sticky="W")
            pc_label = tk.Label(child, text=postal_code, font=("Verdana", 10))
            pc_label.grid(row=0, column=1,  sticky="W")
            radius_label = tk.Label(child, text="Radius", font=("Verdana", 10))
            radius_label.grid(row=1, column=0,  sticky="W")
            radius_label = tk.Label(child, text=radius, font=("Verdana", 10))
            radius_label.grid(row=1, column=1,  sticky="W")
            if num_rows == 0:
                radius_label = tk.Label(child, text="No Results", font=("Verdana", 10))
                radius_label.grid(row=2, column=0,  sticky="W")
            else:
                total_house_count = 0
                for r in range(num_rows):
                    total_house_count += result[r][1]

                total_household_count_label = tk.Label(child, text="Total Household Count", font=("Verdana", 10))
                total_household_count_label.grid(row=2, column=0,  sticky="W")

                total_household_count_label = tk.Label(child, text=total_house_count, font=("Verdana", 10))
                total_household_count_label.grid(row=2, column=1,  sticky="W")

                d_label = tk.Label(child, text='Apartment', font=("Verdana", 10))
                d_label.grid(row=3, column=1,  sticky="W")
                d_label = tk.Label(child, text='Condominium', font=("Verdana", 10))
                d_label.grid(row=3, column=2,  sticky="W")
                d_label = tk.Label(child, text='House', font=("Verdana", 10))
                d_label.grid(row=3, column=3,  sticky="W")
                d_label = tk.Label(child, text='Mobile Home', font=("Verdana", 10))
                d_label.grid(row=3, column=4,  sticky="W")
                d_label = tk.Label(child, text='Townhome', font=("Verdana", 10))
                d_label.grid(row=3, column=5,  sticky="W")

                apartment_v = 0
                condo_v = 0
                house_v = 0
                mobile_v = 0
                townhome_v = 0
                for r in range(num_rows):
                    if result[r][0] == 'apartment':
                        apartment_v += result[r][1]
                    elif result[r][0] == 'condominium':
                        condo_v += result[r][1]
                    elif result[r][0] == 'house':
                        house_v += result[r][1]
                    elif result[r][0] == 'mobile home':
                        mobile_v += result[r][1]
                    else:
                        townhome_v += result[r][1]

                d_label = tk.Label(child, text="count for each household", font=("Verdana", 10))
                d_label.grid(row=4, column=0,  sticky="W")
                d_label = tk.Label(child, text=apartment_v, font=("Verdana", 10))
                d_label.grid(row=4, column=1,  sticky="W")
                d_label = tk.Label(child, text=condo_v, font=("Verdana", 10))
                d_label.grid(row=4, column=2,  sticky="W")
                d_label = tk.Label(child, text=house_v, font=("Verdana", 10))
                d_label.grid(row=4, column=3,  sticky="W")
                d_label = tk.Label(child, text=mobile_v, font=("Verdana", 10))
                d_label.grid(row=4, column=4,  sticky="W")
                d_label = tk.Label(child, text=townhome_v, font=("Verdana", 10))
                d_label.grid(row=4, column=5,  sticky="W")

                apartment_v = 0
                condo_v = 0
                house_v = 0
                mobile_v = 0
                townhome_v = 0

                for r in range(num_rows):
                    if result[r][0] == 'apartment':
                        apartment_v += result[r][7]
                    elif result[r][0] == 'condominium':
                        condo_v += result[r][7]
                    elif result[r][0] == 'house':
                        house_v += result[r][7]
                    elif result[r][0] == 'mobile home':
                        mobile_v += result[r][7]
                    else:
                        townhome_v += result[r][7]
                d_label = tk.Label(child, text="Average Square Footage", font=("Verdana", 10))
                d_label.grid(row=5, column=0,  sticky="W")
                d_label = tk.Label(child, text=apartment_v, font=("Verdana", 10))
                d_label.grid(row=5, column=1,  sticky="W")
                d_label = tk.Label(child, text=condo_v, font=("Verdana", 10))
                d_label.grid(row=5, column=2,  sticky="W")
                d_label = tk.Label(child, text=house_v, font=("Verdana", 10))
                d_label.grid(row=5, column=3,  sticky="W")
                d_label = tk.Label(child, text=mobile_v, font=("Verdana", 10))
                d_label.grid(row=5, column=4,  sticky="W")
                d_label = tk.Label(child, text=townhome_v, font=("Verdana", 10))
                d_label.grid(row=5, column=5,  sticky="W")

                apartment_v = 0
                condo_v = 0
                house_v = 0
                mobile_v = 0
                townhome_v = 0

                for r in range(num_rows):
                    if result[r][0] == 'apartment':
                        apartment_v += result[r][8]
                    elif result[r][0] == 'condominium':
                        condo_v += result[r][8]
                    elif result[r][0] == 'house':
                        house_v += result[r][8]
                    elif result[r][0] == 'mobile home':
                        mobile_v += result[r][8]
                    else:
                        townhome_v += result[r][8]
                d_label = tk.Label(child, text="Average Heating", font=("Verdana", 10))
                d_label.grid(row=6, column=0,  sticky="W")
                d_label = tk.Label(child, text=apartment_v, font=("Verdana", 10))
                d_label.grid(row=6, column=1,  sticky="W")
                d_label = tk.Label(child, text=condo_v, font=("Verdana", 10))
                d_label.grid(row=6, column=2,  sticky="W")
                d_label = tk.Label(child, text=house_v, font=("Verdana", 10))
                d_label.grid(row=6, column=3,  sticky="W")
                d_label = tk.Label(child, text=mobile_v, font=("Verdana", 10))
                d_label.grid(row=6, column=4,  sticky="W")
                d_label = tk.Label(child, text=townhome_v, font=("Verdana", 10))
                d_label.grid(row=6, column=5,  sticky="W")

                apartment_v = 0
                condo_v = 0
                house_v = 0
                mobile_v = 0
                townhome_v = 0

                for r in range(num_rows):
                    if result[r][0] == 'apartment':
                        apartment_v += result[r][9]
                    elif result[r][0] == 'condominium':
                        condo_v += result[r][9]
                    elif result[r][0] == 'house':
                        house_v += result[r][9]
                    elif result[r][0] == 'mobile home':
                        mobile_v += result[r][9]
                    else:
                        townhome_v += result[r][9]
                d_label = tk.Label(child, text="Average Cooling", font=("Verdana", 10))
                d_label.grid(row=7, column=0,  sticky="W")
                d_label = tk.Label(child, text=apartment_v, font=("Verdana", 10))
                d_label.grid(row=7, column=1,  sticky="W")
                d_label = tk.Label(child, text=condo_v, font=("Verdana", 10))
                d_label.grid(row=7, column=2,  sticky="W")
                d_label = tk.Label(child, text=house_v, font=("Verdana", 10))
                d_label.grid(row=7, column=3,  sticky="W")
                d_label = tk.Label(child, text=mobile_v, font=("Verdana", 10))
                d_label.grid(row=7, column=4,  sticky="W")
                d_label = tk.Label(child, text=townhome_v, font=("Verdana", 10))
                d_label.grid(row=7, column=5,  sticky="W")

                def trimming(words):
                    return ','.join(set(words.split(',')))


                apartment_v = 0
                condo_v = 0
                house_v = 0
                mobile_v = 0
                townhome_v = 0
                for r in range(num_rows):
                    if result[r][0] == 'apartment':
                        apartment_v = trimming(result[r][10])
                    elif result[r][0] == 'condominium':
                        condo_v = trimming(result[r][10])
                    elif result[r][0] == 'house':
                        house_v = trimming(result[r][10])
                    elif result[r][0] == 'mobile home':
                        mobile_v = trimming(result[r][10])
                    else:
                        townhome_v = trimming(result[r][10])
                d_label = tk.Label(child, text="Public Utilities Used", font=("Verdana", 10))
                d_label.grid(row=8, column=0,  sticky="W")
                d_label = tk.Label(child, text=apartment_v, font=("Verdana", 10))
                d_label.grid(row=8, column=1,  sticky="W")
                d_label = tk.Label(child, text=condo_v, font=("Verdana", 10))
                d_label.grid(row=8, column=2,  sticky="W")
                d_label = tk.Label(child, text=house_v, font=("Verdana", 10))
                d_label.grid(row=8, column=3,  sticky="W")
                d_label = tk.Label(child, text=mobile_v, font=("Verdana", 10))
                d_label.grid(row=8, column=4,  sticky="W")
                d_label = tk.Label(child, text=townhome_v, font=("Verdana", 10))
                d_label.grid(row=8, column=5,  sticky="W")

                apartment_v = 0
                condo_v = 0
                house_v = 0
                mobile_v = 0
                townhome_v = 0
                for r in range(num_rows):
                    if result[r][0] == 'apartment':
                        apartment_v += result[r][11]
                    elif result[r][0] == 'condominium':
                        condo_v += result[r][11]
                    elif result[r][0] == 'house':
                        house_v += result[r][11]
                    elif result[r][0] == 'mobile home':
                        mobile_v += result[r][11]
                    else:
                        townhome_v += result[r][11]
                d_label = tk.Label(child, text="Count of off-the-grid homes", font=("Verdana", 10))
                d_label.grid(row=9, column=0,  sticky="W")
                d_label = tk.Label(child, text=apartment_v, font=("Verdana", 10))
                d_label.grid(row=9, column=1,  sticky="W")
                d_label = tk.Label(child, text=condo_v, font=("Verdana", 10))
                d_label.grid(row=9, column=2,  sticky="W")
                d_label = tk.Label(child, text=house_v, font=("Verdana", 10))
                d_label.grid(row=9, column=3,  sticky="W")
                d_label = tk.Label(child, text=mobile_v, font=("Verdana", 10))
                d_label.grid(row=9, column=4,  sticky="W")
                d_label = tk.Label(child, text=townhome_v, font=("Verdana", 10))
                d_label.grid(row=9, column=5,  sticky="W")

                apartment_v = 0
                condo_v = 0
                house_v = 0
                mobile_v = 0
                townhome_v = 0
                for r in range(num_rows):
                    if result[r][0] == 'apartment':
                        apartment_v += result[r][12]
                    elif result[r][0] == 'condominium':
                        condo_v += result[r][12]
                    elif result[r][0] == 'house':
                        house_v += result[r][12]
                    elif result[r][0] == 'mobile home':
                        mobile_v += result[r][12]
                    else:
                        townhome_v += result[r][12]
                d_label = tk.Label(child, text="Count of homes with power generation", font=("Verdana", 10))
                d_label.grid(row=10, column=0,  sticky="W")
                d_label = tk.Label(child, text=apartment_v, font=("Verdana", 10))
                d_label.grid(row=10, column=1,  sticky="W")
                d_label = tk.Label(child, text=condo_v, font=("Verdana", 10))
                d_label.grid(row=10, column=2,  sticky="W")
                d_label = tk.Label(child, text=house_v, font=("Verdana", 10))
                d_label.grid(row=10, column=3,  sticky="W")
                d_label = tk.Label(child, text=mobile_v, font=("Verdana", 10))
                d_label.grid(row=10, column=4,  sticky="W")
                d_label = tk.Label(child, text=townhome_v, font=("Verdana", 10))
                d_label.grid(row=10, column=5,  sticky="W")

                apartment_v = 0
                condo_v = 0
                house_v = 0
                mobile_v = 0
                townhome_v = 0
                for r in range(num_rows):
                    if result[r][0] == 'apartment':
                        apartment_v = result[r][13]
                    elif result[r][0] == 'condominium':
                        condo_v = result[r][13]
                    elif result[r][0] == 'house':
                        house_v = result[r][13]
                    elif result[r][0] == 'mobile home':
                        mobile_v = result[r][13]
                    else:
                        townhome_v = result[r][13]
                d_label = tk.Label(child, text="Most common generation method", font=("Verdana", 10))
                d_label.grid(row=11, column=0,  sticky="W")
                d_label = tk.Label(child, text=apartment_v, font=("Verdana", 10))
                d_label.grid(row=11, column=1,  sticky="W")
                d_label = tk.Label(child, text=condo_v, font=("Verdana", 10))
                d_label.grid(row=11, column=2,  sticky="W")
                d_label = tk.Label(child, text=house_v, font=("Verdana", 10))
                d_label.grid(row=11, column=3,  sticky="W")
                d_label = tk.Label(child, text=mobile_v, font=("Verdana", 10))
                d_label.grid(row=11, column=4,  sticky="W")
                d_label = tk.Label(child, text=townhome_v, font=("Verdana", 10))
                d_label.grid(row=11, column=5,  sticky="W")

                apartment_v = 0
                condo_v = 0
                house_v = 0
                mobile_v = 0
                townhome_v = 0
                for r in range(num_rows):
                    if result[r][0] == 'apartment':
                        apartment_v += result[r][14]
                    elif result[r][0] == 'condominium':
                        condo_v += result[r][14]
                    elif result[r][0] == 'house':
                        house_v += result[r][14]
                    elif result[r][0] == 'mobile home':
                        mobile_v += result[r][14]
                    else:
                        townhome_v += result[r][14]
                d_label = tk.Label(child, text="Avg Monthly power generation", font=("Verdana", 10))
                d_label.grid(row=12, column=0,  sticky="W")
                d_label = tk.Label(child, text=apartment_v, font=("Verdana", 10))
                d_label.grid(row=12, column=1,  sticky="W")
                d_label = tk.Label(child, text=condo_v, font=("Verdana", 10))
                d_label.grid(row=12, column=2,  sticky="W")
                d_label = tk.Label(child, text=house_v, font=("Verdana", 10))
                d_label.grid(row=12, column=3,  sticky="W")
                d_label = tk.Label(child, text=mobile_v, font=("Verdana", 10))
                d_label.grid(row=12, column=4,  sticky="W")
                d_label = tk.Label(child, text=townhome_v, font=("Verdana", 10))
                d_label.grid(row=12, column=5,  sticky="W")

                apartment_v = 0
                condo_v = 0
                house_v = 0
                mobile_v = 0
                townhome_v = 0
                for r in range(num_rows):
                    if result[r][0] == 'apartment':
                        apartment_v += result[r][15]
                    elif result[r][0] == 'condominium':
                        condo_v += result[r][15]
                    elif result[r][0] == 'house':
                        house_v += result[r][15]
                    elif result[r][0] == 'mobile home':
                        mobile_v += result[r][15]
                    else:
                        townhome_v += result[r][15]
                d_label = tk.Label(child, text="Avg Monthly power generation", font=("Verdana", 10))
                d_label.grid(row=13, column=0,  sticky="W")
                d_label = tk.Label(child, text=apartment_v, font=("Verdana", 10))
                d_label.grid(row=13, column=1,  sticky="W")
                d_label = tk.Label(child, text=condo_v, font=("Verdana", 10))
                d_label.grid(row=13, column=2,  sticky="W")
                d_label = tk.Label(child, text=house_v, font=("Verdana", 10))
                d_label.grid(row=13, column=3,  sticky="W")
                d_label = tk.Label(child, text=mobile_v, font=("Verdana", 10))
                d_label.grid(row=13, column=4, sticky="W")
                d_label = tk.Label(child, text=townhome_v, font=("Verdana", 10))
                d_label.grid(row=13, column=5, sticky="W")






# [('apartment', 37, Decimal('0'), Decimal('37'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('1022'), Decimal('71.9'), Decimal('72.9'), 'electric,electric,fuel oil,electric,gas,electric,gas,fuel oil,electric,gas,steam,electric,steam,fuel oil,gas,off-the-grid,steam,steam,fuel oil', Decimal('5'), Decimal('18'), 'solar-electric', Decimal('82'), Decimal('11')),
# ('condominium', 8, Decimal('0'), Decimal('0'), Decimal('0'), Decimal('8'), Decimal('0'), Decimal('1181'), Decimal('69.3'), Decimal('71.8'), 'electric,electric,gas,electric,steam,fuel oil,gas', Decimal('0'), Decimal('5'), 'solar-electric', Decimal('82'), Decimal('2')),
# ('house', 35, Decimal('35'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('1504'), Decimal('72.8'), Decimal('72.7'), 'electric,electric,fuel oil,electric,gas,electric,steam,fuel oil,gas,gas,fuel oil,gas,steam,off-the-grid,steam', Decimal('8'), Decimal('16'), 'solar-electric', Decimal('61'), Decimal('9')),
# ('mobile home', 6, Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('6'), Decimal('285'), Decimal('70.4'), Decimal('72.3'), 'electric,electric,fuel oil,electric,gas,gas,fuel oil,off-the-grid', Decimal('2'), Decimal('4'), 'solar-electric', Decimal('71'), Decimal('3')),
# ('townhome', 19, Decimal('0'), Decimal('0'), Decimal('19'), Decimal('0'), Decimal('0'), Decimal('1149'), Decimal('71.9'), Decimal('72.9'), 'electric,electric,fuel oil,electric,gas,electric,gas,fuel oil,electric,steam,gas,gas,fuel oil,off-the-grid,steam', Decimal('7'), Decimal('10'), 'solar-electric', Decimal('89'), Decimal('7'))]