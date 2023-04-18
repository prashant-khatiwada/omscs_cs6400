import tkinter as tk
from report_1 import Report1
from report_2 import Report2
from report_3 import Report3
from report_4 import Report4
from report_5 import Report5
from report_6 import Report6

# view reports page window frame
class ViewReports(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="View Reports", font=("Verdana", 25))
        label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        report1_button = tk.Button(self, text="Report 1", command=lambda: controller.show_frame(Report1))
        report1_button.grid(row=1, column=0, padx=10, pady=10)

        report2_button = tk.Button(self, text="Report 2", command=lambda: controller.show_frame(Report2))
        report2_button.grid(row=2, column=0, padx=10, pady=10)

        report3_button = tk.Button(self, text="Report 3", command=lambda: controller.show_frame(Report3))
        report3_button.grid(row=3, column=0, padx=10, pady=10)

        report4_button = tk.Button(self, text="Report 4", command=lambda: controller.show_frame(Report4))
        report4_button.grid(row=4, column=0, padx=10, pady=10)

        report5_button = tk.Button(self, text="Report 5", command=lambda: controller.show_frame(Report5))
        report5_button.grid(row=5, column=0, padx=10, pady=10)

        report6_button = tk.Button(self, text="Report 6", command=lambda: controller.show_frame(Report6))
        report6_button.grid(row=6, column=0, padx=10, pady=10)

        # importing main page here resolves circular import issue
        from main_page import MainPage
        main_page_button = tk.Button(self, text="Return to the main menu", command=lambda: controller.show_frame(MainPage))
        main_page_button.grid(row=7, column=0, padx=10, pady=10)