# Goal: CLI that displays info about an IP adress, sourced from an online API and parsed from JSON format
import webbrowser
import requests
import ipaddress


#----Function Definitions----#
# use api to get infromation about the IP address and parse it into a dictionary
def GetInfo(ipAddress):
    # HTTP request to ip-api.com for info on the IP and return data(selected with fields option) as JSON
    # credit to ip-api.com for the ip adress geolocation database
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
def OpenMap(addressInfo, openYN):
    latitude = addressInfo['lat']
    longitude = addressInfo['lon']
    if(openYN):
        print("opening map...")
        webbrowser.open(f"https://www.google.com/maps/place/{latitude},{longitude}")
    else:
        print("you chose not to open map")

# checks if the input is a valid ip address and returns a boolean accordingly
def ValidateIP(ipToCheck):
    try:
        ipaddress.ip_address(ipToCheck)
    except:
        return False
    else:
        return True

# get ip address of interest and whether or not to open map, and return the answers
def GetUserInput(whichInput):
    openMap = None
    query = None
    # ask for IP address to check and make sure it's valid
    if(whichInput == "ip"):
        while(True):
            query = input("Enter IP Address (leave blank for localhost): ")
            if(ValidateIP(query) or query == ""):
                break
            print("invalid IP, try again")
        return query
    # choose whether or not to open a map of the location, must enter 'y' or 'n'
    elif(whichInput == "map"):
        while(True):
            mapYN = input("Would you like to open a map of the IP address location? (y/n) ")
            if(mapYN == 'y' or mapYN == 'Y'):
                openMap = True
                break
            elif(mapYN == 'n' or mapYN == 'N'):
                openMap = False
                break
        return openMap


#----Main Code Execution----#
# prompt for IP address of interest
ipAddress = GetUserInput("ip")
print(ipAddress)
# get info from the api database
parsedInfo = GetInfo(ipAddress)

# print error message and exit the program if there's an api error
if(parsedInfo['status'] == 'fail'):
    errorMessage = parsedInfo['message']
    print(f"There was a problem with the api ({errorMessage}), exiting program...")
    exit()

# show output
PrintOutput(parsedInfo)

# prompt whether or not to open the map
openMap = GetUserInput("map")
# open map if user chose to do so
OpenMap(parsedInfo, openMap)

print("Exiting program...")
exit()