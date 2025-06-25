import pandas as pd

user_visits = pd.read_csv('page_visits.csv')

# Part 1.
print(user_visits.head(10))

# Part 2.
click_source = user_visits.groupby('utm_source').id.count().reset_index()

#Part 3.
print(click_source)

#Part 4.
click_source_by_month = user_visits.groupby(['utm_source', 'month']).id.count().reset_index()

#print(click_source_by_month)

#Part 5.
click_source_by_month_pivot = click_source_by_month.pivot(
	columns = 'month',
	index = 'utm_source',
	values = 'id').reset_index()

#Part 6.
print(click_source_by_month_pivot)

