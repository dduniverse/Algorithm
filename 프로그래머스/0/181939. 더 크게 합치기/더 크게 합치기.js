function solution(a, b) {
    var answer = 0;   
    answer = Math.max(Number(String(a) + String(b)), Number(String(b) + String(a)))
    return answer;
}