# -*- coding: utf-8 -*-
# flask run --host 0.0.0.0 --port 8080
from flask import Flask, render_template, request
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

#variable routing
@app.route("/hello/<string:name>")
def hellojy(name) :
    return render_template("hello.html", n=name)

# https://~~c9.io/cube/숫자
#제곱한 결과를 출력
@app.route("/cube/<int:num>")
def square(num) :
    return render_template("square.html", num=num*num)
    
@app.route("/christmas")
def christmas() :
    christmas=""
    if datetime.today().strftime("%m%d") =="1225" :
        christmas = "메리 크리스마스~!"
    else :
        christmas = "응 아니야 정신차려~"
    return render_template("christmas.html", christmas=christmas)

@app.route("/lunch")
def lunch() :
    lunch_box = ["20층","김밥카페","양자강","바스버거","시골집"]
    lunch = random.choice(lunch_box)
    return render_template("lunch.html", lunch=lunch, box=lunch_box)
    
@app.route("/myrandom")
def myRandom() :
    category = ["한식","중식","일식","양식"]
    koreaFood = ["갈비탕","김치찌개","삼겹살","비빔밥"]
    chinaFood = ["마파두부","짜장면","탕수육","짬뽕"]
    japanFood = ["스시","사시미","규카츠","우동"]
    westFood = ["스테이크","파스타","토스트","햄버거"]
    
    choiseCategory = random.choice(category)
    choiseFood = ""
    if choiseCategory == "한식" :
        choiseFood = random.choice(koreaFood)
    elif choiseCategory == "중식" :
        choiseFood = random.choice(chinaFood)
    elif choiseCategory == "일식" :
        choiseFood = random.choice(japanFood)
    elif choiseCategory == "양식" :
        choiseFood = random.choice(westFood)
        
    return render_template("myrandom.html", randCategory=choiseCategory, randFood = choiseFood)
    
@app.route("/google")
def google() :
    return render_template("google.html")
    
@app.route("/opgg")
def opgg() :
   
    return render_template("opgg.html")
    
@app.route("/opggresult")
def opggresult() :
    name = request.args.get('q')
    url = 'http://www.op.gg/summoner/userName={}'.format(name)
    result = requests.get(url)
    bs4 = BeautifulSoup(result.content,"html.parser")
    
    tier = bs4.select_one('div.TierRank > span.tierRank').text
    point = bs4.select_one('div.TierInfo > span.LeaguePoints').text
    wins = bs4.select_one('div.TierInfo > span.WinLose > span.wins').text
    losses = bs4.select_one('div.TierInfo > span.WinLose > span.losses').text
    ratio = bs4.select_one('div.TierInfo > span.WinLose > span.winratio').text
    
    return render_template("opggresult.html", name = name, wins = wins)

