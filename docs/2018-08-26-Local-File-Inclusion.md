---

categories:
- CTF
tags: 
    - web
---
 [题目地址](http://www.wechall.net/challenge/training/php/lfi/up/index.php)

首先访问下题目提到的：[http://www.wechall.net/challenge/training/php/lfi/solution.php](http://www.wechall.net/challenge/training/php/lfi/solution.php)
```
You are not allowed to execute this script directly. Please include it using the LFI vuln in up/index.php.
```
## 提示
在主页面（index.php）利用该漏洞访问solution.php
![3](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0826/3.PNG)

>info1: http://www.wechall.net/challenge/training/php/lfi/up/pages/welcome.html
http://www.wechall.net/challenge/training/php/lfi/solution.php
说明需要返回两个上级目录

---

因为需要访问solution.php，于是联想到%00截断
## 实验一
file=news.html%00
![1](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0826/1.PNG)
截断是有效的

## 实验二
![2](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0826/2.PNG)
打开失败，可以看到报错揭示了路径
>info:  pages/solution.php
路径www/challenge/training/php/lfi/up/pages/news.html

## 实验三
www/challenge/training/php/lfi/up/xx.html
尝试用../返回上层路径。

file=../../solution.php%00
成功进行本地文件包含

