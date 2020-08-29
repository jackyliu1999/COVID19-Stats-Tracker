import requests
from tkinter import *
from datetime import datetime
import webbrowser
from newsapi import NewsApiClient
import os

def dailyStats():
    r = requests.get("https://thevirustracker.com/free-api?global=stats")
    x = r.json()
    y = x["results"]
    gui = Tk()
    gui.geometry("400x125")
    title = "Coronavirus Daily Stats for: "+str(datetime.date(datetime.now()))
    gui.title(title)
    totalCases = "Total Cases: " + str(y[0]["total_cases"])
    totalRecovered = "Total Recovered: " + str(y[0]["total_recovered"])
    totalDeaths = "Total Deaths: " + str(y[0]["total_deaths"])
    deathsToday = "Deaths Today: " + str(y[0]["total_new_deaths_today"])
    newCasesToday = "New Cases Today: " + str(y[0]["total_new_cases_today"])
    label = Label(gui, text=totalCases)
    label.pack(side=TOP)
    label2 = Label(gui, text=totalRecovered)
    label2.pack(side=TOP)
    label3 = Label(gui, text=totalDeaths)
    label3.pack(side=TOP)
    label4 = Label(gui, text=deathsToday)
    label4.pack(side=TOP)
    label5 = Label(gui, text=newCasesToday)
    label5.pack(side=TOP)
    gui.after(15000, gui.destroy)
    gui.mainloop()

def financialHelp():
    webbrowser.open("https://www.canada.ca/en/services/benefits/ei/cerb-application.html")

def openURL(url):
    webbrowser.open(url)

def news():
    newsapi = NewsApiClient(api_key='c5bdf991c8be4c53bc9d90c4f7e42caf')
    top_headlines = newsapi.get_top_headlines(q='covid', language='en')
    article1 = top_headlines["articles"][1]["title"]
    article1URL = top_headlines["articles"][1]["url"]
    article2 = top_headlines["articles"][2]["title"]
    article2URL = top_headlines["articles"][2]["url"]
    article3 = top_headlines["articles"][3]["title"]
    article3URL = top_headlines["articles"][3]["url"]
    article4 = top_headlines["articles"][4]["title"]
    article4URL = top_headlines["articles"][4]["url"]
    article5 = top_headlines["articles"][5]["title"]
    article5URL = top_headlines["articles"][5]["url"]
    gui = Tk()
    gui.geometry("700x250")
    title = "COVID-19 Top News: "+str(datetime.date(datetime.now()))
    gui.title(title)
    label = Label(gui, text=article1)
    label.pack(side=TOP)
    b = Button(gui, text="Open Article", command=lambda:openURL(article1URL))
    b.pack(side=TOP)
    label2 = Label(gui, text=article2)
    label2.pack(side=TOP)
    b2 = Button(gui, text="Open Article", command=lambda:openURL(article2URL))
    b2.pack(side=TOP)
    label3 = Label(gui, text=article3)
    label3.pack(side=TOP)
    b3 = Button(gui, text="Open Article", command=lambda:openURL(article3URL))
    b3.pack(side=TOP)
    label4 = Label(gui, text=article4)
    label4.pack(side=TOP)
    b4 = Button(gui, text="Open Article", command=lambda:openURL(article4URL))
    b4.pack(side=TOP)
    label5 = Label(gui, text=article5)
    label5.pack(side=TOP)
    b5 = Button(gui, text="Open Article", command=lambda:openURL(article5URL))
    b5.pack(side=TOP)
    gui.mainloop()

def statsUS():
    r = requests.get("https://api.smartable.ai/coronavirus/stats/US?Subscription-Key=1b78004d760e4e9dbfbb7a8072a980ae")
    x = r.json()
    y = x["stats"]
    totalCases = "Total Cases: "+str(y["totalConfirmedCases"])
    totalRecovered = "Total Recovered: "+str(y["totalRecoveredCases"])
    totalDeaths ="Total Deaths: "+str( y["totalDeaths"])
    gui = Tk()
    gui.geometry("500x75")
    title = "Coronavirus Daily Stats United States: "+str(datetime.date(datetime.now()))
    gui.title(title)
    label = Label(gui, text=totalCases)
    label.pack(side=TOP)
    label2 = Label(gui, text=totalRecovered)
    label2.pack(side=TOP)
    label3 = Label(gui, text=totalDeaths)
    label3.pack(side=TOP)
    gui.mainloop()

