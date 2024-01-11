import requests

headers = {
    "X-RapidAPI-Key": "32b8e14648mshd695d1fdad61f9ep1012c5jsn77b10c892e78",
    "X-RapidAPI-Host": "breachdirectory.p.rapidapi.com"
}
url = "https://breachdirectory.p.rapidapi.com/"
querystring = {"func":"auto","term":"anshdwansh@gmail.com"}
response = requests.get(url, headers=headers, params=querystring)

print(response.json())
# print(data['found'])
# if data['found'] > 0:
#     print("your email was leaked in a database.....!")
#     for i in range(data['found']):
#         if(1):
#             pass
# else:
#     print("your email was not leaked....!")
