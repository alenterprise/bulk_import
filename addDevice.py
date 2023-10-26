import requests
import csv 
import sys


################## OV IP + USER/PASSWORD ##############


OmniVistaIP = "192.168.121.66"
userOV = "admin"
passwordOV = "0Trust2023!"


#######################################################


requests.packages.urllib3.disable_warnings()

filename = sys.argv[1]

url0 = "https://"+OmniVistaIP+"/rest-api/login"  # Remplacez l'URL par celle de l'API que vous souhaitez appeler
headers0 = {
    "Content-Type": "application/json"  # Spécifiez le type de contenu de la requête
}

username = "admin"
password = "0Trust2023!"

data0 = {
    "userName": userOV,
    "password": passwordOV
}

response = requests.post(url0, headers=headers0, json=data0, verify=False)

if response.status_code == 200:
    data = response.json()
    token= response.json().get("accessToken")
    #print("token vaut : ",token)
else:
    print("Erreur lors de l'appel de l'API :", response.status_code)


url = "https://"+OmniVistaIP+"/api/discoverylite/devices"
headers = {
    "Content-Type" : "application/json",
    "Authorization" : "Bearer {}".format(token)
}

with open(filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ipaddress = row['ipaddress']
        description = row['description']
        print(f"IP : {ipaddress}, Description : {description}")

        DiscoverProfile = {
            
        "ipAddress": ipaddress,
        "discoveryProfile": {
            "name": "no-name",
            "telnetOrFTPUser": "admin",
            "telnetOrFTPPassword": "switch",
            "secondaryPassword": "",
            "snmpProfile": {
                "type": "SnmpProfile",
                "snmpVersion": "SNMPv3",
                "readSnmpCommunity": "",
                "writeSnmpCommunity": "",
                "snmpv3Information": {
                    "contextId": "",
                    "contextName": "",
                    "securityName": "snmpv3user",
                    "authProtocol": "SHA_DES",
                    "authPassword": "Superuser=1",
                    "privPassword": "Superuser=1"
                },
                "maxRetries": 3,
                "timeout": 5000
            },
            "trapStationUserName": "",
            "discoverLinks": "Normally",
            "shellPreference": "SSH",
            "useGetbulk": True,
            "maxRepetitions": 10,
            "allowPortDisabling": False
        },
        #"currentMap": "64aebef3012ac3480d4af850"
            }

        response = requests.post(url, headers=headers, json=DiscoverProfile, verify=False)
        data = response.json()
        print("La règle a été créee : ",data)


