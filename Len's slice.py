#creating a list of toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

#list of prices
prices = [2, 6, 1, 3, 2, 7, 2]

#number of 2$ slices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

#length of toppings list
num_pizzas = len(toppings)
print("we sell " + str(num_pizzas) + " different kinds of pizza!")

#comining the two lists using a 2D list
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)
pizza_and_prices.sort()

#Cheapest_pizza
cheapest_pizza = pizza_and_prices[0]
#priciest_pizza
priciest_pizza = pizza_and_prices[-1]
#Removing anchovies
pizza_and_prices.pop()

#adding a new topping
pizza_and_prices.insert(4, [2.5,"peppers"])
#3 lowest cost pizzas for mice
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)


