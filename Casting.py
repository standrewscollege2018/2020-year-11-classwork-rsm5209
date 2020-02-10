""" This program gets an item name and price, then adds GST to the price"""



Item_name = input("Item name? ")
number = float(input("Item Price? "))
gst = (number/10 * 1.5)
print(Item_name, "will cost", gst + number,"including GST ")

    