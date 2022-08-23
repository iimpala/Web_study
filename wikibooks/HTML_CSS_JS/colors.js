var Body = {
    setColor : function(color){
        $('body').css('color', color);
        // document.querySelector('body').style.color = color;
    },

    setBackgroundColor : function(color){
        $('body').css('backgroundColor', color);
        // document.querySelector('body').style.backgroundColor = color;
    }

}

var Link = {
    setColor : function(color){
        $('a').css('color', color);
        // var alist = document.querySelectorAll('a');
        // var i = 0;
        // while(i < alist.length) {
        //     alist[i].style.color = color;
        //     i = i + 1;
        // }
    }
}

function nightDayHandler(self){
    var target = document.querySelector('body');
    if(self.value === 'night') {
        self.value = 'day';
        Body.setBackgroundColor('black');
        Body.setColor('white');
        Link.setColor('powderblue');               
    }
    else {
        self.value = 'night';
        Body.setBackgroundColor('white');
        Body.setColor('black');
        Link.setColor('blue');
    }
}