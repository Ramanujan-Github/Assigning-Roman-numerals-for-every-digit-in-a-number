n=int(input("Enter number: "))
a=str(n)
d=dict()
for i in range(len(a)):
    if int(a[i])==1:
        d1={int(a[i]):"I"}
        d.update(d1)
    if int(a[i])==2:
        d2={int(a[i]):"II"}
        d.update(d2)
    if int(a[i])==3:
        d3={int(a[i]):"III"}
        d.update(d3)
    if int(a[i])==4:
        d4={int(a[i]):"IV"}
        d.update(d4)
    if int(a[i])==5:
        d5={int(a[i]):"V"}
        d.update(d5)
    if int(a[i])==6:
        d6={int(a[i]):"VI"}
        d.update(d6)
    if int(a[i])==7:
        d7={int(a[i]):"VII"}
        d.update(d7)
    if int(a[i])==8:
        d8={int(a[i]):"VIII"}
        d.update(d8)
    if int(a[i])==9:
        d9={int(a[i]):"IX"}
        d.update(d9)
    if int(a[i])==0:
        d10={int(a[i]):" "}
        d.update(d10)
print(d)