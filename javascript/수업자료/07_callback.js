// 배열을 받아서 다 더해주는 함수를 작성 해주세요.
        // numberAddEach(numbers)  
        const numberAddEach = function(numbers){
            let sumResult = 0
            for(let x of numbers){
                sumResult = sumResult + x
            }
            return sumResult
        }
        console.log(numberAddEach([1,2,3]))

        // Arrow function 방식
        const numberAddEach2 = numbers => {
            let sum = 0
            for (const number of numbers){
                sum += number
            }
            return sum 
        }

        // 빼기
        const numberSubEach = numbers => {
            let sum = 0
            for (const number of numbers){
                sum -= number
            }
            return sum 
        }
        console.log(numberSubEach([1,2,3]))

        // 곱하기
        const numberMulEach = numbers => {
            let sum = 1
            for (const number of numbers){
                sum *= number
            }
            return sum 
        }
        console.log(numberMulEach([1,2,3]))

        // callback
        // callback 함수를 이용해서 위의 것들을 처리해보자
        // 함수 안의 인자로 함수를 받고 처리를 해준다.
        // 파이썬에서의 map 함수와 비슷비슷한 느낌.
        const numberEach = (numbers, calc) => {
            let result
            for (const number of numbers) {
                result = calc(number, result)
            }
            return result
        }
        const addEach = (number, result=0) => result + number
        const subEach = (number, result=0) => result - number
        const mulEach = (number, result=1) => result * number

        console.log( numberEach([1,2,3], addEach) )
        console.log( numberEach([1,2,3], subEach) )
        console.log( numberEach([1,2,3], mulEach) )

        // 그런데, 얘를 익명함수로 넘겨버리거나 또는 함수를 함수 안에서 정의해서 써버리는 경우가 있다.
        // 복잡할 수 있으나, 꼭 익숙해지고 알아둬야한다.
        console.log(numberEach([1,2,3], (number, result=0) => result + number )) // Arrow Func + 익명함수 + 콜백
        console.log(numberEach([1,2,3], function(number, result=0){
            return number + result
        } ))

        // 콜백과 관련된 반복문에서는 forEach를 많이 사용한다.
        // 어떤 메서드의 매개변수에 callback을 넘겨줘야한다면 100% 다른 함수를 넘겨준다는 말이다.
        let foods = ["빠삐코", "메로나", "스시" ] 
        foods.forEach(function(iceCream) {
	    console.log(iceCream)
        })
        foods.forEach( ice => console.log(ice) )

        // forEach는 3가지 인수를 받는다.
        // (currentValue, index, array)
        foods.forEach(function(element, idx, foods) {
	    console.log(element, idx, foods)
        })