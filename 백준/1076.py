a={"black":0,"brown":1,"red":2,"orange":3,
"yellow":4, "green":5, "blue":6, "violet":7,
"grey":8, "white":9}
x=""
for i in range(3):
    x+=str(a.get(input()))
print(int(x[:2])*pow(10,int(x[2])))