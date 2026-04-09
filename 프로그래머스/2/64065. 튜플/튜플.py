

def solution(s):
    s = s[1:-1]
    splitted = s.split("},")
    datas = []
    for tup in splitted:
        cleaned_data = tup.replace("{", "").replace("}", "")
        datas.append(list(map(int, cleaned_data.split(","))))
    answer = []
    datas.sort(key=lambda x: len(x))
    for tup in datas:
        for elem in tup:
            if elem not in answer:
                answer.append(elem)
                break
    
    return answer