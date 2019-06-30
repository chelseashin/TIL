// let 블록 스코프 예제
// 다른 스코프에 있기 때문에 할당 가능
// {
//     let x = '정운지'
//     console.log(x)    // 정운지
//     {
//         let x = 1
//         console.log(x)    // 1
//     }
//     console.log(x)    // 정운지
// }
// // console.log(x)    // Error
// console.log(typeof x)    // undefined - 할당 or 선언되지 않았기 때문

// 전역 변수의 오염 - var로 쓰는 것보다 let이나 const를 쓰는 것이 좋다.
// 전역변수는 신중하게 써야 함!

// var로 선언하면 현재 스코프(유효범위) 안이라면 어디서든 사용할 수 있으며, 심지어 선언하기도 전에 사용할 수 있다.
// let으로 선언하면 그 변수는 선언하기 전에는 존재하지 않는다.

// let foo
// let bar = undefined

// foo    // undefined
// bar    // undefined

// baz    // ReferenceError bas is not defined


// // 우리가 이해한 코드
// y
// var y = 1
// y

// // JS가 이해한 코드
// // hoisting
// // var y
// // y = 1     // 1
// // y

// if (x !== 1) {
//     console.log(y)   // undefined
//     var y = 3
//     if (y === 3) {
//         var x = 1
//     }
//     console.log(y)    // 3
// }
// if (x === 1) {
//     console.log(y)    // 3
// }

// // var로 변수를 선언하면 JS는 같은 변수를 여러번 정의하더라도 무시한다
// var x = 1
// if (x === 1) {
//     var x = 2
//     console.log(x)    // 2
// }
// console.log(x)    // 2

// //JS 이해
// var x
// x = 1

// if (x === 1) {
//     x = 2
//     console.log(x)
// }
// console.log(x)


// 함수 hoisting
// ssafy 함수가 선언되기 전에 ssafy()로 호출된 형태
ssafy()
function ssafy () {
    console.log('hoisting!!!!')
}

// 변수에 할당한 함수는 호이스팅 되지 않는다.
var ssafy = function() {
    console.log('hoisting!!')
}