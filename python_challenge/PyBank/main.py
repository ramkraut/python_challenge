import osimport csv csvpath=os.path.join("Resources", "budget_data.csv")total_months=0total=0greatest_increase=0greatest_decrease=0with open(csvpath) as csvfile:    csvreader=csv.reader(csvfile)    csv_header = next(csvreader)        for row in csvreader:        total_months=total_months+1         total=total+int(row[1])                if int(row[1])>greatest_increase:            greatest_increase=int(row[1])            date=row[0]        if int(row[1])<greatest_decrease:            greatest_decrease=int(row[1])            date2=row[0]average=round(total/total_months,2)print("Data Analysis")print("--------------------------")    print(f"Total Months: {total_months}")print(f"Total: {total}")print(f"Average Change: ${average}")print(f"Greatest Increase in Profits: {date} (${greatest_increase})")print(f"Greatest Decrease in Profits: {date2} - (${greatest_decrease})")      output_path=os.path.join("analysis", "output.txt")with open(output_path, "w") as file:        file.write("Data Analysis\n")    file.write("--------------------------\n")    file.write(f"Total Months: {total_months}\n")    file.write(f"Total: {total}\n")    file.write(f"Average Change: ${average}\n")    file.write(f"Greatest Increase in Profits: {date} (${greatest_increase})\n")    file.write(f"Greatest Decrease in Profits: {date2} - (${greatest_decrease})\n")     