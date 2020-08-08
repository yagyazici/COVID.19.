import requests
import json
from os import system

system("cls")

api_key = ""


class Corona(object):
    def __init__(self,api_key,country_name):
        self.country_name = country_name
        self.url = "http://api.collectapi.com"
        self.api_key = api_key
        self.headers = {
            'content-type': "application/json",
            'authorization': f"{self.api_key}"
        }
        self.res = requests.get(self.url,headers=self.headers)
        self.result = json.loads(self.res.text)
    def GetInfo(self):
        self.info_url = self.url + "/corona/countriesData"
        self.res = requests.get(self.info_url,headers=self.headers)
        self.result = json.loads(self.res.text)
        self.search = self.result["result"]
        for i in self.search:
            if i["country"] == self.country_name:
                print(self.country_name.center(20,"="))
                self.country = i["country"]
                self.totalcase = i["totalCases"]
                self.newCases = i["newCases"]
                self.totalDeaths = i["totalDeaths"]
                self.newDeaths = i["newDeaths"]
                self.totalRecovered = i["totalRecovered"]
        print(f'Total case {self.totalcase}')
        print(f'New cases {self.newCases}')
        print(f'Total deaths {self.totalDeaths}')
        print(f'New deaths {self.newDeaths}')
        print(f'Total recovered {self.totalRecovered}')
    def GetInfoWorld(self):
        self.world_info = self.url + "/corona/totalData"
        self.res = requests.get(self.world_info,headers=self.headers)
        self.result = json.loads(self.res.text)
        totaldeaths = self.result["result"]["totalDeaths"]
        totalCases = self.result["result"]["totalCases"]
        totalRecovered = self.result["result"]["totalRecovered"]
        print("World".center(20,"="))
        print(f"Total deaths {totaldeaths}")
        print(f"Total cases {totalCases}")
        print(f"Total recovered {totalRecovered}")

def PrintCountries():
    headers = {
            'content-type': "application/json",
            'authorization': f"{api_key}"
        }       
    url =  "http://api.collectapi.com/corona/countriesData"
    res = requests.get(url,headers=headers)
    result = json.loads(res.text)
    country_names = result["result"]
    print("Country Names")
    for i in country_names:
        print(i["country"])






while True:
    print("Main Menu".center(30,"-"))
    print("1-Corona virus statistics for country\n2-Corona virus statistics for world")
    choice = input(">")
    system("cls")
    if choice == "1":
        try:
            PrintCountries()
            print("Enter a country name")
            country_name = input(">")
            system("cls")
            c1 = Corona(api_key,country_name)
            c1.GetInfo()
            print("="*20)
        except AttributeError:
            print(f"No country named {country_name}")
        print("1-Main menu\n2-End")
        choice2 = input(">")
        if choice2 == "1":
            system("cls")
            continue
        elif choice2 == "2":
            system("cls")
            print("End")
            break
        else:
            system("cls")
            print("Invalid choice")
            continue
    elif choice == "2":
        country_name = ""
        c1 = Corona(api_key,country_name)
        c1.GetInfoWorld()
        print("="*20)
        print("1-Main menu\n2-End")
        choice2 = input(">")
        if choice2 == "1":
            continue
        elif choice2 == "2":
            system("cls")
            print("End")
            break
        else:
            system("cls")
            print("Invalid choice")
            continue
    else:
        system("cls")
        print("Invalid choice")
        continue
