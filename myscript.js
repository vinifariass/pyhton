var x = 0;

while (x < 5) {
    console.log("x is currently: " + x)

    if (x === 3) {
        console.log("x is 3!")
    }
    console.log("x is still less than 5, adding 1 to x")
    x = x + 1;
}

while ( 1 <=x && x <= 10) {
    console.log("x is currently: " + x)
    x = x + 1;
}

var word =  "ABCDEFGHIJK"

for (var i = 0; i < word.length; i++) {
    console.log(word[i])
}

var num = 0;

while (num<25){
    if(num%2!==0){
        console.log(num)
    }
    num = num + 1;
}


