# -*- coding: latin-1 -*-
#http://docs.python-guide.org/en/latest/scenarios/json/
import json #json lib

with open('json_test.txt', 'r') as jsonfile: #opens textfile as variable jsonfile
	parsed_json = json.loads(jsonfile.read()) #reads and parses json string to variable parsed_json
	jsonfile.closed #returns 1/0 if jsonfile file is closed by script
True #Not sure what this does here, checks that jsonfile.closed is true? What happens if not true?

#prints from parsed_json
print("Title:\t\t", parsed_json['Title'])  # as in C, \t is tab
print("Year:\t\t", parsed_json['Year'])
print("Duration:\t", parsed_json['Runtime'],"\n") # as in C, \n is new line
print("Awards:")
print(parsed_json['Awards']) 
print("Actors:")
print(parsed_json['Actors']) 