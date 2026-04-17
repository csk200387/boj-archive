const input = require('fs').readFileSync('/dev/stdin').toString().trim();

var reg = /(100+1+|01)+/g;
if (input == str.match(reg)[0]) {
    console.log("SUBMARINE");
}
else {
    console.log("NOISE");
}