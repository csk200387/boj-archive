const fs = require('fs');
const input = fs.readFileSync("/dev/stdin").toString().trim().split(" ");
var a = input.split(" ")[0];
var b = input.split(" ")[1];
console.log(a/b);