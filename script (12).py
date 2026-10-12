from math import sqrt, pow
#Gather data
X1_value=float(input("enter the first value of the first point: "))
X2_value=float(input("enter the first value of the second point: "))
Y1_value=float(input("enter the second value of the first point: "))
Y2_value=float(input("enter the second value of the second point: "))
#Calculations
D = sqrt(pow(X2-X1, 2) + pow(Y2-Y1, 2))
#Display output
print (D)