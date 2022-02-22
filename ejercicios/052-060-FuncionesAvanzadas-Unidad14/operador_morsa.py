x=8
"""
#No válido
if (x=x+2>=10):
    print("Es mayor o igual que 10")
"""
#Válido
if ((x:=x+2)>=10):
    print(x, "Es mayor o igual que 10")

x=0
while((x:=x+2)<20):
    print(x)   
