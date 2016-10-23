# -*- coding: latin-1 -*-

#Gets data for TV-show/Movie from JSON respone
#Either from TV-Maze or OMDb, depending on passed argument 2
#Argument 3 is the value to read eg Title, name, Genre, genres, etc

import json, urllib.request, sys #libraries for json and url
#sys.argv[0] contains script-name -- similar to C
#sys.argv[1] contains passed argument 1 -- IMDb-id
#sys.argv[2] contains passed argument 2 -- 1 = OMDb 2= TVmaze
#sys.argv[3] contains passed argument 3 -- Key to read: eg Title, name, Genre, genres, etc

imdb = sys.argv[1]

if int(sys.argv[2]) == 1: #Arguments are passed as strings? Use int() to convert to integer
	url = "http://www.omdbapi.com/?i=" + imdb + "&y=&plot=short&r=json" #adds strings to variable url

elif int(sys.argv[2]) == 2:
	url = "http://api.tvmaze.com/lookup/shows?imdb=" + imdb
	
else:
	print("Wrong arg2")

response = urllib.request.urlopen(url).read().decode('utf-8') #reads url, decodes to utf8 char encoding
parsed_json = json.loads(response) #reads and parses json string to variable parsed_json

if sys.argv[3] == "lastAired": 
	print(parsed_json["_links"]["previousepisode"]["href"]) #Will get the url for last aired episode of show

else: #Prints the parsed json, at value of passed argument 2 (can be title, year, etc for this case)
	print(parsed_json[sys.argv[3]]) 

#command line test: 
#python json_tvmaze_omdb.py tt0475784 2 lastAired
