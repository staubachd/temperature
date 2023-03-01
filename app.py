import requests
import urllib.request, json
import time

url = "https://lnkt4gjfcsr4rxvyr46icmbb5y0mgmuf.lambda-url.eu-central-1.on.aws/"

def getJsonContentFromUrl():
    with urllib.request.urlopen(url) as jsonRequest:
        jsonContent = json.load(jsonRequest)
        print(jsonContent)

starttime = time.time()

while True:
    getJsonContentFromUrl()
    time.sleep(5.0 - ((time.time() - starttime) % 5.0))