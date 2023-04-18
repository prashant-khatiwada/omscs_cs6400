import tkinter as tk

# submission complete page window frame
class SubmissionComplete(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Submission complete!", font=("Verdana", 25))
        label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        self.controller = controller

        # importing main page here resolves circular import issue
        from main_page import MainPage
        #next_button = tk.Button(self, text="Return to the main menu", command=lambda: controller.show_frame(MainPage))
        next_button = tk.Button(self, text="Return to the main menu", command=self.destroy_and_recreate_app)
        next_button.grid(row=1, column=0, padx=10, pady=10)

    def destroy_and_recreate_app(self):
        self.controller.destroy()
        from main import tkinterApp
        app = tkinterApp()
        app.mainloop()

  