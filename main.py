# my app to find out LIVE information about JWT using Nasa's public JWT API :)
from requests import *

jwt_API=get("https://api.jwst-hub.com/track")

print(jwt_API.text)


