function solution(arr, queries) {
    for(let querie of queries) {
        const [i, j] = querie;
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr
}