# Goal: CLI that displays info about an IP adress, sourced from an online API and parsed from JSON format
from ast import parse
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


# checks if the input is a valid ip address and returns a boolean accordingly
def ValidateIP(ipToCheck):
    try:
        ipaddress.ip_address(ipToCheck)
    except:
        return False
    else:
        return True


#----Main Code Execution----

# ask for IP address to check and make sure it's valid
while(True):
    query = input("Enter IP Address (leave blank for localhost): ")
    if(ValidateIP(query) or query == ""):
        break
    print("invalid IP, try again")
    
# get info from the api database
parsedInfo = GetInfo(query)

# print error message and exit the program if there's an api error
if(parsedInfo['status'] == 'fail'):
    errorMessage = parsedInfo['message']
    print(f"There was a problem with the api ({errorMessage}), exiting program...")
    exit()

# show output
PrintOutput(parsedInfo)

# choose whether or not to open a map of the location, must enter 'y' or 'n'
while(True):
    mapYN = input("Open map (y/n) ")
    if(mapYN == 'y' or mapYN == 'Y'):
        OpenMap(parsedInfo)
        break
    elif(mapYN == 'n' or mapYN == 'N'):
        break

print("Exiting program...")
exit()