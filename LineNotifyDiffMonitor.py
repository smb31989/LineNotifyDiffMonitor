from line_notify import LineNotify
import configparser
import urllib.request
import json
import datetime
import time

class Coin:
    def __init__(self, name):

        self.willingtomonitor = False
        self.targetDiff = 9999999.0
        self.difficulty = 9999999.0
        self.name = name

coins = {}

coins['rvn'] =  Coin('Ravencoin')
coins['eth'] =  Coin('Ethereum')
coins['etc'] =  Coin('Ethermine')

# Read in config file
Config = configparser.ConfigParser()
Config.read('config.config')

# Enable the coins you want to monitor here.
for key in coins:
    try:
        coins[key].willingtomonitor = Config.getboolean('MonitorCoins','moni'+key)
    except:
        continue

# Read target diff to notify
for key in coins:
    try:
        coins[key].targetDiff = Config.get('targetDifficult','tarDiff'+key)
    except:
        continue

# Read token from config file
try:
    ACCESS_TOKEN = Config.get('TOKEN','Acc_TOKEN')
    print(ACCESS_TOKEN)
except:
    pass

# Read timescan from config file
try:
    timescan = Config.get('looptime','timescan')
except:
    pass

def getDiffApiRVN():
    key = 'rvn'
    urlRvnApi = 'http://rvnhodl.com/api/getdifficulty'
    req = urllib.request.Request(urlRvnApi)
    opener = urllib.request.build_opener()
    f = opener.open(req, timeout=5)
    diffRVN = json.load(f)
    coins[key].difficulty = diffRVN
    #print(diffRVN)

def getDiffApiETH():
    key = 'eth'
    class AppURLopener(urllib.request.FancyURLopener):
        version = "Mozilla/5.0"
    opener = AppURLopener()
    response = opener.open('https://api.ethermine.org/networkStats')
    apiDiff = json.load(response)
    rawdiff = apiDiff['data']
    diffETH = rawdiff['difficulty']
    coins[key].difficulty = diffETH
    #print(diffETH)

def getDiffApiETC():
    key = 'etc'
    class AppURLopener(urllib.request.FancyURLopener):
        version = "Mozilla/5.0"
    opener = AppURLopener()
    response = opener.open('https://api-etc.ethermine.org/networkStats')
    apiDiff = json.load(response)
    rawdiff = apiDiff['data']
    diffETC = rawdiff['difficulty']
    coins[key].difficulty = diffETC
    #print(diffETC)


notify = LineNotify(ACCESS_TOKEN)


while True:
    getDiffApiRVN()
    #getDiffApiETH()
    #getDiffApiETC()
    for key in coins:
        if coins[key].willingtomonitor == True :
            print("Coin notify : "+coins[key].name)
            if float(coins[key].difficulty) <= float(coins[key].targetDiff) :
                print(coins[key].difficulty)
                print(coins[key].targetDiff)
                notify.send(key+" Diff: "+str(coins[key].difficulty))
                #tmin = int(timescan) / 60
                #notify.send("time scan : " + str(timescan) + " sec = " + str(tmin) + " min ")
                #notify.send("date: "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

    #delay (sec)
    time.sleep(int(timescan))
