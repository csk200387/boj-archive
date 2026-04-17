let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

for (let i = 1; i <= input[0]; i++) {
    let tmp = input[i].split(" ");
    let sliceNum = parseInt(tmp[0]);
    let res = tmp[1].slice(0,sliceNum-1)+tmp[1].slice(sliceNum);
    console.log(res);
}