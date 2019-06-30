// 이런 식으로 함수도 호이스팅이 발생한다.
        // 1. 함수 선언식 (delcaration)
        let result = add(1, 3)
        function add(num1, num2) {
            return num1 + num2 
        }
        console.log(result)

        // 따라서 다음과 같은 함수 표현식을 사용하여 호이스팅을 방지한다.
        // 2. 함수 표현식 (exrpession) - 함수자체를 변수에 저장해서 호출하여 쓴다.
        let add2 = function (num1, num2){   // 이러한 이름이 없는 함수를 익명함수라고 한다.
                            return num1 + num2 }
        console.log(add2(1, 3))
        // console.log(add3(1, 3))  // 얘는 에러가 발생된다. function에 원래 add3라는 이름을 붙여놨었는데 뗌.

        // 3. ES6+ Arrow Function (중요) (에서는 위의 방식에서 하나의 방식이 더 추가되었다.)
        let sub = (num1, num2) => {
            return num1-num2
        }

        // 인자가 하나인 경우, () 생략 가능
        // 단순 리턴인 경우, {} 및 return 키워드 생략 가능
        let greeting = name => `${name}, 안녕!`
        console.log(greeting('빵글'))
        let mul = (num1, num2) => num1*num2
        console.log(mul(5, 3))

        // 인자가 없는 경우에는 빈 소괄호를 써주고 리턴값만 정해주면 된다.
        let hello = () => `hello, world!`
        console.log(hello())

        // object 리턴 시 object 타입 생성위해 중괄호로 묶어준 후, 소괄호로 묶어줘야 출력이 된다.
        let me = (name, age) => ({name, age})

        // Arrow Function 연습 (오늘의 홈워크 or 워크샵)
        // 함수 표현식에 재할당이 가능하면 안되므로 const사용.
        const negative = num => num*(-1)
        const gutenTag = () => "Guten Tag"
        const vietnam = member => {
            let  member_base = "이빵글"    // let안써주면 전역변수로 잡힘.
            return `${member_base}와 ${member}가 베트남에 가요!`
        }

        // 함수의 완전 람다식 표현. 정의와 동시에 호출.
        ((a, b) => a*b)(4,5)

        // 만약, default args (기본인자)를 넣어주고 싶다면
        let bonjour = (name='빵글') => `${name}, bonjour` 
        
        // 4. 익명 함수 - 이름이 없다! 즉시실행함수는 무조건 소괄호로 묶어줘야한다.
        (function (num) {return num*num})
        num => num*num // Arrow function을 이용하면...

        // 5. 즉시 실행 함수 (익명함수 + 호출) - IIFE(Immediately Invoked Function Expression)라는 이름을 가지고 있다.
        // 웹에서 변수 초기화할 때 많이 사용한다.
        let myNum1 = (function (num) {return num*num})(5)
        let myNum2 = (num => num*num)(5)