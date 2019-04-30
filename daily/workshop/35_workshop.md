Workshop

대전 2반 17번 신채원

2019-04-30

< JS & ES6 >

Background

*  JS 기초 문법 학습. 
*  기존 Python 코드의 추상화 된 핵심 이해.

* python기초 개념코드를 JS코드로 번역



< Problem >

* 아래 Python 코드를 JS 코드로 변환해보자.. 
* Checkpoint 
  1. 브라우저는 생각하지 않는다.
  2. 변수/함수 이름은 JS naming convention(lowerCamelCase) 을 따른다. 
  3. F String => Template Literal.

![image](https://user-images.githubusercontent.com/45935233/56943624-57c16980-6b5b-11e9-8cd1-84aa99ff49c7.png)



```javascript
const conCat = (str1, str2) => `${str1}-${str2}`

const checkLongStr = string => {
    if (string.length > 10) {
        return true
    } else {
    return false
    }
}

if (checkLongStr(conCat('Happy', 'Hacking'))) {
    console.log('Long String')
} else {
    console.log('Short String')
}
```

