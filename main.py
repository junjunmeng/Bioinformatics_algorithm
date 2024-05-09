def PatternCount(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern)+ 1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count



def friends(rels):
    fs = dict()
    for r in rels:
        if len(r) == 1:
            fs[r[0]] = 0
        else:     
            fs[r[0]] =+ 1 
            fs[r[1]] =+ 1
    return fs

rels = [[1,3],[3,5],[4], [1,5]] 
