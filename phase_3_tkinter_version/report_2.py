import tkinter as tk
from tkinter import *
from tkinter import ttk
from db_and_sql_handler import USE_DATABASE_SQL, CONN

cursor = CONN.cursor()
cursor.execute(USE_DATABASE_SQL)

def search_execute_command(params):
    # get input values
    input_search = params["input_search"].get()

    # execute search query
    cursor.execute("SELECT DISTINCT manufacturer_name, model_name FROM Appliance WHERE \
                   LOWER(manufacturer_name) LIKE LOWER(%s) OR LOWER(model_name) LIKE LOWER(%s) ORDER BY \
                   manufacturer_name ASC, model_name ASC", ('%' + input_search + '%', '%' + input_search + '%',))
    query_result = cursor.fetchall()

    # Create an instance of report frame
    win = Tk()

    # report frame title
    win.title("Manufacturer/model search Report")

    # insert column names to index 0 in query result
    query_result.insert(0, ("Manufacturer Name", "Model Name"))

    total_rows = len(query_result)
    total_cols = len(query_result[0])

    # adding values from query results to each cell
    for i in range(0, total_rows):
        for j in range(0, total_cols):
            value = query_result[i][j]
            # if index = 0 in rows, it is column name
            if i == 0:
                cell = tk.Label(win, text=value, width=20, font='Helvetica 15 bold', borderwidth=1, relief="solid")
            else:
                # if value contains search string, cell background must be highlighted to green
                if input_search.lower() in value.lower():
                    cell = tk.Label(win, text=value, width=20, bg='light green', borderwidth=1, relief="solid")
                else:
                    cell = tk.Label(win, text=value, width=20, borderwidth=1, relief="solid")
            cell.grid(row=i, column=j)

    # close report window
    close_button = tk.Button(win, text="Back", command=win.destroy)
    close_button.grid(row=total_rows, column=total_cols-1)

    # display report window
    win.mainloop()


# report 2 window frame
class Report2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Report 2", font=("Verdana", 25))
        label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        # label of email address
        label_email = tk.Label(self, text="Please enter a manufacturer name or model name:", font=("Verdana", 15))
        label_email.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        # entry field of search
        input_search = tk.Entry(self, textvariable=tk.StringVar())
        input_search.grid(row=1, column=1, padx=10, pady=10, sticky="W")

        # get all the input parameters
        params = {
            "input_search": input_search
        }

        search_button = tk.Button(self, text="Search", command=lambda: search_execute_command(params))
        search_button.grid(row=2, column=0, padx=10, pady=10)

        # importing ViewReports here resolves circular import issue
        from view_reports_page import ViewReports
        next_button = tk.Button(self, text="Return to View Reports", command=lambda: controller.show_frame(ViewReports))
        next_button.grid(row=3, column=0, padx=10, pady=10)