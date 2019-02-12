# Import the modules
import csv

# assigne the file path to open 
#/UTAUS201901DATA3/homework-instructions/03-Python/Instructions/PyBank/Resources/budget_data.csv
#/Users/hishamhammour/Desktop/UTAUS201901DATA3/UTAUS201901DATA3/homework-instructions/03-Python/ExtraContent/Instructions/PyBoss/employee_data.csv
open_file_path = "Resources/budget_data.csv"

output_file = "budget_data_summery.txt"



''' # Variables and counters ...
The total number of month 
The total amount of profit/loss >> total revenue(+/-)
The Average changes in profit/loss
The greatest increase profits (date and amount)
The greates decrease in losses (date and amount)

'''
total_number_of_months = 0
greatest_profit_increase = ["",0]
greatest_losses_decrease = ["",10000000000000000]
month_of_change = []

 
months_total = 0
total_PL = 0
current_PL_total = 0
changes_in_PL = []
PL_change_list =[]


#load the file into list of dictionaries
with open(open_file_path) as budget_data:
    csvreader = csv.DictReader(budget_data)

    for anyline in csvreader:

        total_number_of_months +=1 # total number of months
        total_PL = total_PL+ int(anyline["Profit/Losses"]) #total Profit and Losses +/-


        changes_in_PL = int(anyline["Profit/Losses"]) - current_PL_total
        current_PL_total =int(anyline["Profit/Losses"])
        PL_change_list = PL_change_list + [changes_in_PL]
        month_of_change = month_of_change + [anyline["Date"]]


        # Greatest increase calculation
        if (changes_in_PL > greatest_profit_increase[1]):
            greatest_profit_increase[0] = anyline["Date"]
            greatest_profit_increase[1] = changes_in_PL

        # Greatest decrease 
        if (changes_in_PL < greatest_losses_decrease[1]):
            greatest_losses_decrease[0] = anyline["Date"]
            greatest_losses_decrease[1] = changes_in_PL

# Calculating the Average change in PL
PL_avg_change = sum(PL_change_list) / len(PL_change_list)


#Summery output

Summery = (f"\nFinancail Analysis\n"
           f"\n==================\n"
           f"Total Months: {total_number_of_months} \n" 
           f"Total: ${total_PL}\n"
           f"Average Change: ${PL_avg_change}  \n"
           f"Greatest Increase in Profits:{greatest_profit_increase[0]} (${greatest_profit_increase[1]})\n"
           f"Greatest Decrease in Losses: {greatest_losses_decrease[0]} (${greatest_losses_decrease[1]})\n")

print(Summery)

#Exporting to text file
with open(output_file, "w") as text_file:
    text_file.write(Summery)







