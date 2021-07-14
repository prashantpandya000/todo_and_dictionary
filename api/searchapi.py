import requests
word="hell0"
url_link= "https://owlbot.info/api/v4/dictionary/"

url=url_link+word

payload={}
headers = {
  'Authorization': 'Token 8d1301b449cf197316984ff5b92d274439c69c90'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)