# -*- coding: latin-1 -*-

#Searches OMDb for json-respones, where title is passed argument 1, and returns value at argument 2

import json, urllib.request, sys #libraries for json and url
#sys.argv[0] contains script-name -- similar to C
#sys.argv[1] contains passed argument 1 -- similar to C
title = sys.argv[1].replace(" ", "%20")
#http://www.omdbapi.com/?t=hannibal&y=&plot=short&r=json
url = "http://www.omdbapi.com/?t=" + title + "&y=&plot=short&r=json" #adds strings to variable url
response = urllib.request.urlopen(url).read().decode('utf-8') #reads url, decodes to utf8 char encoding
parsed_json = json.loads(response) #reads and parses json string to variable parsed_json

print(parsed_json[sys.argv[2]]) #Prints the parsed json, at value of passed argument 2 (can be title, year, etc for this case)

#xyplorer test: 
#echo runret('python json_web_argv.py "the terminator" "Year"', "D:\Google Drive\Utbildning\Mjukvaruutvecklare inbyggda system\Kod\Python\Testing\JSON\");
#Will get 'year' of movie 'the terminator'