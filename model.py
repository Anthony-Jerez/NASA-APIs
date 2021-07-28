import requests

def getImageUrlFrom(userEntry):
    myNasaAPIResponse = requests.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera={userEntry}&api_key=DEMO_KEY").json()
    myNasaImageURL = myNasaAPIResponse['photos'][0]["img_src"]
    return myNasaImageURL

#print(myNasaAPIResponse)

