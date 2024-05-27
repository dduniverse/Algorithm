const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input, a, b;

rl.on('line', function (line) {
    input = line.split(' ');
    rl.close();
}).on('close', function () {
    a = input[0]
    b = input[1]
    console.log("a =", a)
    console.log("b =", b)
    process.exit()
    
});