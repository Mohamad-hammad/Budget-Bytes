import tkinter

import customtkinter
import matplotlib, numpy, sys
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
customtkinter.set_appearance_mode("dark")

root = customtkinter.CTk()
root.title("Budget Bytes")
root.geometry("1000x700")

root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1,weight=1)
root.grid_columnconfigure(2,weight=1)
root.grid_columnconfigure(3,weight=1)
root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1,weight=1)
root.grid_rowconfigure(2,weight=1)
root.grid_rowconfigure(3,weight=1)
root.grid_rowconfigure(4,weight=1)
root.grid_rowconfigure(5,weight=1)
root.grid_rowconfigure(6,weight=1)
root.grid_rowconfigure(7,weight=1)
root.grid_rowconfigure(8,weight=1)
#fonts

#balance label
font_balance = customtkinter.CTkFont(family="Poppins Regular", size=15)
label_balance = customtkinter.CTkLabel(master=root, text="Balance",anchor="w",font = font_balance)
label_balance.grid(row=0, column=0,padx=20, sticky="nw")

#total balance
font_totalBalance = customtkinter.CTkFont(family="Poppins Bold", size=25)
label_totalBalance = customtkinter.CTkLabel(master=root, text="Rs. 11,500",font = font_totalBalance)
label_totalBalance.grid(row=0, column=0,padx=20,pady=20,sticky="nw")

#barchart
f = Figure(figsize=(5,4), dpi=100)
f.set_facecolor("black")
ax = f.add_subplot(111)

data = (20, 35, 30, 35, 27,1,1,1)

ind = numpy.arange(8)  # the x locations for the groups
width = .5

rects1 = ax.bar(ind, data, width)
ax.set_facecolor("black")

canvas = FigureCanvasTkAgg(f, master=root)
canvas.draw()
canvas.get_tk_widget().grid(row=2, column=0,columnspan=1,padx=20, sticky="nw")

#loan label
font_loan = customtkinter.CTkFont(family="Poppins Bold", size=20)
label_loan = customtkinter.CTkLabel(master=root, text="Loan",anchor="w",font = font_loan)
label_loan.grid(row=3, column=0,padx=20, sticky="nw")

#loan to be paid label
font_tobePaid= customtkinter.CTkFont(family="Poppins Regular", size=15)
label_tobePaid = customtkinter.CTkLabel(master=root, text="To Be Payed",anchor="w",font = font_tobePaid)
label_tobePaid.grid(row=4, column=0,padx=20, sticky="nw")

#total loabn
font_totalLoan = customtkinter.CTkFont(family="Poppins Bold", size=20)
label_totalLoan = customtkinter.CTkLabel(master=root, text="Rs. 11,500",font = font_totalLoan)
label_totalLoan.grid(row=4, column=0,padx=20,pady=20,sticky="nw")


#loan to be received label
font_tobePaid= customtkinter.CTkFont(family="Poppins Regular", size=15)
label_tobePaid = customtkinter.CTkLabel(master=root, text="To Recieve",anchor="w",font = font_tobePaid)
label_tobePaid.grid(row=4, column=0,padx=200,sticky="nw")

#total loabn
font_totalLoan = customtkinter.CTkFont(family="Poppins Bold", size=20)
label_totalLoan = customtkinter.CTkLabel(master=root, text="Rs. 11,500",font = font_totalLoan)
label_totalLoan.grid(row=4, column=0,padx=200,pady=20,sticky="nw")

#Monthly expense limit
font_expenseLimit= customtkinter.CTkFont(family="Poppins Regular", size=15)
label_expenseLimit = customtkinter.CTkLabel(master=root, text="Monthly Expense Limit:",anchor="nw",font = font_expenseLimit)
label_expenseLimit.grid(row=2, column=1, sticky="nw")

#mothly expense limit amount label
font_expenseLimitAmount= customtkinter.CTkFont(family="Poppins Bold", size=20)
label_expenseLimitAmount = customtkinter.CTkLabel(master=root, text="Rs.10000",anchor="w",font = font_expenseLimitAmount)
label_expenseLimitAmount.grid(row=2, column=1,pady=20, sticky="nw")

#This month's expenses
font_thisMonthLimit= customtkinter.CTkFont(family="Poppins Regular", size=15)
label_thisMonthLimit = customtkinter.CTkLabel(master=root, text="This Month's Limit:",anchor="nw",font = font_thisMonthLimit)
label_thisMonthLimit.grid(row=2, column=1,pady=60, sticky="nw")

#This month's expenses
font_thisMonthLimitAmount= customtkinter.CTkFont(family="Poppins Bold", size=20)
label_thisMonthLimitAmoun = customtkinter.CTkLabel(master=root, text="Rs.8500",anchor="w",font = font_thisMonthLimitAmount)
label_thisMonthLimitAmoun.grid(row=2, column=1,pady=80, sticky="nw")

#Cash flow for december label
font_cashflowLabel= customtkinter.CTkFont(family="Poppins Regular", size=15)
label_cashflowLabe = customtkinter.CTkLabel(master=root, text="Cash flow for December",anchor="w",font = font_cashflowLabel)
label_cashflowLabe.grid(row=4, column=1, sticky="nw")

#Earned label
font_earnedLabel= customtkinter.CTkFont(family="Poppins Regular", size=10)
label_earnedLabel = customtkinter.CTkLabel(master=root, text="EARNED",anchor="w",font = font_earnedLabel)
label_earnedLabel.grid(row=4, column=1,pady=20, sticky="nw")

#Earned amount label
font_amountEarned= customtkinter.CTkFont(family="Poppins Bold", size=10)
label_amountEarned = customtkinter.CTkLabel(master=root, text="Rs.5000",anchor="w",font = font_amountEarned)
label_amountEarned.grid(row=4, column=1,padx=150,pady=20, sticky="nw")

#progess bar
progressbar = customtkinter.CTkProgressBar(master=root)
progressbar.grid(row=4, column=1,pady=40,sticky="nw")

#SPENT label
font_spentLabel= customtkinter.CTkFont(family="Poppins Regular", size=10)
label_spentLabel = customtkinter.CTkLabel(master=root, text="SPENT",anchor="w",font = font_spentLabel)
label_spentLabel.grid(row=4, column=1,pady=60, sticky="nw")

#SPENT amount label
font_spentAmount= customtkinter.CTkFont(family="Poppins Bold", size=10)
label_spentAmount = customtkinter.CTkLabel(master=root, text="Rs.1500",anchor="w",font = font_spentAmount)
label_spentAmount.grid(row=4, column=1,padx=150,pady=60, sticky="nw")

#progess bar
progressbar = customtkinter.CTkProgressBar(master=root)
progressbar.grid(row=4, column=1,pady=80,sticky="nw")

#Remaining cashflow amount label
font_remainingAmount= customtkinter.CTkFont(family="Poppins Bold", size=20)
label_remainingAmount = customtkinter.CTkLabel(master=root, text="Rs.35000",anchor="w",font = font_remainingAmount)
label_remainingAmount.grid(row=4, column=1,padx=210,pady=45, sticky="nw")

#Remaning label
font_remainingLabel= customtkinter.CTkFont(family="Poppins Regular", size=10)
label_remaining = customtkinter.CTkLabel(master=root, text="REMAINING",anchor="w",font = font_remainingLabel)
label_remaining.grid(row=4, column=1,pady=70,padx=210, sticky="nw")
root.mainloop()
