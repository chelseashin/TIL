2019-01-31

< Flask >

* flask response request

  fake google / pingpong / GET&POST / OP.GG

* flask csv

  DictWriter / DictReade / 방명록 만들기

* SQL (CRUD)


```python
from flask import Flask, render_template, request, redirect
import os
import datetime
import requests
from bs4 import BeautifulSoup
import csv

app = Flask(__name__)

# 이름 부르기    
 @app.route('/hi/<string:name>')    
 def greeting(name):
     return render_template('greeting.html', html_name=name)
    
# @app.route('/movie')
 def movie():
     movies = ['극한직업', '정글북', '캡틴마블', '보헤미안랩소디', '완벽한타인']
     return render_template('movie.html', movie=movies)
    
 # fake google
 @app.route('/google')
 def google():
     return render_template('google.html')

# pingpong
 @app.route('/ping')
 def ping():
     return render_template('ping.html')
    
# @app.route('/pong')    
 def pong():
     name = request.args.get('name')
     # name = request.args['name']    틀리면 에러메세지를 뿜기 때문에 선호 X
     msg = request.args.get('msg')
     return render_template('pong.html', name=name, msg=msg) #바로 위에 request로 받은 것
    
# @app.route("/ping_new")
 def ping_new():
     return render_template('ping_new.html')
    
# @app.route("/pong_new", methods=['POST'])
 def pong_new():
     # name = request.args['name']
     name = request.form.get('name')
     msg = request.form.get('msg')
     return render_template('pong_new.html', name=name, msg=msg)


@app.route('/opgg')
def opgg():
    return render_template('opgg.html')
    
@app.route('/opgg_result')
def opgg_result():
    url = "http://www.op.gg/summoner/userName="
    username = request.args.get('username')
    response = requests.get(url+username).text
    soup = BeautifulSoup(response, 'html.parser')

    wins = soup.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins")
    loses = soup.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses")
    return render_template('opgg_result.html', username = username, wins = wins.text, loses = loses.text)


# CSV
@app.route('/timeline')
def timeline():
    
    # 지금까지 입력된 방명록들을 보여주자
    with open('timeline.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        new = []
        for row in reader:
            new.append((row['username'], row['message']))
            
    # with open('timeline.csv', 'r', newline='', encoding='utf-8') as f:
        # reader = csv.DictReader(f)
        # new = []
        # for row in reader:
        #     timelines.append((row['username'], row['message']))

    return render_template('timeline.html', new=new)
    

@app.route('/timeline_create')
def timeline_create():
    username = request.args.get('username')
    message = request.args.get('message')
    
    with open('timeline.csv', 'a', newline='', encoding='utf-8') as f:   
        # 덮어써지지 않게 하기 위해 a(add)를 사용!
        fieldnames = ('username', 'message')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        # writer = csv.DictWriter(f, fieldnames=['username', 'message'])
        
        writer.writerow({
            'username': username, 
            'message': message
        })
        
        # return page를 다시 넘김(페이지 넘김없이 바로 입력값 아래에 추가됨)
        return redirect('/timeline') 
        # return render_template('timeline_create.html', username=username, message=message)
       
    
# 항상 마지막에 위치
if __name__ == "__main__":
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)  
    # c9 열어놓은 ip찾아옴

```



```python
<!-- 내 이름이 들어오면, 다른 사람이름이 들어오면 -->
<!-- greeting.html -->
<!DOCTYPE HTML>
<html>
  <head>
    <title>Flask app</title>
  </head>
  <body>
    {% if html_name == "채원" %}
      <h1>안녕, {{ html_name }}아 왔니?</h1>
    {% else %}
      <h1>{{ html_name }}, 너는 누구야?</h1>
    {% endif %}
  </body>
</html>
```



```python
<!-- google.html -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>

<body>
    <form action="https://www.google.co.kr/search" target="_blank">
        <input type="text" name="q">
        <input type="submit" value="search">
    </form>
</body>

</html>
```



```python
# opgg.html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" 
</head>

<body>
    <div class="contents-center bg-primary">
        <form action="/opgg_result" target="_blank">
            <input type="text" name="username">
            <input type="submit" name="search">
        </form>
    </div>

</body>

</html>

# opgg_result.html
<h1>{{username}}의 전적은 {{wins}} {{loses}} 입니다.</h1>
```



```python
# timeline.html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>

<body>
    <form action="/timeline_create">
        <input type="text" name="username">
        <input type="text" name="message">
        <input type="submit" value="submit">
    </form>
    <!--flask에서 받은 객체(딕셔너리형태)를 받아서 반복문으로 출력-->
    {% for row in new %}
    <ul>
        <li> {{ row[0] }} : {{ row[1] }} </li>
    </ul>
    {% endfor %}
    
    <!--<ul>-->
    <!--    <li>{{timeline.username}} : {{timeline.message}}</li>-->
    <!--</ul>-->
</body>

</html>
```



```python

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <ul>
        <li>{{ username }} : {{ message }}</li>
    </ul>
</body>
</html>
```







