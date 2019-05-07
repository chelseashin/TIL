// 자바스크립트 데이터 타입 - 다음의 원시타입(primitive type)을 제외하곤 전부 object type이다.
        // Boolean(true, false), null, undefined, number, string

        // 자바스크립트 object 표기법
        // 여기서 키값의 경우 식별자로 인식이 안되는 (예를 들어 하이픈이라던가...)것이 이름에 들어가면
        // 따옴표로 감싸줘야한다. 그렇지 않은 경우에는 따옴표 없이 사용이 가능하다.
        let minkyo = {
            name: "minkyo",
            personality: 'nice',
            number: '010-0000-0000'
        }
        // minkyo.name 또는 minkyo["name"] 둘 다로 접근이 가능하다.
        // minkyo는 "typeof"로 찍어보면 object 타입임을 알 수 있다.
        // 따라서 위의 표기법은 JS에서의 가장 기본적인 객체 표기법이라 할 수 있다.
        // 클래스를 만들고 인스턴스를 까는 게 아니라 JS에서는 이런식으로 표기한다고 할 수 있다. 
        // CONCULSION : JSON = 자바스크립트에서의 객체 표기법

        console.log(minkyo.name)        // 'minkyo'
        console.log(minkyo.personality) // 'nice'
        console.log(minkyo.number)      // '010-0000-0000'
        console.log(typeof minkyo)      // object
        console.log(typeof [1,2,3])     // object

        // 여기 아래부터는 ES6+ 문법 - 변수자체를 넣어버리면 자동으로 객체로써 저장이 된다.
        let name = 'bbangul'
        let stuff = ['텀블러', '안경']
        let bbangul = {
            name, 
            stuff
        }

        // 위의 객체는 다음의 메서드를 사용하여 JSON화 할 수 있는데,
        let jsonData = JSON.stringify(bbangul)
        // JSON이란 사실 다음의 표기법으로 표기된 문자열이라고 할 수 있다. (큰 따옴표밖에 사용못함)
        // "{"name":"bbangul","stuff":["텀블러","안경"]}" 
        // 반대로 위와같은 JSON형식을 받았다고 하면 다음과 같이 parsing해서 사용할 수도 있다.
        let jsonParse = JSON.parse(jsonData)