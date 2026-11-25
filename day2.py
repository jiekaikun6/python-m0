
#while条件适合明确知道第几次结束循坏的场景
#while true+break适合不能知道具体要循坏几次，猜数字不知道哪次能猜对，只能一直循坏，直到猜对，break结束，agent也一样，直到模型反馈不需要调动工具了再break结束

#结束条件能不能在循环开头判断？能 → while 条件；必须先在循环体里做一步才知道 → while True + break。

import random
n=random.randint(1,100)
k=0
while True:
    s=int(input("请输入："))
    k+=1
    if n>s:
        print("猜小了")
    elif n<s:
        print("猜大了")
    else:
        print("猜对了",k)
        break

for i in range(1,10):
    for j in range(1,i+1):
            print(f"{j}*{i}={i*j}",end="\t")
    print()




age = 20
if age>=18:
    print("成年")
elif age>=12:
    print("少年")
else:
    print("儿童")

#while 适合"我不知道转几次，转到某个条件满足为止"
count = 0
while count<5:
    print(count)
    count=count+1

coun =9
while coun>2:
    print(coun)
    coun-=1

#for 循环适合"我知道要转几次/要遍历谁"
for i in range(1,5):
    print(i)  #输出1234

for y in "abcd":
    print(y)

for k in range(1,10,2):
    print(k)#输出13579

print("-------------------------------------")

#break：砸掉整个循环，跳到循环外面继续。
#continue：只放弃这一轮，循环本身继续。
for i in range(1,10):
    if i==5:
        break
    if i%2==0:
        continue
    print(i)
print("-------------------------------------")
for k in range(1,10):
    if k==9:
        break
    if k/2==1:
        continue
    print(k)
