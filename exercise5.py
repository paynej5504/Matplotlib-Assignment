#importing panda and matplotlib
import pandas as p
import matplotlib.pyplot as mPlot

#getting data from csv file
data = p.read_csv("company_sales_data.csv")

#list each product
month = data['month_number'].tolist()
faceCream = data['facecream'].tolist()
faceWash = data['facewash'].tolist()

#creates bar graph for face cream and face wash
mPlot.bar([a-0.25 for a in month], faceCream, width = 0.25, label = 'Face Cream Sales Data', align='edge')
mPlot.bar([a+0.25 for a in month], faceWash, width = -0.25, label = 'Face Wash Sales Data', align='edge')
#label for the x axis
mPlot.xlabel('Month Number')
#label for the y axis
mPlot.ylabel('Sales units in number')
#sets the legend in the lower right corner
mPlot.legend(loc='upper left')
# title of graph
mPlot.title('Facewash and Facecream Sales Data')
mPlot.xticks(month)
#sets line style and width of grid
mPlot.grid(True, linewidth = 0.5, linestyle = "--")
mPlot.show()
