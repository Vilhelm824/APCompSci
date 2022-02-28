# Goal: CLI that displays info about an IP adress, sourced from an online API and parsed from JSON format
import webbrowser
import requests

# IP address to check
query = input("Enter IP Address to check (just hit enter for localhost): ")

# HTTP request ap-api.com for info on the IP and return data(selected with fields option) as JSON
# uses f-strings to add the query into the string
ipInfo = requests.get(f"http://ip-api.com/json/{query}?fields=status,message,country,regionName,city,zip,lat,lon,org,query")

# convert the JSON data from the request into a python dictionary
parsedInfo = ipInfo.json()

print(parsedInfo)

# TODO: error messages and incorrect input, maybe CLI parser
# TODO: print out data nicely, maybe add location-based message
# TODO: open web browser with location on maps