def statsCanada():
    r = requests.get("https://api.smartable.ai/coronavirus/stats/CA?Subscription-Key=1b78004d760e4e9dbfbb7a8072a980ae")
    x = r.json()
    y = x["stats"]
    totalCases = "Total Cases: "+str(y["totalConfirmedCases"])
    totalRecovered = "Total Recovered: "+str(y["totalRecoveredCases"])
    totalDeaths ="Total Deaths: "+str( y["totalDeaths"])
    gui = Tk()
    gui.geometry("400x75")
    title = "Coronavirus Daily Stats Canada: "+str(datetime.date(datetime.now()))
    gui.title(title)
    label = Label(gui, text=totalCases)
    label.pack(side=TOP)
    label2 = Label(gui, text=totalRecovered)
    label2.pack(side=TOP)
    label3 = Label(gui, text=totalDeaths)
    label3.pack(side=TOP)
    gui.mainloop()

def reddit():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    r = requests.get("https://www.reddit.com/r/COVID19/top.json", headers=headers)
    x = r.json()
    y = x["data"]
    z = y["children"]
    post1 = z[0]["data"]["title"]
    post1 = post1[0:100]
    post1Link = "https://www.reddit.com/"+z[0]["data"]["permalink"]
    post2 = z[1]["data"]["title"]
    post2 = post2[0:100]
    post2Link = "https://www.reddit.com/"+z[1]["data"]["permalink"]
    post3 = z[2]["data"]["title"]
    post3 = post3[0:100]
    post3Link = "https://www.reddit.com/"+z[2]["data"]["permalink"]
    post4 = z[3]["data"]["title"]
    post4 = post4[0:100]
    post4Link = "https://www.reddit.com/"+z[3]["data"]["permalink"]
    post5 = z[4]["data"]["title"]
    post5 = post5[0:100]
    post5Link = "https://www.reddit.com/"+z[4]["data"]["permalink"]
    gui = Tk()
    gui.geometry("700x250")
    title = "COVID-19 Top News: "+str(datetime.date(datetime.now()))
    gui.title(title)
    label = Label(gui, text=post1)
    label.pack(side=TOP)
    b = Button(gui, text="Open Reddit Post", command=lambda:openURL(post1Link))
    b.pack(side=TOP)
    label = Label(gui, text=post2)
    label.pack(side=TOP)
    b = Button(gui, text="Open Reddit Post", command=lambda:openURL(post2Link))
    b.pack(side=TOP)
    label = Label(gui, text=post3)
    label.pack(side=TOP)
    b = Button(gui, text="Open Reddit Post", command=lambda:openURL(post3Link))
    b.pack(side=TOP)
    label = Label(gui, text=post4)
    label.pack(side=TOP)
    b = Button(gui, text="Open Reddit Post", command=lambda:openURL(post4Link))
    b.pack(side=TOP)
    label = Label(gui, text=post5)
    label.pack(side=TOP)
    b = Button(gui, text="Open Reddit Post", command=lambda:openURL(post5Link))
    b.pack(side=TOP)
    gui.mainloop()

def buyMasks():
    webbrowser.open("https://www.amazon.com/s?k=masks")

def buySanitizer():
    webbrowser.open("https://www.amazon.com/s?k=hand+sanitizer")

def clinic():
    webbrowser.open("https://www.google.com/search?q=covid19+clinic+near+me&oq=covid19+clinic+near+me&aqs=chrome..69i57j0l4.2790j0j7&sourceid=chrome&ie=UTF-8")

def help():
    os.startfile("Documentation.txt")