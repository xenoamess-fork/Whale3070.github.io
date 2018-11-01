---
title: mr robots(escalation privilege)
categories:
- training
tags: 
    - training
---

[上一篇](https://whale3070.github.io/training/2017/12/03/mr-robot-SUID-%E6%8F%90%E6%9D%83/)

通过这篇文章，学习shell脚本获取提权信息

nikto -host 192.168.1.135

![1](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/1102/1.PNG)
WordPress/4.3.1

---
## 研究一下CVE-2017-8295：密码重置
https://exploitbox.io/vuln/WordPress-Exploit-4-7-Unauth-Password-Reset-0day-CVE-2017-8295.html

wordpress未授权密码重置
```
As we can see, Wordpress is using SERVER_NAME variable to get the hostname of
the server in order to create a From/Return-Path header of the outgoing password
reset email.
However, major web servers such as Apache by default set the SERVER_NAME variable
using the hostname supplied by the client (within the HTTP_HOST header):
这个cms在创建密码重置邮箱的时候，用到了主机名这个变量，而apache这种服务器，是使用客户提供的http主机头文件作为“主机名变量”
```
客户提供的http_host header
![2](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/1102/2.PNG)
如果我们把这个变量改为“attackers-mxserver.com”，wordpress的“$from_email”变量为”wordpress@attackers-mxserver.com“

![3](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/1102/3.PNG)

查找了一下不能发邮件的原因，==缺少了插件wp-mail-smtp。
http://www.jamesandchey.net/wordpress-the-e-mail-could-not-be-sent-possible-reason-your-host-may-have-disabled-the-mail-function/

好吧，就研究到这里，如果这个目标机有好好配置的话，是可以通过未授权密码重置，得到密码的。

---
nmap并没有写在环境变量中，所以直接调用nmap是not found。
在这个靶机中，nmap很鸡贼地藏在/usr/local/bin/路径下。
nmap version 3.81，低版本的nmap可以以执行root
![12](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/1102/12.PNG)

执行一下脚本，即可获取有SUID权限的二进制文件。
```
#!/bin/bash
cd /tmp
find / -perm -4000 2>/dev/null > examSUID.txt
cat examSUID.txt | grep -E "nmap|vim|find|bash|more|less|nano|cp"
```
script还很简陋，以后再优化优化。
