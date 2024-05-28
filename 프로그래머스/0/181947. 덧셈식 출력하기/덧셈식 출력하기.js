const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
    const [a, b] = [input[0], input[1]];
    const answer = Number(a) + Number(b);
    console.log(`${a} + ${b} = ${answer}`);
});