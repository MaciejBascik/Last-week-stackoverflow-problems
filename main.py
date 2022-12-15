import requests
import json
import pprint
import webbrowser
import datetime

params = {"site": "stackoverflow", 
            "tagged" :"python", 
            "order": "desc",
            "fromdate":"2022-12-15", 
            "min": 15, 
            "sort" : "votes"
        }
r = requests.get("https://api.stackexchange.com/2.3/questions/", params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Invalid format")
else:
    def openBrowser():
        for question in questions["items"]:
            webbrowser.open_new_tab(question["link"])
    def checkQuestions(numberOfDays):

        if (questions['items'] == list("")):
                print("There aren't any questions in this week!") 
                choice = input("Do you want to change period of time? (y - yes n - no): ")

                if (choice == "y" or "Y"):

                    date = datetime.datetime.today() - datetime.timedelta(days=numberOfDays)
                    params["fromdate"] = (date.year, date.month, date.day)

                    r = requests.get("https://api.stackexchange.com/2.3/questions/", params)

                    questions2 = r.json()
                    for question in questions2["items"]:
                            webbrowser.open_new_tab(question["link"])
                elif (choice == "n" or "N"):
                    print("Thank you for using my app!")
                else:
                    print("Choose yes or no.")

checkQuestions(15)
