const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input;
let answer = '';

rl.on('line', function (line) {
    input = line;
    rl.close();
}).on('close',function(){
    for (i=0; i<input.length; i++) {
        if (input[i] == input[i].toUpperCase()) {
            answer += input[i].toLowerCase();
        } else {
            answer += input[i].toUpperCase();
        }
    }
    console.log(answer);
    process.exit();
});