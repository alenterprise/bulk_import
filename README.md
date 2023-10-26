# bulk_import
OmniSwitch Import into OmniVista 2500 using API

# How to use the script 
python3 addDevice.py inventory_2.csv 

# Pre-requisites 

This is the payload sent to OmniVista.
Be sure to fill the right snmp parameters including :
- snmpVersion: (Version of the SNMP used)
- securityName:(Name of the snmp profile created on OmniVista 2500 web ui)
- authProtocol: (Type of hash/encryption used in the SNMP profile created)
- authPassword
- privPassword

```json
{
    "ipAddress": "1.1.1.1",
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
        "useGetbulk": true,
        "maxRepetitions": 10,
        "allowPortDisabling": false
    }
}
```
