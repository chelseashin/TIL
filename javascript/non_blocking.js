// const nothing = () => {}

// console.log('start sleeping')
// setTimeout(nothing, 3000)     // non-block callback stack
// console.log('end of program')

// python code와 동일하게 동작
// const logEnd = () => {
//     console.log('end of program')
// }
// console.log('start sleeping')
// setTimeout(logEnd, 3000)


// function first() {
//     console.log('first')
// }

// function second() {
//     console.log('second')
// }

// function third() {
//     console.log('third')
// }

// first()
// setTimeout(second, 5000)    // 5초 쉬었다가
// third()


// func1()를 호출했을 때, 아래와 같이 콘솔에 출력
// func1
// func2
// func3


// 1
// function func1() {
//     console.log('func1')
//     func3()
//     func2()
// }

// function func2() {
//     console.log('func2')
// }

// function func3() {
//     console.log('func3')
// }

// func1()


// 2
function func1() {
    console.log('func1')
    func2()
}

function func2() {
    setTimeout(() => console.log('func2'), 0)
    func3()
}

function func3() {
    console.log('func3')
}

func1()
