const readline = require('readline'); // readline 모듈 불러오기
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
}); // readline 인터페이스 생성

let input;

rl.on('line', function (line) {
    // 입력값 처리 코드
    input = line;
    rl.close(); // 인터페이스를 종료하여 무한히 입력 받는 것을 방지
}).on('close',function(){
    // 입력이후 처리 코드
    console.log(input)
    process.exit(); // 프로세스 종료
});