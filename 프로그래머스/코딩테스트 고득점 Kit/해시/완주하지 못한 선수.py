from collections import Counter
def solution(participant, completion):
    return list(Counter(participant)-Counter(completion))[0]
print(solution(["leo", "kiki", "eden"],["kiki", "eden"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["marina", "josipa", "nikola", "filipa"]))
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "mislav", "ana"]))