import customtkinter
from Backend import*

selected_month = None
root = None
def create_current_month_expenses_frame():
    current_month_frame = customtkinter.CTkFrame(root, corner_radius=0, fg_color="transparent")
    month_frame = customtkinter.CTkLabel(master=current_month_frame, text=selected_month)
    month_frame.grid(row=0, column=0, padx=20)
    

    current_month_frame.grid(row=1, column=0,sticky="nsew")


def select_month_event(month):
    global selected_month
    selected_month= month
    create_current_month_expenses_frame()


def create_expenses_frame(Root):
    global root
    expenses_frame = customtkinter.CTkFrame(Root, corner_radius=0, fg_color="transparent")
    root = expenses_frame
    appearance_mode_menu = customtkinter.CTkOptionMenu(master=expenses_frame,values=get_names_of_all_months(),command=select_month_event)
    appearance_mode_menu.grid(row=0, column=0, padx=20, sticky="s")



    return expenses_frame