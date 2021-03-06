import requests
import spacy
from difflib import SequenceMatcher
from bs4 import BeautifulSoup
from googlesearch import search
import yfinance as yf
import pandas as pd
import requests
import yahooquery as yq
import re
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

class DataResult:
    def __init__(self, url, company, ticker):
        self.url = url
        self.company = company
        self.ticker = ticker

    def __str__(self):
        return f'({self.ticker})'

class SymbolResult:
    def __init__(self, symbol, company):
        self.symbol = symbol
        self.company = company



def getNouns(title):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(title)
    #print("The nouns are:")
    return list(doc.noun_chunks)


# return list(doc.noun_chunks)

def get_symbol(query, preferred_exchange='AMS'):
    try:
        data = yq.search(query)
    except ValueError:  # Will catch JSONDecodeError
        print(query)
    else:
        quotes = data['quotes']
        if len(quotes) == 0:
            return SymbolResult("No Symbol Found", "")

        symbol = SymbolResult("No Symbol Found", "")
        for quote in quotes:
            # print("quote = ", quote)
            try:
                symbolLike = similar(query.lower(), quote['symbol'].lower())
                nounLike = similar(query.lower(), quote['longname'].lower())
                print(query.lower()," = ", symbolLike)
                if nounLike > 0.5 or symbolLike > 0.5:
                    #if query.lower() in quote['longname'].lower():
                    symbol = SymbolResult(str(quote['symbol']), str(quote['longname']))
                    break
            except:
                #print(quote)
                symbolLike = similar(query.lower(), quote['symbol'].lower())
                nounLike = similar(query.lower(), quote['shortname'].lower())
                print("Similar = ", symbolLike)
                if nounLike > 0.5 or symbolLike > 0.5:
                    #if query.lower() in quote['shortname'].lower():
                    symbol = SymbolResult(str(quote['symbol']), str(quote['shortname']))
                    break
        return symbol

def getFinanceData(symbol, period, interval):
    ticker = yf.Ticker(symbol)
    return ticker.history(period=period, interval=interval)

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def cleanName(title):
    return title.replace("/[^a-zA-Z ]/g", "").replace("|", "").replace("financial", "").replace("inc.", "").replace("co.", "")



# to search
# query = "large donations to mental health charity"
#query = "corporate donation to healthcare media"

#query = "corporate donation to mental health media"

#query = "company donates to mental health"


def getResultsFromQuery(inputquery, period, interval):
    # query = "news company donates to mental health"
    query = inputquery

    results = []

    for url in search(query, tld="co.in", num=10, stop=10, pause=0):
        try:
            # making requests instance
            reqs = requests.get(url)

            # using the BeaitifulSoup module
            soup = BeautifulSoup(reqs.text, 'html.parser')

            # displaying the title
            #print("Title of the website is : ")

            title = soup.find('title').get_text()

            print(title)

            title = cleanName(title)

            nouns = getNouns(title)

            for noun in nouns:
                symbolResult = get_symbol(str(noun))
                print(symbolResult.symbol)
                #print(noun, " = ", symbol)
                #if (symbol != "No Symbol Found") and (any(x.ticker == symbol.symbol for x in results)):
                if (symbolResult.symbol != "No Symbol Found"):
                    print(noun, " = ", symbolResult.symbol)
                    results.append(DataResult(url, symbolResult.company, symbolResult.symbol))
        except:
            print("error, moving on")

        #print("END")
    print(results)
    historyResults = list()

    for result in results:
        print(result.url)
        print(result.company)
        dat = getFinanceData(result.ticker, period, interval)
        historyResults.append([result.url, result.company, dat])
        print(dat)

    #print("The end")
    return historyResults
