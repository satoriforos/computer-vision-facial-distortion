#!/usr/bin/env python
import requests
import cv2
import base64

filename = "image.jpg"
image = cv2.imread(filename)
image_bytestring = cv2.imencode('.jpg', image)[1].tostring()

api_url = "https://example.com"
payload = {
    "name": filename,
    "data": base64.encodestring(image_bytestring).decode("utf-8")
}

print("Uploading {} to {}".format(filename, api_url))
response = requests.put(api_url, json=payload)
print("done")
