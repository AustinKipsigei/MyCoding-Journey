#This is a program that prints out the receipt of a customer purchasing items from our business "LovelySeats"

#creating a variable lovely_loveseat_description
lovely_loveseat_description="Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

#setting price of the lovely seat
lovely_loveseat_price = 254.00

#extending our inventory with stylish_settee_description
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

#setting price for stylish_settee_description
stylish_settee_price = 180.50

#adding luxury lamp to our inventory and its description
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

#setting the price for the lamp
luxurious_lamp_price = 52.15

#adding the variable sales tax
sales_tax = 0.88

#our first customer
customer_one_total = 254.00

#customer one itemization
customer_one_itemization = lovely_loveseat_description

#customer purchased luxurious lamp
customer_one_total += luxurious_lamp_price

#adding luxurious lamp description to customer itemization
customer_one_itemization += luxurious_lamp_description

#calculating sales tax
customer_one_tax = customer_one_total*sales_tax

#adding sales tax
customer_one_total += customer_one_tax

print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)
