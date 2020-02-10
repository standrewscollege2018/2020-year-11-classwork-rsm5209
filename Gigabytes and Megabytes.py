""" to find out the number of megabytes in a gigabyte """

#Constant of gigabyte
GIGABYTE = 1024

#inputs
gb = int(input("Number of gigabytes? "))

#output
print("There are {} megabytes in {} gigabytes".format(gb*GIGABYTE, gb))