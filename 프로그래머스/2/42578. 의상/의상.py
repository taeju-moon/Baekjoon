def solution(clothes):
    hash = {}
    for cloth in clothes:
        gotHash = hash.get(cloth[1])
        if gotHash == None:
            hash[cloth[1]] = [cloth[0]]
        if gotHash != None and cloth[0] not in gotHash:
            hash[cloth[1]].append(cloth[0])

    combi = 1
    hash_keys_len = len(hash.keys())
    if (hash_keys_len == 1):
        for key in hash:
            combi = combi * len(hash[key])
    else:
        for key in hash:
            combi = combi * (len(hash[key])+1)

    if (hash_keys_len != 1):
        combi -= 1

    return combi