Daily Workshop

대전 2반 17번 신채원

2019-01-11



< Flask >

##### # Flask에서 Dictionary 자료형을 이용하여 다음 조건을 만족하는 ‘나만의 영어 단어장’ 페이지를 만들어보세요.


```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/dictionary/<string:word>")
def dictionary(word):
    word_dict = {'orange':'오렌지', 'apple' : '사과'}
    return render_template('word.html', word = word, word_dict = word_dict)


if __name__ == '__main__':
   app.run(host='127.0.0.1', port=5000, debug = True)

```

```python
# word.html
{% if word in word_dict %}
    <h1>{{ word }}는 {{word_dict[word]}}입니다.</h1>
{% else %}
    <h3>{{ word }}는 없는 단어입니다.</h3>
{% endif %}
```

