import datetime as dt
from decimal import Decimal
from random import randint
from random import choice
import custom_module
date = dt.date.today()
time = dt.datetime.now().time()
print(date)
print(time)
base_cost = Decimal('1000.00')
current_year = dt.date.today().year
target_year = randint(1900, 2100)
year_difference = abs(current_year - target_year)
final_cost = base_cost * Decimal(year_difference)
destinations = ["Mars", "The moon", "Earth", "Jupiter", "Milky way", "Sea"]
selected_destination = choice(destinations)
message = custom_module.generate_time_travel_message(target_year, selected_destination, final_cost)
print(message)

