# Goal: CLI that displays info about an IP adress, sourced from an online API and parsed from JSON format
import webbrowser
import requests
import ipaddress


# use api to get infromation about the IP address and parse it into a dictionary
def GetInfo(ipAddress):
    # HTTP request ap-api.com for info on the IP and return data(selected with fields option) as JSON
    # uses f-strings to add the query into the string
    ipInfo = requests.get(f"http://ip-api.com/json/{ipAddress}?fields=status,message,country,regionName,city,lat,lon,org,query")
    # convert the JSON data from the request into a python dictionary
    return ipInfo.json()


# print out data nicely
def PrintOutput(addressInfo):
    print("========================= \n||IP Adress Information|| \n=========================")
    print("Country:", addressInfo['country'], "\nRegion/State:", addressInfo['regionName'], "\nCity:", addressInfo['city'])
    print("Coordinates:", str(addressInfo['lat']) + ",", str(addressInfo['lon']))
    print("Organization:", addressInfo['org'],"\n")


# open web browser with location on maps
def OpenMap(addressInfo):
    latitude = addressInfo['lat']
    longitude = addressInfo['lon']
    webbrowser.open(f"https://www.google.com/maps/place/{latitude},{longitude}")


# TODO: error messages and incorrect input
def ValidateIP(ipToCheck):
    try:
        ipaddress.ip_address(ipToCheck)
    except:
        print("invalid ip")

# IP address to check
query = input("Enter IP Address (leave blank for localhost): ")

ValidateIP(query)

# main code execution
parsedInfo = GetInfo(query)
# print(parsedInfo)
PrintOutput(parsedInfo)
# OpenMap(parsedInfo)