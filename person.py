from __future__ import print_function
import sys

if sys.version_info < (3, 0):
	input = raw_input


class Person(object):
	def __init__(self, name):
		self.name = name

# display all information
	def display(self, warehouse):
		print("This is {0}., display all information".format(self.name))
		print("The warehouse contains:", warehouse.list_contents())
# change the status to on load and display all information
	def status_changeon(self, warehouse, isbn):
		warehouse.status_on(isbn)
		self.display(warehouse)
# change the status to not on load and display all information
	def status_changenot(self, warehouse, isbn):
		warehouse.status_not(isbn)
		self.display(warehouse)
# display the subset of books currently stored inclusive year range(2000-2010)
	def display_3(self, warehouse, year1, year2):
		print("The warehouse subset contains based on Year of Publication:", warehouse.display_year(year1, year2))

# display the subset of books currently stored based on ISBN
	def display_4(self, warehouse, isbn):
		print("The warehouse subset contains based on ISBN:", warehouse.display_isbn(isbn))


