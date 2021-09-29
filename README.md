# Table-tennis-scorer
这是我开发的乒乓球计分器，方便家庭等环境下的乒乓球娱乐。

### 本文中应用有两种意思：1.程序、2.代码、3积木代码等

### 计分：
现在是只写了11个球制游戏，只要不满足的游戏结束要求便可以使用本套应用进行
要满足您的使用可以把结束操作的代码修改减少
乒乓球11分制竞赛规则（部分）：
一局比赛中，先得11分的一方为胜方。10平后，先多得2分的一方为胜方。

### 应用介绍
使用（与介绍）
一方计数增加：
电脑端，点击分数大框框即可以一次为“+1”累计，其他位置无法执行
手机端与电脑端相同
Arduino端，添加按钮进行控制，本人编写程序时没有按钮与蓝牙传主等设备，所以暂时只支持Arduino接收信号，又因为Arduino板的储存空间有限，所以只能在手机上运行计算，手机操控显示
掌控板端：分左右两边，A、B键进行计数增加
一方计数减少

Android端长按“重置”断开所有可以断开的外部设备，长按“连接与设置”进行连接可以连接的外部设备
唯一识别码是需要向创作者获取的

6、发球一方只要没有发过(包括漏发)都算对方得分。
手机端物联网设置说明：目前使用MQtt协议（常用），当你设置完毕后需要在主界面长按“设置与连接”进行连接确认，如果您也设置了蓝牙连接方式，那会一并连接。
注：数据会因为储存问题而可能被迫清除。由于电脑端编程不足，所以不支持单方分数清零，如果清零可能会导致电脑端发球者显示错误，
还有，作者比较懒，所以设备间的共同代码虽然相同但是有些代码不支持，还请使用或修改时探索！同时为了使程序更好地进行运算，使用了延时，所以请勿快速点击，否则会导致结果不准确或程序崩溃！

### 说明：本软件如果被原创（本人）（注册）共享到应用商店，其主要目的是使应用通过查杀软件的扫描
软件只做交流学习，如有实际应用还请注明创作者信息

### 创作者信息（2020/3/24）：常用昵称：鹰下是海 or 墨书奇迹 email：kaivictor@qq.com
扩展：加入声，灯等提醒，目前部分设备只支持单向信息传递，只需增加“订阅”/“发送”模块并添加延时等即可
还有一些扩展在各个程序代码里有写，主要是懒得去写那些功能

#### 开发信息：python，Mind+，AppInventor,Arduino

#### 设备间的信息
        if rese == "p1add":
            p1sadd()
        if rese == "p1red":
            p1sreduce()
        if rese == "p2add":
            p2sadd()
        if rese == "p2red":
            p2sreduce()
        if rese == "reset":
            resetsoce()
        if rese == "outli":
            outline()
        if rese == "p1res":
            a = 0
        if rese == "p2res":
            b = 0
        resi = "no"

 ___文档没有写完___

[English Readme](https://github.com/kaivictor/Table-tennis-scorer/blob/main/readme_En.md)
