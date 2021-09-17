import re
def solution(word, pages):
    score = {}
    word = word.lower()

    for i,page in enumerate(pages):

        nowPage = ""
        meta = re.findall('<meta.*"',page[page.find("<head>"):page.find("</head>")])
        for m in meta:
            tmp = m.find("https://")
            if tmp!=-1:
                nowPage = m[tmp:]
                break
        score[nowPage] = [0,[],0, i]       #기본(매칭), 외부링크들, 외부링크점수, 인덱스

        page = page.lower()
        score[nowPage][0] = re.sub('[^a-z]+', '.', page.lower()).split('.').count(word.lower())#문자아닌 문자들을 모두 .으로 치환후 .을 기준으로 분리...!!!!!!!!

        
        a = re.findall('<a href="\S+"', page)                           # 공백이 있다고..??
        for elink in a:
            score[nowPage][1].append(elink[elink.find("https://"):])

    for key in score.keys():
        for elink in score[key][1]:
            if score.get(elink,False):
                score[elink][2]+=score[key][0]/len(score[key][1])
    for key in score.keys():
        score[key][0]+=score[key][2]
    
    return(sorted(score.values(), key = lambda x: (-x[0],x[3])))[0][3]

            


print(solution("blind",
    ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
))

print(solution("Muzi", ["MuziMuzi <html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))