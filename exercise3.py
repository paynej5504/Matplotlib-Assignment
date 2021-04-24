#importing panda and matplotlib
import pandas as p
import matplotlib.pyplot as mPlot

#getting data from csv file
data = p.read_csv("company_sales_data.csv")

#list each product
month = data['month_number'].tolist()
faceCream = data['facecream'].tolist()
faceWash = data['facewash'].tolist()
toothpaste = data['toothpaste'].tolist()
bathingSoap = data['bathingsoap'].tolist()
shampoo = data['shampoo'].tolist()
moisturizer = data['moisturizer'].tolist()

#sets the line width and marker for each product
mPlot.plot(month, faceCream, label = 'Face cream sales', marker='o', linewidth=3)
mPlot.plot(month, faceWash, label = 'Face wash sales', marker='o', linewidth=3)
mPlot.plot(month, toothpaste, label = 'Toothpaste sales', marker='o', linewidth=3)
mPlot.plot(month, bathingSoap, label = 'Bathing soap sales', marker='o', linewidth=3)
mPlot.plot(month, shampoo, label = 'Shampoo sales', marker='o', linewidth=3)
mPlot.plot(month, moisturizer, label = 'Moisturizer sales', marker='o', linewidth=3)



#label for the x axis
mPlot.xlabel('Month Number')
#label for the y axis
mPlot.ylabel('Sales units in number')
mPlot.xticks(month)
#sets the legend in the lower right corner
mPlot.legend(loc="upper left")
# title of graph
mPlot.title('Sales data')
#the numbers for the y axis
mPlot.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
mPlot.show()