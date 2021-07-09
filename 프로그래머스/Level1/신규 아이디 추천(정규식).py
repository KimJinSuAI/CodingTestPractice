def solution(new_id):
    new_id = new_id.lower()
    characters = "-_.abcdefghijklmnopqrstuvwxyz1234567890"
    new_id = ''.join(x for x in new_id if x in characters)
    
    while True:
        if ".." in new_id:
            new_id = new_id.replace("..",".")
        else:
            break

    if new_id[0]=='.':
        new_id = new_id[1:]

    if len(new_id)>0:    
        if new_id[-1]=='.':
            new_id = new_id[:-1]

    if len(new_id)==0:
        new_id='a'
        
    if len(new_id)>15:
        new_id = new_id[:15]
        if new_id[-1]=='.':
            new_id = new_id[:-1]
    
    while len(new_id)<3:
        new_id+=new_id[-1]
    
    return new_id
print(solution("z-+.^."))