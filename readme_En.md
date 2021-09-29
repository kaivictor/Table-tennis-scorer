This is the table tennis scorer developed by me, which is convenient for table tennis entertainment in family and other environments.

Application in this paper has two meanings: 1. Program, 2. Code, 3. Building block code, etc

About Scoring:
Now only 11 ball games have been written. You can use this set of application as long as you don't meet the end requirements of the game. To meet your use, you can modify the end operation code and reduce the 11 point competition rules of table tennis (part): in a game, the party who gets 11 points first is the winner. After 10 draws, the one who gets 2 points more first is the winner.

Application Introduction

Use (and introduction) one side count increase: on the computer side, click the big score box to accumulate "+ 1" at one time. Other locations cannot execute the same Arduino side as the computer side. Add buttons for control. When I write the program, I have no buttons, Bluetooth transmitter and other devices, so I only support Arduino to receive signals for the time being. Because the storage space of Arduino board is limited, Therefore, the calculation can only be run on the mobile phone. The mobile phone controls the display control board end: it is divided into left and right sides, and the A and B keys are used to count. The count of one side increases and the count of the other side decreases

Long press "reset" on the Android terminal to disconnect all external devices that can be disconnected. Long press "connect and settings" to connect. The unique identification code of external devices that can be connected needs to be obtained from the creator

6. As long as the serving party has not served (including missed service), the other party will score. Description of mobile Internet of things setting: Currently, mqtt protocol (commonly used) is used. After setting, you need to long press "setting and connection" in the main interface to confirm the connection. If you also set the Bluetooth connection method, it will be connected together. Note: data may be forced to be erased due to storage problems. Due to the lack of computer programming, unilateral score clearing is not supported. If it is cleared, the server on the computer may display errors. In addition, the author is lazy, so the common codes between devices are the same, but some codes are not supported. Please explore when using or modifying! At the same time, in order to make the program operate better, delay is used, so do not click quickly, otherwise it will lead to inaccurate results or program crash!

Note: if the software is shared to the app store by the original (I) (registered), its main purpose is to enable the application to pass the scanning of the killing software

The software is only for communication and learning. If there is practical application, please also indicate the creator information

Creator information (March 24, 2020): common nickname: 鹰下是海 or 墨书奇迹  email: kaivictor@qq.com

Extension: add sound, light and other reminders. At present, some devices only support one-way information transmission. Just add the "subscribe" / "send" module and add delay. Some extensions are written in each program code, mainly because they are too lazy to write those functions

Development information: Python, mind +, appinventor, Arduino

Equipment room information
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

The document is not finished

Using machine translation