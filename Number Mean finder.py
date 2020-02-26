numbers = []

keep_asking = True

while keep_asking == True:
                try:
                                number_input = int(input("Enter a number: "))
                                if number_input == -1:
                                                keep_asking = False
                                else:
                                                numbers.append(number_input)
                                                                               
                except:
                                print("Please enter a valid number")
print("You entered these numbers") 
for i in range(len(numbers)):
                print(numbers[i])
print("This is the mean of the numbers you entered", sum(numbers) / len(numbers))
