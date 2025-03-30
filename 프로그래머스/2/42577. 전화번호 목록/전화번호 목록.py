def solution(phone_book):
    hash = {}
    
    for phone in phone_book:
        hash[phone] = phone
        
    sorted_phone_book = sorted(phone_book, reverse=True, key=len)
    
    for book in sorted_phone_book:
        for i in range(len(book)):
            got = hash.get(book[:i+1])
            if (got != None and got != book):
                return False
            
    return True