import os


import csv

csvpath = os.path.join( 'budget_data.csv')


tot_p = []
date = []
monthly_change_list = []
previous_value =0
count = 0
tot_value = 0
change = 0
average_change = 0
sum_change = 0
great_increase = 0
great_decrease = 0
date_max_increase = 0
date_max_decrease = 0



with open(csvpath) as csvfile:

    
    csvreader = csv.reader(csvfile, delimiter =',')

    
    csv_header = next(csvreader)

    
    Jan_data = next (csvreader)
    count = count+1 
    tot_value = tot_value + int(Jan_data[1])
    previous_value = int(Jan_data[1])

    
    for row in csvreader:
       
        date.append(row[0])

        
        tot_p.append(row[1])

        count = count + 1
        tot_value = tot_value + int(row[1])

        change =int(row[1]) - previous_value
        previous_value = int(row[1])
       
        monthly_change_list.append(change)

    average_change = round(sum(monthly_change_list)/len(monthly_change_list),2)

    print ("                               ")    
    print ("Financial Analysis")

    print ("-------------------------------")         
    
    print ("Total Months = " + str(count))
    print ("Total_profit/loss = $ " + str(tot_value))   
    

    print ("Averange Monthly Change = $ " + str(average_change))

    
    max (monthly_change_list)
    grgreat_increase =eat_decrease = min (monthly_change_list)
    date_max_increase = date[monthly_change_list.index(great_increase)]
    date_max_decrease = date[monthly_change_list.index(great_decrease)]
    print ("The Greatest Increase = $ " + str(great_increase) + " on " + date_max_increase)
    print ("The Greatest Decrease = $ " + str(great_decrease) + " on " + date_max_decrease)
    print ("----------------------------------")

    PyBank_analysis = os.path.join("analysis", "PyBank_analysis.txt")


    with open (PyBank_analysis , "w") as text:
        text.write("                               \n")
        text.write("Financial Analysis\n")
        text.write("-------------------------------\n")
        text.write("Total Months = " + str(count) + "\n")
        text.write("Total_profit/loss = $ " + str(tot_value) + "\n") 
        text.write("Averange Monthly Change = $ " + str(average_change) + "\n")
        text.write("The Greatest Increase  = $ " + str(great_increase) + " on " + date_max_increase + "\n")
        text.write("The Greatest Decrease = $ " + str(great_decrease) + " on " + date_max_decrease + "\n")
        text.write("-------------------------------\n")