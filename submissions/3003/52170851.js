let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split(" ");
let arr = [1, 1, 2, 2, 2, 8];
let res = [];
for (let i = 0; i < 6; i++) {
    res.push(arr[i] - input[i]);
}
console.log(res.join(" "));