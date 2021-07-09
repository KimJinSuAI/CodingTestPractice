def solution(n, words):
    stck = []
    stck.append(words[0])
    for i in range(1, len(words)):
        if words[i] in stck or words[i][0]!=stck[-1][-1]:
            return [i%n+1,i//n+1]
        else:
            stck.append(words[i])

    return [0,0]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))