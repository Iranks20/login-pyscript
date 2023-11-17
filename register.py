import requests

def register_user(countryCode, email, firstName, lastName, phoneNumber, state, clientId, deviceId, disableSeamlessChannel, layout, redirecctUri, responseType, scope ):
    url = "https://identity.doordash.com/auth/google/signupComplete"
    payload = {
        'clientId': clientId,
        'countryCode': countryCode,
        'email': email,
        'firstName': firstName,
        'lastName': lastName,
        'phoneNumber': phoneNumber,
        'state': state,
        'deviceId': deviceId,
        'disableSeamlessChannel': disableSeamlessChannel,
        'layout': layout,
        'redirecctUri': redirecctUri,
        'responseType': responseType,
        'scope': scope,
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("user registered successfully")
        else:
            print(response)
    except requests.RequestException as e:
        print(f"Error: {e}")

# run test
countryCode = input("enter country code")
email = input('enter email')
firstName = input("enter first name")
lastName = input("enter last name")
phoneNumber = input("enter phone numbe")
state = input("enter server state")
clientId = input("enter clientid")
deviceId = input("enter deviceId")
disableSeamlessChannel = input("enter disableseamlesschannel")
layout = input("enter layout")
redirecctUri = input("enter redirect uri")
responseType = input("enter response type")
scope = input("enter scope")


register_user(countryCode, email, firstName, lastName, phoneNumber, state, clientId, deviceId, disableSeamlessChannel, layout, redirecctUri, responseType, scope)
