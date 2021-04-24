#importing panda and matplotlib
import pandas as p
import matplotlib.pyplot as mPlot

#getting data from csv file
data = p.read_csv("company_sales_data.csv")

month = data['month_number'].tolist()
toothpaste = data['toothpaste'].tolist()

#creates scatter plot
mPlot.scatter(month, toothpaste, label = 'Toothpaste Sales Data')
#label for the x axis
mPlot.xlabel('Month Number')
#label for the y axis
mPlot.ylabel('Number of units sold')
#sets the legend in the lower right corner
mPlot.legend(loc='upper left')
# title of graph
mPlot.title('Toothpaste Sales Data')
mPlot.xticks(month)
#sets line style and width of grid
mPlot.grid(True, linewidth = 1, linestyle = "--")
mPlot.show()
