// 1. 배열 반복하면서 출력
        const avengers = ['헐크', '아이언맨', '토르', '헐크', '스파이더맨', '블랙위도우', '닥터스트레인지'];
        
        avengers.forEach(function(avenger, index) { // 1. 함수 표현식
                console.log(avenger, index)
        });
        avengers.forEach( avenger => {              // 2. Arrow function
            console.log(avenger)
        })

        /* forEach 함수 사용법 by MDN Mozilla

            arr.forEach(function callback(currentValue [, index [, array]]) {
                //your iterator
            }[, thisArg]);

        */

        // 2. map (기존에 파이썬에서 사용했던 map과 정확하게 동일하다.)
        const numbers = [1, 2, 3]
        const stringNumbers = numbers.map(number => 
                                   String(number)
                                )
        console.log(stringNumbers)        
        const squareNumbers = numbers.map(number => number*number)
        console.log(squareNumbers)

        const minkyo = [
            {'velocity': 40, 'time':50},
            {'velocity': 200, 'time':75},
            {'velocity': 100, 'time':6},
        ]
        // const여도 값 할당이 가능한데, 메모리의 주소가 안바뀌는 것이지 그 값 자체는 바뀔 수가 있다.
        const distance = [] 
        minkyo.forEach(function(each){
            distance.push(each.velocity*each.time)
        })
        console.log(distance)

        // map을 사용하면...
        const distance2 = minkyo.map(function(obj){
            let distance = obj.velocity*obj.time
            return distance
        })
        console.log(distance2)

        // 3. filter
        // 반복문을 돌면서 true인 것들만 모아서 배열로 만들어준다!
        const nums = [1,2,3,5,7]
        const evenNumbers = nums.filter(num => num% 2 === 0)
        console.log(evenNumbers)
        const oddNumbers = nums.filter(num => num% 2 === 1)
        console.log(oddNumbers)

        const drinks = [
            {'type' : 'caffeine', 'name' : 'cold brew'},
            {'type' : 'caffeine', 'name' : 'iced latte'},
            {'type' : 'juice', 'name' : 'orange'},
            {'type' : 'juice', 'name' : 'apple'},
        ]
        const juices = drinks.filter(drink => drink.type === 'juice')
        console.log(juices)
        // 오브젝트를 넘겨주므로, 이름만 뽑고싶으면 map을 써주면 된다.
        const juicesName = drinks.filter(drink => drink.type === 'juice')
                                                    .map(drink => drink.name)
        console.log(juicesName)

        // 4. reduce
        // 배열 내에 존재하는 각 요소에 대해 callback 함수를 한 번씩 실행하는데,
        // 각각의 결과값을 최종적으로 하나의 변수에 담아서 반환해준다.
        // 스크립트 언어에서는 많이 지원하는 형식. 파이썬에서도 존재한다.
        const reduceNum = [1, 5, 6]
        const reduceResult = reduceNum.reduce((acc, num) => {
            return acc + num*10
        }, 0)   // 첫번째 인자의 인덱스를 넘겨줘야 1번째 부터 계산을 한다. Initial Value를 넘겨줘야함.
        console.log(reduceResult);

        // 5. find
        const dc = ['슈퍼맨', '배트맨', '조커']
        const badguy = dc.find(name => name === '조커')
        console.log(badguy);
