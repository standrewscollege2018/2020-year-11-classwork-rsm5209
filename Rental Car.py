import time
cars = ["Suzki Van", "Toyota Corolla", "Honda CRV", "Suzuki Swift", "Mitsubishi Airtek", "Nissan DC Ute", "Toyota Previa", "Toyota Hiace", "Toyota Hiace"]
seats = [2, 4, 4, 4, 4, 4, 7, 12, 12]
availability = ["Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes"]
keep_asking = True
chars = set("$,`~!@#%^&*()':;./?><-_=+|{}[]")
what_car = True
while keep_asking == True:
    try:
        seats_needed = input("How many seats are needed?: ")
        if any((c in chars) for c in seats_needed) or seats_needed == "":
            print("Please enter a valid number")
        else:
            print("Great, now pick a car")
            int_seats_needed = int(seats_needed)
            keep_asking = False
    except:
        print("Please enter a valid number")

print("Getting all the cars...")
time.sleep(2)
for i in range(len(cars)):
    print("{}. {} - seats: {} - available: {}".format(i+1, cars[i], seats[i], availability[i]))
    time.sleep(0.1)
while what_car == True:    
    try:
        car_input = input("What car would you like to borrow?\n")
        int_car_input = int(car_input)
        if seats[int_car_input -1]  < int_seats_needed:
            print("You said you needed {} seats, this car does not meet the seating requirements that you have entered".format(seats_needed))
        else:
            print("Ok, thanks for borrowing the {}. It is ready".format(cars[int_car_input-1]))
            
    except:
        print("Please enter a valid number")


    