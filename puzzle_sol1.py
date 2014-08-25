import sys
import csv
import math
import time
import pprint
from collections import defaultdict
from operator import itemgetter
from itertools import chain, combinations

def powerset(iterable):
	s = list(iterable)
	return chain.from_iterable(combinations(s, r) for r in range(1,len(s)+1))

class restaurant_puzzle(object):
	def __init__(self, fname, item_list):
		self.filename = fname
		self.items = item_list
		self.itemized_menu = {}
		self.items_per_restaurant = {}
		self.csv_rows = []
		self.possible_restaurants = []
		self.min_price = {}
		self.min_pair = ()

	def read_csv_file(self):
		with open(self.filename, 'rb') as f:
			reader = csv.reader(f)
			for row in reader:
				if len(row) > 2:
					if row[0] not in self.itemized_menu:
						self.itemized_menu[row[0]] = defaultdict(list)

					price = float(row[1])	
					tmp_lis = [x.strip() for x in row[2:]]
					for item in tmp_lis:
						if item in self.items:
							tmp_lis.append(price)
							self.itemized_menu[row[0]][price].append(tuple(tmp_lis))
							break

		#pprint.pprint(self.itemized_menu)
				
	def get_items_per_restaurant(self):
		for res_id,menu in self.itemized_menu.items():
			tmp = []
			for price,items in menu.items():
				tmp.extend(items)
			self.items_per_restaurant[res_id] = tmp
		#pprint.pprint(self.items_per_restaurant)

	def find_matching_restaurants(self):
		for key, val in self.items_per_restaurant.items():
			flat_set = set(sum(val, ()))
			if set(self.items).issubset(flat_set):
				self.possible_restaurants.append(key)
		#print self.possible_restaurants

	def get_restaurant_items(self, rest_id):
		menu_list = set()
		for key,val in self.itemized_menu[rest_id].items():
			for items in val:
				menu_list.add(items)
		return menu_list

	def min_price_per_restaurant(self,rest_id,food_combinations):
		min_price = math.pow(10,7)
		for combination in food_combinations:
			items_in_combination = []
			total_price = 0.0
			for item in combination:
				total_price += item[-1]
				items_in_combination.extend(x for x in item[:len(item)-1])
			if set(self.items).issubset(set(items_in_combination)) and total_price < min_price:
				self.min_price[rest_id] = total_price
				min_price = total_price

	def find_min_price_all_restaurant(self):
		if len(self.possible_restaurants) == 0:
			print "Nil"
		else:
			for rest_id in self.possible_restaurants:
				menu_items = self.get_restaurant_items(rest_id)
				possible_food_combinations = set(powerset(menu_items))
				self.min_price_per_restaurant(rest_id, possible_food_combinations)
			
			self.min_pair = min(self.min_price.iteritems(), key=itemgetter(1))
			print '%s %s' % (self.min_pair[0], self.min_pair[1])	

	def execute(self):
		self.read_csv_file()
		self.get_items_per_restaurant()
		self.find_matching_restaurants()
		self.find_min_price_all_restaurant()

if __name__ == '__main__':
	filename = sys.argv[1]
	items = sys.argv[2:]
	obj = restaurant_puzzle(filename,items)
	start = time.time()
	obj.execute()
	end = time.time()
	print end-start