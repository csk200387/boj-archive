let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n").map(Number);
for (let i = 0; i < input.length; i++) {
    if(!input.includes(i)) {
        console.log(i);
    }
}