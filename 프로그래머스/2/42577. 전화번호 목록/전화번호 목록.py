def solution(phone_book):
    hash = {}
    for phone in phone_book:
        hash[phone] = 1
        
    for data in phone_book:
        temp = ""
        for num in data:
            temp += num
            if (temp in hash and temp != data):
                return False
            
    return True