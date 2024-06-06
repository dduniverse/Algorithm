function solution(n, control) {
    for (let c of control) {
        if (c === 'w') {n += 1}
        if (c === 's') {n -= 1}
        if (c === 'd') {n += 10}
        if (c === 'a') {n -= 10}
    }
    
    return n
}