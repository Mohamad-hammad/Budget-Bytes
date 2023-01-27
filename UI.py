import tkinter
from backend import *
import backend
import customtkinter
import matplotlib, numpy, sys
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
customtkinter.set_appearance_mode("dark")
class App(customtkinter.CTk):
    def __init__(self,currentBalance):
        super().__init__()
        self.title("Budget Bytes")
        self.geometry("1100x700")

        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)
        self.grid_rowconfigure(2,weight=1)
        self.grid_rowconfigure(3,weight=1)
        self.grid_rowconfigure(4,weight=1)
        self.grid_rowconfigure(5,weight=1)
        self.grid_rowconfigure(6,weight=1)
        self.grid_rowconfigure(7,weight=1)
        self.grid_rowconfigure(8,weight=1)
        #fonts

        #balance label
        font_balance = customtkinter.CTkFont(family="Poppins Regular", size=15)
        label_balance = customtkinter.CTkLabel(master=self, text="Balance",anchor="w",font = font_balance)
        label_balance.grid(row=0, column=0,padx=20, sticky="nw")

        #total balance
        font_totalBalance = customtkinter.CTkFont(family="Poppins Bold", size=25)
        label_totalBalance = customtkinter.CTkLabel(master=self, text="Rs."+str(f"{currentBalance:,}"),font = font_totalBalance)
        label_totalBalance.grid(row=0, column=0,padx=20,pady=20,sticky="nw")

        #barchart
        """
        f = Figure(figsize=(5,4), dpi=100)
        f.set_facecolor("black")
        ax = f.add_subplot(111)

        data = (20, 35, 30, 35, 27,1,1,1)

        ind = numpy.arange(8)  # the x locations for the groups
        width = .5

        rects1 = ax.bar(ind, data, width) 
        ax.set_facecolor("black")
        """
        canvas = FigureCanvasTkAgg(drawBarChart(), master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=2, column=0,columnspan=1,padx=20, sticky="nw")

        #loan label
        font_loan = customtkinter.CTkFont(family="Poppins Bold", size=20)
        label_loan = customtkinter.CTkLabel(master=self, text="Loan",anchor="w",font = font_loan)
        label_loan.grid(row=3, column=0,padx=20, sticky="nw")

        #loan to be paid label
        font_tobePaid= customtkinter.CTkFont(family="Poppins Regular", size=15)
        label_tobePaid = customtkinter.CTkLabel(master=self, text="To Be Payed",anchor="w",font = font_tobePaid)
        label_tobePaid.grid(row=4, column=0,padx=20, sticky="nw")

        #total loabn
        font_totalLoan = customtkinter.CTkFont(family="Poppins Bold", size=20)
        label_totalLoan = customtkinter.CTkLabel(master=self, text="Rs. 11,500",font = font_totalLoan)
        label_totalLoan.grid(row=4, column=0,padx=20,pady=20,sticky="nw")


        #loan to be received label
        font_tobePaid= customtkinter.CTkFont(family="Poppins Regular", size=15)
        label_tobePaid = customtkinter.CTkLabel(master=self, text="To Recieve",anchor="w",font = font_tobePaid)
        label_tobePaid.grid(row=4, column=0,padx=200,sticky="nw")

        #total loabn
        font_totalLoan = customtkinter.CTkFont(family="Poppins Bold", size=20)
        label_totalLoan = customtkinter.CTkLabel(master=self, text="Rs. 11,500",font = font_totalLoan)
        label_totalLoan.grid(row=4, column=0,padx=200,pady=20,sticky="nw")

        #Monthly expense limit
        font_expenseLimit= customtkinter.CTkFont(family="Poppins Regular", size=15)
        label_expenseLimit = customtkinter.CTkLabel(master=self, text="Monthly Expense Limit:",anchor="nw",font = font_expenseLimit)
        label_expenseLimit.grid(row=2, column=1, sticky="nw")

        #mothly expense limit amount label
        font_expenseLimitAmount= customtkinter.CTkFont(family="Poppins Bold", size=20)
        label_expenseLimitAmount = customtkinter.CTkLabel(master=self, text="Rs."+str(getMonthlyExpenseLimit()),anchor="w",font = font_expenseLimitAmount)
        label_expenseLimitAmount.grid(row=2, column=1,pady=20, sticky="nw")

        #This month's expenses
        font_thisMonthLimit= customtkinter.CTkFont(family="Poppins Regular", size=15)
        label_thisMonthLimit = customtkinter.CTkLabel(master=self, text="This Month's Expenses:",anchor="nw",font = font_thisMonthLimit)
        label_thisMonthLimit.grid(row=2, column=1,pady=60, sticky="nw")

        #This month's expenses
        font_thisMonthLimitAmount= customtkinter.CTkFont(family="Poppins Bold", size=20)
        label_thisMonthLimitAmoun = customtkinter.CTkLabel(master=self, text="Rs."+str(currentMonthExpenses()),anchor="w",font = font_thisMonthLimitAmount)
        label_thisMonthLimitAmoun.grid(row=2, column=1,pady=80, sticky="nw")

        #Cash flow for december label
        font_cashflowLabel= customtkinter.CTkFont(family="Poppins Regular", size=15)
        label_cashflowLabe = customtkinter.CTkLabel(master=self, text="Cash flow for December",anchor="w",font = font_cashflowLabel)
        label_cashflowLabe.grid(row=4, column=1, sticky="nw")

        #Earned label
        font_earnedLabel= customtkinter.CTkFont(family="Poppins Regular", size=10)
        label_earnedLabel = customtkinter.CTkLabel(master=self, text="EARNED",anchor="w",font = font_earnedLabel)
        label_earnedLabel.grid(row=4, column=1,pady=20, sticky="nw")

        #Earned amount label
        font_amountEarned= customtkinter.CTkFont(family="Poppins Bold", size=10)
        label_amountEarned = customtkinter.CTkLabel(master=self, text="Rs."+str(currentMonthEarning()),anchor="w",font = font_amountEarned)
        label_amountEarned.grid(row=4, column=1,padx=150,pady=20, sticky="nw")

        #progess bar
        progressbar = customtkinter.CTkProgressBar(master=self)
        progressbar.grid(row=4, column=1,pady=40,sticky="nw")

        #SPENT label
        font_spentLabel= customtkinter.CTkFont(family="Poppins Regular", size=10)
        label_spentLabel = customtkinter.CTkLabel(master=self, text="SPENT",anchor="w",font = font_spentLabel)
        label_spentLabel.grid(row=4, column=1,pady=60, sticky="nw")

        #SPENT amount label
        font_spentAmount= customtkinter.CTkFont(family="Poppins Bold", size=10)
        label_spentAmount = customtkinter.CTkLabel(master=self, text="Rs."+str(currentMonthExpenses()),anchor="w",font = font_spentAmount)
        label_spentAmount.grid(row=4, column=1,padx=150,pady=60, sticky="nw")

        #progess bar
        progressbar = customtkinter.CTkProgressBar(master=self)
        progressbar.grid(row=4, column=1,pady=80,sticky="nw")

        #Remaining cashflow amount label
        font_remainingAmount= customtkinter.CTkFont(family="Poppins Bold", size=20)
        label_remainingAmount = customtkinter.CTkLabel(master=self, text="Rs."+str(currentMonthEarning()-currentMonthExpenses()),anchor="w",font = font_remainingAmount)
        label_remainingAmount.grid(row=4, column=1,padx=210,pady=45, sticky="nw")

        #Remaning label
        font_remainingLabel= customtkinter.CTkFont(family="Poppins Regular", size=10)
        label_remaining = customtkinter.CTkLabel(master=self, text="REMAINING",anchor="w",font = font_remainingLabel)
        label_remaining.grid(row=4, column=1,pady=70,padx=210, sticky="nw")

if __name__ == "__main__":

    AllTransactions=loadData()
    printData()
    app = App(round(AllTransactions[len(AllTransactions)-1].availableBalance))
    app.mainloop()
