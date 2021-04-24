#import pandas and matplotlib
import pandas as p
import matplotlib.pyplot as mPlot

#getting data from csv file
data = p.read_csv("company_sales_data.csv")

profit = data['total_profit'].tolist()
month = data['month_number'].tolist()

#sets the line type, color, width, and marker
mPlot.plot(month, profit, label = 'Last Years Profits',
         color='r', marker='o', markerfacecolor='k', linestyle='--',
         linewidth=3)


#label for the x axis
mPlot.xlabel('Month Number')
#label for the y axis
mPlot.ylabel('Profit in Dollar')
mPlot.xticks(month)
#sets the legend in the lower right corner
mPlot.legend(loc="lower right")
# title of graph
mPlot.title('Company Sales data of last year')
#the numbers for the y axis
mPlot.yticks([100000, 200000, 300000, 400000, 500000])
mPlot.show()