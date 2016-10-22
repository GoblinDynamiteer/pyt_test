# -*- coding: latin-1 -*-

#Asks for a movie title, searches OMDb for json-respones

#http://docs.python-guide.org/en/latest/scenarios/json/
import json, urllib.request #libraries for json and url

title = input("Ange filmtitel: ").replace(" ", "%20") #asks for movie title, replaces spaces with %20
#title = title.replace(" ", "%s")
#print(title)

#http://www.omdbapi.com/?t=hannibal&y=&plot=short&r=json
url = "http://www.omdbapi.com/?t=" + title + "&y=&plot=short&r=json" #adds strings to variable url

#with urllib.request.urlopen(url) as response:
response = urllib.request.urlopen(url).read().decode('utf-8') #reads url, decodes to utf8 char encoding
#str_response = response.read().decode('utf-8')
parsed_json = json.loads(response) #reads and parses json string to variable parsed_json

#prints from parsed_json
print("OMDb Repsonse for",title.replace("%20", " "),":\n")
print("Title:\t\t", parsed_json['Title'])  # as in C, \t is tab
print("Year:\t\t", parsed_json['Year'])
print("Duration:\t", parsed_json['Runtime'],"\n") # as in C, \n is new line
print("Awards:")
print(parsed_json['Awards']) 
print("Actors:")
print(parsed_json['Actors']) 