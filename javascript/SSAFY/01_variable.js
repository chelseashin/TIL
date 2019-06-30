// 1. JS에서의 프린트 두 가지 방법.
        // alert("hello javascript!")
        console.log("hello world!");

        /* 
        2. 여러 줄 주석 처리입니다.
        */

        document.write('<h1> hello javascript! </h1>')

        // 3. DOM 조작
        // document.querySelector(TagName).innerText = "내용"

        // 4. 변수 선언 (호이스팅)
        console.log(name)   // undefined
        var name = "이빵글"

        // let을 쓰면 호이스팅 방지 가능
        console.log(minkyo)
        let minkyo = "이빵글2"

        /*
        JS는 선언된 변수들을 최상단으로 올려버린다.
        따라서 해당 변수가 호출된 시점이 선언된 시점보다 뒤에 있더라도 코드가 작동한다.
        이러한 호이스팅은 함수에도 적용이 된다.

        강사님 words:
        자바스크립트에서 모든 선언과 관련된 문장(변수, 함수 등)은 호이스팅 된다.
        변수는 1) 선언단계 2) 초기화 단계(undefined) 3) 할당 단계를 거치게 된다.
        */
        console.log(name)   // undefined
        var name
        var name = "이빵글"
        console.log(phoneNumber) // phoneNumber is not defined (ReferenceError)
        
        // 우리는 let, const만 사용할 것이다. (ES6 표준임)
        // 앞에 아무것도 붙이지 않고 할당만 할 수 있는데 얘는 전역변수를 생성하는 것.
        // 그러나 사용하지 않는다.

        // var와 let의 가장 큰 차이는 사실 scope가 다르다는 점에 있다.
        for (var i = 0; i < 3; i++){
            console.log(i)
        }
        console.log('======================')
        console.log(i)  // i 값이 3

        // let은 한정된 스코프 내에서만 해당 변수에 대한 참조가 가능하다!
        for (let j = 0; j < 3; j++){
            console.log(j)
        }
        console.log('======================')
        console.log(j)  // i 값이 없음