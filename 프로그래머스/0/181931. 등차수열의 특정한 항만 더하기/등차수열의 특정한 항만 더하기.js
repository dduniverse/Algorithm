function solution(a, d, included) {
    const n = included.length;
    let answer = 0;
    for (let i=0; i<n; i++) {
        if (included[i]) {
            answer += a + d * i;
        }
    }
    return answer;
}