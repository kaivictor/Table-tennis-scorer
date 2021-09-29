'''
//python 3.8 鹰下是海 QQ:2993968987 python计分器
'''

import tkinter
import threading
import time
from tkinter import messagebox
import paho.mqtt.client

te = tkinter.Tk()

te.title("乒乓球计分器")
te.geometry("1090x600")


a = 0
b = 0
#局数
gamenumber = 1

resi = "no"

#结果统计(运用多线程）
totallscore = a + b
text_score = str(a) + str(b)


#物联网控制(运用多线程）

mqtt = paho.mqtt.client
#MQtt加持
resi = "no"
rese = "no"
seve = 1
sevehelp = 1

def on_connect(client,userdata, flags, rc):
    #print("Connected with result code "+str(rc)) #打印连接状态
    client.subscribe("******") #订阅的主题
def on_message(client, userdata, msg):
    global resi
    resi =("%s"%(msg.payload)) 
    #print(resi)#打印接受的消息
    time.sleep(1)
    resi = "no"
        

#物联网控制
def mqcontrol():
    global a,b,rese,resi,seve,sevehelp,totallscore,text_score,state
    time.sleep(1)
    rese = "no"
    seve = 1
    while True:
        totallscore = a + b
        text_score = str(a) + ':' + str(b)
        #time.sleep(1)
        #print(totallscore)
        #print(text_score)
        #结果判定
        if a >= 11 and b <= 9:
            tkinter.messagebox.showinfo(title='结果', message='玩家二胜利')
            resetsoce()
        if b >= 11 and a <= 9:
            tkinter.messagebox.showinfo(title='结果', message='玩家一胜利')
            resetsoce()
        if totallscore >=22:
            if (a - b) == 2:
                tkinter.messagebox.showinfo(title='结果', message='玩家二胜利')
                resetsoce()
            if (b - a) == 2:
                tkinter.messagebox.showinfo(title='结果', message='玩家一胜利')
                resetsoce()
        time.sleep(1)
        print(resi)
        rese = (resi[2:7])
        print("seve: %s"%seve)
        
        if a == 1 and b == 0 and seve ==1:
            seve = 3
            sevehelp = 3
            dispsev_a()
            time.sleep(1)
            a = 0
        if b == 1 and a == 0 and seve ==1:
            seve = 4
            sevehelp = 4
            dispsev_b()
            time.sleep(1)
            b = 0
        
        if totallscore%2 == 0 and totallscore <= 20 and totallscore >> 0 and seve == sevehelp:
            time.sleep(0.5)
            seve += 1
            if totallscore == 20:
                sevehelp = totallscore
        if seve%2 == 1 and seve >> 1 and totallscore >> 0:
            dispsev_a()
            #print("runed4")
        if seve%2 == 0 and seve >> 1 and totallscore >> 0:
            dispsev_b()
            #print("runed5")
        if totallscore%2 == 1 and totallscore << 20 and totallscore >> 0 and seve == (sevehelp + 1):
            if sevehelp != seve:
                sevehelp = seve
        #if totallscore%2 == 1 and totallscore << 20 and totallscore >> 0 and seve == sevehelp:
        #    sevehelp -= 1
        if totallscore >= 21:
            if totallscore == sevehelp + 1:
                time.sleep(0.5)
                seve += 1
                sevehelp += 1
        if totallscore == 0 and (seve == 2 or seve == 1):
            resetsoce()
                
        if rese == "p1add":
            p1sadd()
            print(rese)
        if rese == "p1red":
            p1sreduce()
        if rese == "p2add":
            p2sadd()
        if rese == "p2red":
            p2sreduce()
        if rese == "reset":
            resetsoce()
        if rese == "outli":
            resi = "no"
            time.sleep(2)
            outline()
            #pass#outline
        #有发生一打开程序便退出，需要检查：如果使用移动端退出电脑端程序且网络响应过慢则需要更该变量（rese)，应为该变量储存为了“outli”,那你就替换代码（比如使用：pass）运行并需要在物联网控制平台发送其他内容来更改该变量
        if rese == "p1res":
            a = 0
        if rese == "p2res":
            b = 0
        if rese == "p1sev":
            resi = "no"
            #p1sadd()
            p1sadd()
        if rese == "p2sev":
            resi = "no"
            #p2sadd()
            p2sadd()
        resi = "no"

        p1add['text']= a
        p2add['text']= b

