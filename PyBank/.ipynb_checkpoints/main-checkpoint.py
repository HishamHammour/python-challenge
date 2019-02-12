{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Financail Analysis\n",
      "\n",
      "==================\n",
      "Total Months: 86 \n",
      "Total: $38382578\n",
      "Average Change: $7803.476744186047  \n",
      "Greatest Increase in Profits:Feb-2012 ($1926159)\n",
      "Greatest Decrease in Losses: Sep-2013 ($-2196167)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Import the modules\n",
    "import csv\n",
    "import os\n",
    "\n",
    "\n",
    "# assigne the file path to open \n",
    "#/UTAUS201901DATA3/homework-instructions/03-Python/Instructions/PyBank/Resources/budget_data.csv\n",
    "#/Users/hishamhammour/Desktop/UTAUS201901DATA3/UTAUS201901DATA3/homework-instructions/03-Python/ExtraContent/Instructions/PyBoss/employee_data.csv\n",
    "open_file_path = \"Resources/budget_data.csv\"\n",
    "\n",
    "output_file = \"budget_data_summery.txt\"\n",
    "\n",
    "\n",
    "\n",
    "''' # Variables and counters ...\n",
    "The total number of month \n",
    "The total amount of profit/loss >> total revenue(+/-)\n",
    "The Average changes in profit/loss\n",
    "The greatest increase profits (date and amount)\n",
    "The greates decrease in losses (date and amount)\n",
    "\n",
    "'''\n",
    "total_number_of_months = 0\n",
    "greatest_profit_increase = [\"\",0]\n",
    "greatest_losses_decrease = [\"\",10000000000000000]\n",
    "month_of_change = []\n",
    "\n",
    " \n",
    "months_total = 0\n",
    "total_PL = 0\n",
    "current_PL_total = 0\n",
    "changes_in_PL = []\n",
    "PL_change_list =[]\n",
    "\n",
    "\n",
    "#load the file into list of dictionaries\n",
    "with open(open_file_path) as budget_data:\n",
    "    csvreader = csv.DictReader(budget_data)\n",
    "\n",
    "    for anyline in csvreader:\n",
    "\n",
    "        total_number_of_months +=1 # total number of months\n",
    "        total_PL = total_PL+ int(anyline[\"Profit/Losses\"]) #total Profit and Losses +/-\n",
    "\n",
    "\n",
    "        changes_in_PL = int(anyline[\"Profit/Losses\"]) - current_PL_total\n",
    "        current_PL_total =int(anyline[\"Profit/Losses\"])\n",
    "        PL_change_list = PL_change_list + [changes_in_PL]\n",
    "        month_of_change = month_of_change + [anyline[\"Date\"]]\n",
    "\n",
    "\n",
    "        # Greatest increase calculation\n",
    "        if (changes_in_PL > greatest_profit_increase[1]):\n",
    "            greatest_profit_increase[0] = anyline[\"Date\"]\n",
    "            greatest_profit_increase[1] = changes_in_PL\n",
    "\n",
    "        # Greatest decrease \n",
    "        if (changes_in_PL < greatest_losses_decrease[1]):\n",
    "            greatest_losses_decrease[0] = anyline[\"Date\"]\n",
    "            greatest_losses_decrease[1] = changes_in_PL\n",
    "\n",
    "# Calculating the Average change in PL\n",
    "PL_avg_change = sum(PL_change_list) / len(PL_change_list)\n",
    "\n",
    "\n",
    "#Summery output\n",
    "\n",
    "Summery = (f\"\\nFinancail Analysis\\n\"\n",
    "           f\"\\n==================\\n\"\n",
    "           f\"Total Months: {total_number_of_months} \\n\" \n",
    "           f\"Total: ${total_PL}\\n\"\n",
    "           f\"Average Change: ${PL_avg_change}  \\n\"\n",
    "           f\"Greatest Increase in Profits:{greatest_profit_increase[0]} (${greatest_profit_increase[1]})\\n\"\n",
    "           f\"Greatest Decrease in Losses: {greatest_losses_decrease[0]} (${greatest_losses_decrease[1]})\\n\")\n",
    "\n",
    "print(Summery)\n",
    "\n",
    "#Exporting to text file\n",
    "with open(output_file, \"w\") as text_file:\n",
    "    text_file.write(Summery)\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python3 (PythonData)",
   "language": "python",
   "name": "pythondata"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
