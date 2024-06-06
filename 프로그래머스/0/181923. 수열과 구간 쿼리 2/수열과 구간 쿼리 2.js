function solution(arr, queries) {
    let answer = [];
    
    queries.forEach(([s,e,k]) => {
        let temp = Infinity;
        for(i=s; i<=e; i++) {
            if (arr[i] > k) {
                temp = Math.min(temp, arr[i]);
            }
        }
        temp < Infinity ? answer.push(temp) : answer.push(-1);
    })
    return answer
}