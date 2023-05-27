def solution(id_list, report, k):
    dict = {i:[] for i in id_list}
    stop = {i:0 for i in id_list}
    for re in set(report):
        dict[re.split()[0]].append(re.split()[1])
        stop[re.split()[1]] += 1
    
    stop_id = []
    for key, value in stop.items():
        if value >= k:
            stop_id.append(key)
                
    answer = []
    for i in range(len(id_list)):
        temp = 0
        for s in stop_id:
            if s in dict[id_list[i]]:
                temp += 1
        answer.append(temp)
        
    return answer