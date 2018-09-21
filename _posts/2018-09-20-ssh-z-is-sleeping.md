---
title: SSH... Z is sleeping
categories:
- unresolved
tags:
-CTF
---
题目地址：
http://www.wechall.net/challenge/warchall/ssssh/index.php

Z is sleeping, if you hurry you can steal his SSH key and log in as level8
题目要求：窃取Z的ssh密钥，以用户level8登陆

![可以看出，level8是一个普通用户](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0920/3.PNG)

![查看level8家目录的文件](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0920/%E6%8D%95%E8%8E%B7.PNG)
查看backups，其中有authorized_keys.backup
```
ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAtyppECq53bP3yUbQToXsxIhuYK5PyXLvTCj+Ob02/kcM3ZUEXNpsX1177Gl92kq4+tbt9pRm3UY3C8/7pEmkSWcbiLgIx96aqIoFvHEOdmz+9YaimPmzqaHTDW+g8QV+khFGDp22SOaUpKaUTpmLKniavIEVP4ouXPLqwapg/xEU36xF18a6bG4/iYV/Nxmf0bv7K6nkgRsYC55lRPHMVJnI1Gy7eHHk/PiHYR5pkOIb9GSTtqcJTRs/EJgVhBMygHYTrVT8+HLW0PqYK3Dw/Z6az3+qOaaAYqJk7sxBAZC4/YKhLVL6LjagRpff6rpXFUwv1eHidy2iLBRNcY/2Hw== 
```
solution.txt查看，发现权限不够
## 第一步

前面信息搜集完毕，知道我们要做的事是，获得level8的ssh密钥，登陆后查看solution.txt

查看level8登陆，端口正确
尝试用authorized_keys.backup登陆，提示权限问题
更改权限之后，提示格式错误 
![1](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0920/1.PNG)

好吧，生成一个公钥和密钥，观察一下格式。
![2](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0920/2.PNG)
- 公钥：id_rsa.pub
```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCx8c7MJcW5+5AaCSiEj3t3H7Rwlqe5lDlnW0bjbalTFd/xYwOVXUJfV/WN1UR08Bxc7arQpnA9sW7yTtbFv0yJl/yjQUMTR1ZXED2Ad8SO/7a2C3qbQsRLhsEIwKBgl4TGolr7Av/K+eChVEQBzzkGueLMnkyHS6o+4R5NfFX5TyMWl4XEx/4VQTAjjmBQMG+cWp5rzhtcwcsXQb+01hjQa15MIZyaTGc/++JRMDQZShvy0HOg/lEuXacyuny59ipQ/+YnRAaxQ5VAZJqHIDII82Ip3UWPPV0hEzBJ+zatANXLm5GUZpLxC00+HKSA2XykyrD/GIvc2hsKGVtOPAKx root@whale3070

```
私钥：
```
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAsfHOzCXFufuQGgkohI97dx+0cJanuZQ5Z1tG422pUxXf8WMD
lV1CX1f1jdVEdPAcXO2q0KZwPbFu8k7Wxb9MiZf8o0FDE0dWVxA9gHfEjv+2tgt6
此处省略几十行。。。
-----END RSA PRIVATE KEY-----

```
 ## 第二步
authorized_keys.backup 给的是公钥，不是私钥，无法直接登陆。。。

转到level8的家目录，cat .ssh，还是权限不够。

## 第三步
根据题目提示，Z is sleeping, if you hurry you can steal his SSH key and log in as level8

1. Z是谁？搜索了一圈，发现没有这个用户，可能是代称。
2. 在/home目录下，搜索关键字，`id_rsa`、`.ssh`、`rsa`
基本都是权限不够，不过发现了一个用户ricter！
根据自己的家目录`/home/user/whale3070`判断，该用户也是在wechall上练习的人。

根据ricter留下的线索，认为是 [openssl Predictable PRNG Brute Force SSH](https://www.exploit-db.com/exploits/5720/)，一个可预测的ssh爆破漏洞

 在rsa目录下有2048文件夹，里面存放着一些爆破用的文件，本来想拷出来，但权限不够。

![4](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0920/4.PNG)

info:
warchall.net 176.58.89.195

## 第四步
用脚本爆破ssh尝试登陆
![5](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0920/5.PNG)

