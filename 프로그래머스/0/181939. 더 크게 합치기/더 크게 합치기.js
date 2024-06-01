function solution(a, b) {
    var answer = 0;
    
    const case1 = Number(String(a) + String(b));
    const case2 = Number(String(b) + String(a));
    
    if (case1 >= case2) {
        answer = case1;
    } else {
        answer = case2;
    }
    
    return answer;
}