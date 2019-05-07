// "JS는 DOM 조작이 주 기능이므로 다음의 기능들이 있어도 잘 안쓴다."

        // 파이썬처럼 -1로 맨 뒤에값 참조 불능
        // 인덱싱은 [x]로 가능
        // numbers.length로 배열 길이 참조 가능
        // numbers.reverse() 원본 자체를 뒤집는다
        let numbers = [1,2,3,4]
        
        numbers[0]      // 인덱싱
        numbers[0, 2]   // ?
        numbers.length  // 배열 길이 반환
        
        numbers.reverse()
        numbers.push('hello')
        numbers.pop()   // 값을 뺀 후의 배열 길이 리턴
        numbers.pop(4)  // 뭘 넣어도 맨 뒤에 값을 뺌 - 값을 넣은 후의 배열 길이 리턴
        
        numbers.includes(3) // 값이 있는지 없는지 체크
        numbers.join('-')   // 배열 내부 값들 이어줌
        numbers.indexOf(1)  // 없는 값은 -1을 리턴, 잆는 값은 해당 값의 위치 (0부터 시작)
        
        numbers.shift()     // 맨 앞에 값을 뺀다.     - 현재 배열 길이 리턴
        numbers.unshift(1)  // 맨 앞에 값을 넣어준다. - 현재 배열 길이 리턴
        
        numbers.sort()      // 정렬. 원본자체가 바뀐다.

        numbers.slice(0, 3)     // 어디서 시작할 것이고, 어디까지 자를 것인지
        numbers.slice(-2)       // 뒤에서부터 두 개 자르기
        numbers.slice(0, 100)   // 오류 안 뜨고 배열 길이 넘치게 요청해도 현재 요청 위치에서부터 끝까지 가져옴
        