from bs4 import BeautifulSoup
import requests


url = 'http://www.op.gg/summoner/userName=hide on bush'
result = requests.get(url)
bs4 = BeautifulSoup(result.content,"html.parser")

tier = bs4.select_one('div.TierRank > span.tierRank').text
point = bs4.select_one('div.TierInfo > span.LeaguePoints').text
wins = bs4.select_one('div.TierInfo > span.WinLose > span.wins').text
losses = bs4.select_one('div.TierInfo > span.WinLose > span.losses').text
ratio = bs4.select_one('div.TierInfo > span.WinLose > span.winratio').text

print(wins)
print(losses)
print(ratio)