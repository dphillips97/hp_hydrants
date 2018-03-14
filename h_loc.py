import openpyxl
import requests
import json
from api_keys import *

URL = r'https://maps.googleapis.com/maps/api/geocode/json?'
API_KEY = GITHUB_API_KEY




def read_wb():

	# open sheet object
	wb = openpyxl.load_workbook('hydrant_loc.xlsx')
	sheet = wb.active
	
	max_rows = sheet.max_row
	
	# pass sheet object and max rows to main()
	return sheet, max_rows

def geocode(loc, URL):	

	city = ',Hazel_Parl'
	state = ',MI'

	unique_url = URL + 'address=%s&key=%s' % ((loc + city + state), API_KEY)
	results = requests.get(unique_url)
	
	data = json.loads(results.txt)
	
	
	
def main():
	
	# get sheet object and max rows from other function
	sheet, max_rows = read_wb()
	
	for row_iter in range(2, max_rows):
		
		loc = sheet.cell(row = row_iter, column = 2).value
	
	
		
main()