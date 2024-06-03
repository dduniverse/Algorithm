function solution(num_list) {
    let sum = 0;
    let mul = 1;
    
    for (let i=0; i<num_list.length; i++) {
        sum += num_list[i]
        mul *= num_list[i]
    }

    return sum ** 2 > mul ? 1 : 0 
}