[download](https://www.vulnhub.com/entry/ch4inrulz-101,247/)

# scan
21/tcp   open  ftp
22/tcp   open  ssh
80/tcp   open  http
8011/tcp open  unknown

## ftp
21/tcp open  ftp     vsftpd 2.3.5
## ssh
OpenSSH 5.9p1 Debian 5ubuntu1.10 (Ubuntu Linux; protocol 2.0)

- https://www.exploit-db.com/exploits/45001/
OpenSSH < 6.6 SFTP - Command Execution
失败

- https://www.exploit-db.com/exploits/45233/
OpenSSH 2.3 < 7.7 - Username Enumeration
成功
![2](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/1029/2.PNG)
确认frank用户存在，但是爆破失败。笑容逐渐消失~~
## http-80port
`http://192.168.1.132/robots.txt`显示这个路径存在，心中一喜，访问看看。
`NOTHING here , yet !`
MD好贱呐！

## http-8011port
visit http://192.168.1.132:8011/
`Development Server !`

```
#nmap -sV -p 8011 192.168.1.132
8011/tcp open  http    Apache httpd 2.2.22 ((Ubuntu))
```
## info1
Apache/2.2.22 (Ubuntu) Server
http://192.168.1.132/development/ 有一个登陆页面

# Trying1
![1](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/1029/1.PNG)
输入用户名123，密码123，发现以123:123的形式base64编码。
于是可以尝试爆破。
![Screenshot from 2018-10-27 12-33-31](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/1029/Screenshot%20from%202018-10-27%2012-33-31.png)
```
import base64
user = open("/usr/share/wordlists/rockyou.txt","r")
answer=open("/root/Desktop/302/answer.txt","w+")
while True:
	one = user.readline()
	#password = open("/usr/share/wordlists/rockyou.txt","r") 
	with open("/usr/share/wordlists/password.txt","r") as password:
		for one_password in password.readlines():	
			ans = one_password.strip("\n")+":"+one
			key = base64.b64encode(ans)
			answer.writelines(key+"\n")

user.close()
```
用burp intruder爆破，无果。
![3](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/1029/3.PNG)

好吧，看看writeup，我承认我菜了==

https://delosec.com/vulnhub-ch4inrulz-writeup/

## 划重点
当时我扫描到了api这个页面，其中提示了四个页面，说在建设中，我检查了前两个，不存在，我就当作四个都不存在。。。

当时的精力花在80端口破解登陆页面去了。。。
反省，需要另开一篇，复习踩点。

http://192.168.1.132:8011/api/files_api.php
![4](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/1029/4.PNG)

- 尝试get提交文件名
```
YOUR IP IS : 192.168.1.128
WRONG INPUT !!
```
- 尝试post提交文件名
![5](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/1029/5.PNG)
说明该php没有禁止post方式==

接下来我尝试了好久，找apache日志的地址，结果都是无用功。。

- nikto -h ip
找到了一个备份文件
http://192.168.1.132/index.html.bak
```
<html><body><h1>It works!</h1>
<p>This is the default web page for this server.</p>
<p>The web server software is running but no content has been added, yet.</p>
<a href="/development">development</a>
<!-- I will use frank:$apr1$1oIGDEDK$/aVFPluYt56UvslZMBDoC0 as the .htpasswd file to protect the development path -->
</body></html>
```
ORZ，我爆破了那么久的口令，就藏在备份文件里了吗。。。
当我尝试`$apr1$1oIGDEDK$/aVFPluYt56UvslZMBDoC0`作为口令登陆失败，我意识到这可能是一个路径，而不是口令。

于是我找到了另一个登陆页面
```
http://192.168.1.132/development/$apr1$1oIGDEDK$/aVFPluYt56UvslZMBDoC0
```
em。。？黑人问号

- 新知识点1
[Apache密码类型](https://httpd.apache.org/docs/2.4/misc/password_encryptions.html)
![7](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/1029/7.PNG)
以前遇到的都是加盐（salt）类型的mdf，md5($pass.$salt)。
这次遇到的这一串`$apr1$1oIGDEDK$/aVFPluYt56UvslZMBDoC0`
貌似是apache特有的加密方式==，长见识了。密码学没怎么学。
![6](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/1029/6.PNG)

总之获得了frank:frank!!!口令，登陆后，看到了上传页面。

上传了一个png，然后找图片上传路径==，找了半天没找到。
看了wp，路径是/development/uploader/FRANKuploads

- 新知识点2
wfuzz的使用

## 文件上传

1. nc -lnvp 1234
2. 选择/usr/share/webshells/php/php-reverse-shell.php
3. 开burp拦截，因为只允许图片类型
后缀改为gif，文件内容改为GIF98，点go就可以成功上传。
![12](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/1029/12.PNG)
4. 绝对路径进行文件包含。
![](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/1029/8.PNG)
linux2.6，版本很低嘛，很明显的内核漏洞提权，快讲烂了==
![13](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/1029/13.PNG)

## 总结
wfuzz、nikto、johntheripper，复习了工具的使用。
明明知道怎么操作，但是就是因为字典或者工具的原因无法成功利用那才是灾难。。。