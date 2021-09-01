# GET OPEN-SRC DATA FROM NETWORK
import urllib.request as request
import json
src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    data = json.load(response)
print(data)

clist = data["result"]["results"]
with open("company.txt", "w", encoding = "utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"] + "\n")
