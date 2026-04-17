let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim();
let year = parseInt(input);

if (year % 4 == 0) {
    if (y % 400 != 0 && y % 100 == 0) {
        console.log(0);
    }
    else {
        console.log(1);
    }
}
else {
    console.log(0);
}