from functools import cmp_to_key

def comparer(a,b):
    if (a[2] == b[2]):
        if a[0] > b[0]:
            return 1
        else:
            return -1
    else:
        if a[2] < b[2]:
            return 1
        else:
            return -1

class GenreObject:
    count = 0
    songs = []
    def __init__(self, _count, _songs):
        self.count = _count
        self.songs = _songs


def solution(genres, plays):
    answer = []
    hash = {}
    
    #데이터 담기
    for i in range(len(plays)):
        genre = genres[i]
        play = plays[i]
        if not hash.get(genre):
            hash[genre] = GenreObject(0, [])
        
        hash[genre].count += play
        hash[genre].songs.append([i, genre, play])
        
    
    sorted_genre_objects = sorted(list(hash.values()), key=lambda x: x.count, reverse=True)
    
    for genre_object in sorted_genre_objects:
        sorted_songs = sorted(genre_object.songs, key=cmp_to_key(comparer))
        answer.append(sorted_songs[0][0])
        if (len(sorted_songs) > 1): answer.append(sorted_songs[1][0])
    
    return answer