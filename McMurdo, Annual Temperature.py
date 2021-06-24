import matplotlib.pyplot as plt
# source for data: https://climate.nasa.gov/vital-signs/ice-sheets/


# line 1 points
x1 = [2002.29,2002.35,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0]
y1 = [0.00,- 9.5,-18.2,-20.7,-21.7,-23,-25.7,-26.1,-24.6,-18.9,-9.7,-3.4]
# plotting the line 1 points 
plt.plot(x1, y1, label = "line 1")
  
# naming the x axis
plt.xlabel('Month')
# naming the y axis
plt.ylabel('Temp deg C')
# giving a title to my graph
plt.title('McMurdo, Annual Temperature')
  
# show a legend on the plot
plt.legend()
  
# function to show the plot
plt.show()