function solution(my_string, overwrite_string, s) {
    var answer = '';
    
    // 6번 케이스 실패
    // var m = overwrite_string.length;
    // var replace_str = my_string.substr(s, m) // 교체해야 하는 부분
    // answer = my_string.replace(replace_str, overwrite_string);
    // return answer
    
    let str = [...my_string];
    var m = overwrite_string.length;
    str.splice(s, m, overwrite_string);
    str = str.join('');
    return str;
}