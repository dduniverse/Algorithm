function solution(ineq, eq, n, m) {
    var answer;
    
    if (ineq + eq == '>=') { answer = (n >= m) }
    if (ineq + eq == '<=') { answer = (n <= m) }
    if (ineq + eq == '>!') { answer = (n > m) }
    if (ineq + eq == '<!') { answer = (n < m) }
    
    if (answer) {
        return 1
    } else {
        return 0
    }
}