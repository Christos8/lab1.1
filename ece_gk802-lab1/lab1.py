#### LAB1 ####
#### CHYTAS CHRISTOS 1084003 ####

import requests

url = input("Give an URL address: ")

if not url.startswith("https://"):
    url = "https://" + url


with requests.get(url) as response: 
    print("Website headers are: \n", response.headers)

    server = response.headers.get('Server')

    if server:
        print("\n\nThe server is: ", server)
    else:
        print("\n\nNo server found")

    cookies = response.headers.get("Set-Cookie")

    if cookies:
        print("\n\nThe cookies are: ", cookies)
    else:
        print("\n\nNo cookies found")