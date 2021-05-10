import requests
import json

# pip install pywin32
from win32com.client import Dispatch
s = Dispatch("SAPI.SpVoice")


def speak(country, category, apikey):
    s.speak("Today's top headlines are as follows :")
    url = f"http://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={apikey}"
    response = requests.get(url)
    # print(response.json()['status'])

    #  -- OR --

    newsText = response.text
    newsDict = json.loads(newsText)
    # print(newsDict['articles'])

    articles = newsDict['articles']
    k = 1
    for a in articles:
        print(" ")
        print(' #', k, "--")
        print(" ")
        print(a['url'])
        print(" ")
        print(a['content'])
        s.speak(a['title'])
        if k<len(articles):
            s.speak("Moving on to the next news...")
        k+=1

    s.speak('Thanks for Listening!')


if __name__ == "__main__":

    print(" ")
    print("The 2-letter ISO 3166-1 code of the country you want to get headlines for. Possible options:\nae ar at au be bg br ca ch cn co cu cz de eg fr gb gr hk hu id ie il in it jp kr lt lv ma mx my ng nl no nz ph pl pt ro rs ru sa se sg sisk th tr tw ua us ve za\n")
    country = input("Enter Country Code :\n ")

    print(" ")
    print("The category you want to get headlines for. Possible options:\n business entertainment general health science sports technology\n")
    category = input("Enter Category :\n ")

    print(" ")
    apikey = "Enter-your-apikey-here"
    speak(country, category, apikey)



