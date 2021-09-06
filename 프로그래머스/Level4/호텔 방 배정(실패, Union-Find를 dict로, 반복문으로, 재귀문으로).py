import sys
sys.setrecursionlimit(10**9)
def ancestor(k):
    if roomList[k-1]==k:
        roomList[k-1] = roomList[k]
        return k, roomList[k]
    else:
        answer, roomList[k-1] = ancestor(roomList[k-1])
        return answer, roomList[k-1]
def solution(k, room_number):
    global roomList
    roomList = list(range(1,k+2))
    answer = []
    for room in room_number:
        answer.append(ancestor(room)[0])
    return answer


def solution(k, room_number):
    global roomList
    roomList = list(range(1,k+2))
    answer = []
    for room in room_number:
        if roomList[room-1]==room:
            roomList[room-1] = roomList[room]
            answer.append(room)
        else:
            rooms = []
            while roomList[room-1]!=room:
                rooms.append(room-1)
                room = roomList[room-1]
            roomList[room-1] = roomList[room]
            for tmproom in rooms:
                roomList[tmproom] = roomList[room]
            answer.append(room)
    return answer



def solution(k, room_number):
    roomList = {}
    answer = []
    for room in room_number:
        if not roomList.get(room-1,False):
            roomList[room-1] = roomList.get(room,room)
            answer.append(room)
        else:
            rooms = []
            while roomList.get(room-1,False):
                rooms.append(room-1)
                room = roomList[room-1]+1
            roomList[room-1] = roomList.get(room,room)
            for tmproom in rooms:
                roomList[tmproom] = roomList.get(room,room)
            answer.append(room)
    return answer

print(solution(10**12,[1,3,4,1,3,1]))