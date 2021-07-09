def solution(files):
    txt = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .-"
    num = "0123456789"
    file = []
    
    for i in range(len(files)):
        index = 0
        head = ""
        number = ""
        for j in range(len(files[i])):
            if files[i][j] in txt:
                head += files[i][j]
            else:
                break
        for k in range(j,len(files[i])):
            if files[i][k] in num:
                number+= files[i][k]
            else:
                break
        if files[i][k] not in number:
            file.append([head,number,files[i][k:],i])
        else:
            file.append([head,number,"",i])
    file = sorted(file, key = lambda x:(x[0].lower(),int(x[1]),x[3]))
    for i in range(len(file)):
        file[i] = ''.join(file[i][:-1])
    return file

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]), ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"])
print()