import random,time
def door():
    list=["羊","羊","汽车"]
    dict={"door1":"","door2":"","door3":""}
    random.shuffle(list)
    dict["door1"] = list[0]
    dict["door2"] = list[1]
    dict["door3"] = list[2]
    return dict

dict=door()

print("主持人：欢迎收看有奖游戏节目！...")
time.sleep(1)
print("主持人：我是主持人佩罗琪,请这位嘉宾向大家介绍一下自己吧！\n")
time.sleep(1)
name=input("大家好！我叫")
time.sleep(1)
print("主持人："+name+"，你好!欢迎参加我们这个有奖竞猜节目！\n")
time.sleep(1)
print("主持人：现在让我们开始竞猜........\n")
time.sleep(2)
print("主持人：这里有三扇门，请问你想选择哪扇门呢？\n")
time.sleep(2)

choose=int(input("1号门、2号门、3号门："))

assert choose in [1,2,3],"请输入正确的数字！！！！！！"

for i in range(1,4):
    if i==choose:
        continue
    if dict["door"+str(i)]=="羊":
        sheep_door=i



time.sleep(2)
print("主持人：好的，我们的嘉宾选择了"+str(choose)+"号门。\n")
time.sleep(2)
print("主持人：现在我来打开另一扇门\n")
time.sleep(1)
print("(...主持人正在选择一扇门打开...)\n")
time.sleep(2)
print("(...主持人打开了"+str(sheep_door)+"号门,这扇门后面是一只羊...）\n")
time.sleep(2)

for i in range(1,4):
    if i != sheep_door and i != choose:
        rest=i
print("主持人："+name+"，请问您想改选"+str(rest)+"号门吗？\n")
time.sleep(1)

change=input("改选（y），否则（n):")
assert change in ["y","n"],"请回答y or n！！！！！"



time.sleep(2)
if(change=="y"):
    print("主持人：好的，我们的嘉宾又选择了"+str(rest)+"号门\n")
    final=rest
else:
    print("主持人：我们的嘉宾非常坚信自己的选择呀，他选择的依然是" + str(choose) + "号门\n")
    final=choose
time.sleep(1)
print("主持人：那么，"+name+"这次究竟能否赢得汽车大奖呢？\n")
time.sleep(1)
print("\n(...主持人打开"+str(final)+"号门...）")
time.sleep(3)
print("(里面出现的是----"+dict["door"+str(final)]+"!)\n")
time.sleep(2)
if(dict["door"+str(final)]=="羊"):
    print("主持人：非常遗憾啊！小徐没有竞猜成功。")
else:
    print("主持人：恭喜"+name+"！竞猜成功")
