// while
let i = 0;
while (i < 10){
    console.log(i)
    i++
}

// for
for (let j=0; j < 10; j++) {
    console.log(j)
}

// 배열
let myArray = [1, 2, 3]
for (let k=0; k < 3; k++) {
    console.log(myArray[k])
}
// 또는 for of : 배열 반복문 사용
let myArray = [1, 2, 3]
for (let k of myArray) {
    console.log(k)
}
// let 대신에 const를 써도 동일하게 동작한다.
// 대신에 k에 재할당이 불가능하다.
let myArray = [1, 2, 3]
for (const k of myArray) {
    console.log(k)
}
// 무슨 말이냐면
for (const k of myArray) {
    k = k + 5 // 이런 행위가 불가능하다는 뜻
    console.log(k)
}