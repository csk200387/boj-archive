let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString();
let a = input.charCodeAt();

console.log(84 + Math.abs(a-73));