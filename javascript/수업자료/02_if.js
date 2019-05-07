const firstName = 'happy'
    const lastName = "hacking"
    const name = firstName + lastName
    // document.write('<h1>' + name + '</h1>')
    // 키보드에서 숫자 1 왼쪽에 있는 (`)으로 감싼다.
    // ES6+ 문법: Template Literal(템플릿 문자열이라고 한다.)
    document.write(`<h1> ${name} </h1>`)

    // prompt는 파이썬에서의 input이라고 할 수 있다.
    let userName = prompt('너 누구니?')
    let message = `<h1> ${userName} </h1>`
    // document.write(message)

    // === : 일치함을 비교 (값, 타입)
    // == : 동등함을 비교(값) : 타입이 암묵적 변환
    // 123 == '123 : ture   (JS에서는 true와 false 모두 소문자를 사용한다.)
    // !==
    // !=
    if (userName === '빵글'){
        message = `<h1>${userName}이 안녕</h1>`
    } else if (userName === '동글'){
        message = `<h1>${userName}이 안녕</h1>`
    } else {
        message = `<h1> 안녕하세요 </h1>`
    }
    document.write(message)