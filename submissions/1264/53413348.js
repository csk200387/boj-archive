let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split("\n");
for (var i = 0; i < input.length-1; i++) {
    console.log(input[i].length - (input[i].replace(/[aeiouAEIOU]/g, "")).length);
}