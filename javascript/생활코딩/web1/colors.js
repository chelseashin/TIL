//   객체화 - Links, Body
var Links = {
    setColor: function (color){
        // var alist = document.querySelectorAll('a');
        // var i = 0;
        // while(i < alist.length){
        // alist[i].style.color = color;
        // i = i + 1;
        // }
        // 모든 a태그를 jQuery로 제어하겠다는 뜻 - 위와 같은 기능을 함
        $('a').css('color', color);
    }
}
var Body = {
setColor: function (color){
    // document.querySelector('body').style.color = color;
    // jQuery로 표현
    $('body').css('color', color);
},
setBackgroundColor: function (color) {
    // document.querySelector('body').style.backgroundColor = color;
    $('body').css('backgroundColor', color);
    }
}
function nightDayHandler(self){
var target = document.querySelector('body');
if(self.value === 'night'){
  Body.setBackgroundColor('black');
  Body.setColor('white');
  self.value = 'day';
  Links.setColor('pink');
} else {
  Body.setBackgroundColor('white');
  Body.setColor('black');
  self.value = 'night';
  Links.setColor('crimson');
}
}