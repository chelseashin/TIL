// 1. forEach
// forEach 함수는 아무것도 return 하지 않는다.

// ESS
var colors = ['red', 'blue', 'green', ]

for (var i = 0; i < colors.length; i++) {
    console.log(colors[i])
}

// ES6
const COLORS = ['red', 'blue', 'green', ]
COLORS.forEach(function (color) {
    console.log(color)
})

// 배열 + 메소드 + 콜백함수 순서로 작성
COLORS.forEach(color => console.log(color))

// exercise 1-1 아래 함수에 for를 forEach로 바꾸시오
// function handlePosts() {
//     const posts = [
//         {id : 23, title: 'daily news'},  
//         {id : 52, title: 'Code City'},  
//         {id : 105, title: 'The Ruby'},  
// ]
// for (let i = 0; i < posts.length; i++) {
//         savePost(posts[i])
//     }
// }

// // posts.forEach(post => console.log(post))
// posts.forEach(function(post) {
//     savePost(post)
// })


// exercise 1-2 아래 코드의 images 배열 안에 있는 정보(height, width)를 곱해,
// 넓이를 구하여 area 배열에 저장하는 코드를 forEach 헬퍼를 사용해 작성해보자

const images = [
    { height: 10, width: 30},
    { height: 20, width: 90},
    { height: 54, width: 32},
]
const areas = []

images.forEach(function (image) {
    areas.push(image.height * image.width)
})

// 2. map
// map 함수는 새로운 배열을 return 한다. (배열 요소를 변형)
// 일정한 형식의 배열을 다른 형식으로 바꿔야 할 때
// map filter는 모두 사본을 return 하며 원본 배열은 바뀌지 않는다. 

const NUMBERS = [1, 2, 3, ]

const DOUBLE_NUMBERS = NUMBERS.map(function (number) {
    return number * 2
})

// const DOUBLE_NUMBERS = NUMBERS.map(number => number * 2)

console.log(DOUBLE_NUMBERS)

// exercise 2-1 map헬퍼를 사용해, images 배열 안의 Object들만 저장되어 있는 height 배열에 저장해보자.


const images = [
    { height: 10, width: 30},
    { height: 20, width: 90},
    { height: 54, width: 32},
]

const images = ??


const trips = [
    { distance: 34, time: 10}, 
    { distance: 90, time: 50}, 
    { distance: 59, time: 25, 
]
const speeds = ??