#子线程物联网控制启动
m_01 = threading.Thread(target=mqcontrol,name="thread2")
m_01.setDaemon(True)
m_01.start()


#def mqhelp():
client_id = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
client = mqtt.Client(client_id)    # ClientId不能重复，所以使用当前时间
client.username_pw_set("*****", "*******")  # 必须设置，否则会返回「Connected with result code 4」，就是错误嘛
#client.username_pw_set("iot id", "iot key")
client.on_connect = on_connect
client.on_message = on_message
client.connect("*****************", 1883, 60)
#client.loop_forever()

client.loop_start()#循环


#print("start thread %s" % threading.current_thread().getName())

#分数增加
def p1sadd():
    global a,b,seve
    if a == 1 and b == 0 and seve ==1:
        a = 0
    else:
        a += 1

def p2sadd():
    global a,b,seve
    if b == 1 and a == 0 and seve ==1:
        a = b
    else:
        b += 1
    
#键盘操控
def p1sa(event):
    global a
    a += 1
    
def p2sa(event):
    global b
    b += 1

#分数减少
def p1sreduce():
    global a,seve,sevehelp
    if a > 0:
        a -= 1
    seve -= 1
    sevehelp = seve - 1

def p2sreduce():
    global b,seve,sevehelp
    if b > 0:
        b -= 1
    seve -= 1
    sevehelp = seve - 1

#重置
def resetsoce():
    global a,b,gamenumber,totallscore,seve,sevehelp
    a = 0
    b = 0
    totallscore = a + b
    seve = 1
    sevehelp = 1
    p1add['text']= a
    p2add['text']= b
    p1sdp['text']= "    "
    p2sdp['text']= "    "
    gamenumber += 1

#退出
def outline():
    global gamenumber
    te.destroy()
    print(gamenumber)

    

#创作信息
def information():
    tkinter.messagebox.showinfo(title='创作信息', message='作者：鹰下是海  QQ：2993968987                                                                     项目名称：计分器 2020/3/19  目前设定规则为11球制')


    
#键盘操作
#def resets(event):
#    global a
#    global b
#    a = 0
#    b = 0
#    p1add['text']= a
#    p2add['text']= b

#键盘<back>键的撤销动作

#plus
#加入数据保存,快速修改分数，可修改a、b的值实现初始值改变
#把上面一大串弄成一个类，并移到另一个py中，并引用
#加入键盘控制



#按钮
p1add = tkinter.Button(text = "0",command = p1sadd,height = 1,width = 3,font=('楷体',280),fg='#FF0000',bg='#FFF68F')
p1add.place(x=0,y=0)
p2add = tkinter.Button(text = "0",command = p2sadd,height = 1,width = 3,font=('楷体',280),fg='#FF0000',bg='#FFF68F')
p2add.place(x=546,y=0)
p1red = tkinter.Button(text = "一方撤销",command = p1sreduce,height = 1,width = 77)
p1red.place(x=0,y=540)
p2red = tkinter.Button(text = "一方撤销",command = p2sreduce,height = 1,width = 77)
p2red.place(x=546,y=540)
reset = tkinter.Button(text = "重置",command = resetsoce,height = 1,width = 78)
reset.place(x=245,y=570)


p1sdp = tkinter.Label(te,text = "    ",font=('楷体',40),fg='#76EE00',bg='#FFF68F')
#,command=dispsev_a
p1sdp.place(x=220,y=0)
p2sdp = tkinter.Label(te,text = "    ",font=('楷体',40),fg='#76EE00',bg='#FFF68F')
p2sdp.place(x=780,y=0)

#发球显示
def dispsev_a():
    p1sdp['text']= "发球"
    p2sdp['text']= "    "
    global a,b,seve
    if a == 1 and b == 0 and seve ==1:
        a = 0
    
def dispsev_b():
    global a,b,seve
    p2sdp['text']= "发球"
    p1sdp['text']= "    "
    if b == 1 and a == 0 and seve ==1:
        b = 0

#退出
turn_out = tkinter.Button(text = "退出",command = outline,height = 1,width = 40)
turn_out.place(x=800,y=570)

#创作信息
information = tkinter.Button(text = "创作信息",command = information,height = 1,width = 40)
information.place(x=0,y=570)


#键盘操控
te.bind('<Key-Left>',p1sa)
te.bind('<Key-Right>',p2sa)
#te.bind('<Key-BackSpace>',resetsoce)
#te.bind('<F5>',disupate)
#te.bind('<Rsc>',outline)

te.mainloop()#循环
