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
    <title>mr.robot（无漏洞、爆破后台）</title>
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
        <h1 class="title">mr.robot（无漏洞、爆破后台）</h1>
        <div class="show-content">
          <p><a href="https://www.vulnhub.com/entry/mr-robot-1,151/" target="_blank">靶机下载地址</a>：扫一扫，linux系统，发现只开了80、443，进去看一看，web页面是一个模拟linux终端的页面</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-595353543a444102.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>如果输入指定的命令，则会出现一段视频，或者一些文字，(⊙﹏⊙)这个靶机到底想传达什么。</p><p>如果输入以外的命令，显示command not recongnized...</p><p>查看主页面的源代码，发现两个注释，什么东东？</p><blockquote>
<p>1.you are not alone.你并不孤独</p>
<p>2.如果是ie9浏览器，显示，你使用一个过时的浏览器，请到https://browsehappy.com/升级你的浏览器，提升浏览体验。</p>
</blockquote><p>用paros扫描，没有发现明显的漏洞。</p><p>发现目录/audio , /css ,/js ，用浏览器访问，显示403 forbidden</p><hr><p>看来，要看看提供的六个命令。依次输入了这些命令，了解到，这个服务器是一个组织fsociety的，这个组织貌似是反||美的一个z-f组织，最后一个命令join会要求你提供一个邮箱，还说会跟你联系。。</p><p>然而如何突破防线，没有任何思路。</p><p>这时候注意到，浏览器是这样，http://192.168.1.116/wakeup，说明是通过get方式请求页面的。</p><p>于是不在终端输入，而直接在url上输入。输入任何东西，都会跳转到下图所示页面，而且显示xx（你输入的字符）404not found.</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-a34d0d23bc9de395.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>了解到，该网站是用wordpress搭建的，yoxi~</p><p>扫描下后台，用的我写的<a href="https://www.jianshu.com/p/b4cfa0cf5ad0" target="_blank">脚本</a></p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-8c6b32b54839247d.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>em?用浏览器打开，然后页面就一直抽搐。。</p><blockquote>
<p>wget http://192.168.1.116/admin/index.html</p>
<p>firefox index.html</p>
</blockquote><p>浏览器打开后，发现是白页，查看源代码，和http://192.168.1.116 的源代码并没有什么差别，不过又注意到了原先没注意的一条代码。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-698226211ae2689c.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>难道要伪造IP——208.185.115.6，才能访问index.html？</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-be518359b82d87e7.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>然而，并没有什么区别，响应还是那个页面。。</p><p>访问/admin页面，显示301 Moved Permanently永久重定向？页面显示重定向的页面是/admin/，打开一看，又是老页面。</p><hr><p>好吧，放弃该死的后台寻找，看看writeup</p><blockquote><p>wpscan --url 192.168.1.116 --enumerate p</p></blockquote><p><a href="https://tools.kali.org/web-applications/wpscan" target="_blank">wpscan介绍</a>：用wordpress专用扫描器，，</p><blockquote>
<p>http://192.168.1.116/robots.txt</p>
<p>http://192.168.1.116/wp-content/plugins/google-analytics-for-wordpress/readme.txt</p>
<p>http://192.168.1.116/wp-content/plugins/contact-form-7/</p>
<p>...............</p>
</blockquote><p>扫描出了很多目录，而且获得了一个key（总共有三个，靶机下载介绍过）。而且扫描器指出，可能有存储型XSS。</p><hr><p>终于找到一个突破点了，不容易啊。。。对xss不熟悉的同学，跟我复习一下好了。</p><p>xss，cross-site-scipt跨站脚本攻击：web提供了输入输出的地方（这是正常功能对吧？)，如果没有过滤，就可以输入脚本。</p><p>如果脚本可以永久存储，就叫存储型xss（打击面为所有访问网站的客户端），若不能，就叫反射型xss。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-d4873ff38d134380.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption">并没有弹框</div>
</div><p>呃。。不会了</p><hr><p>nikto扫描器试试，还挺给力的，找到后台。。</p><blockquote><p>nikto -h http://192.168.1.116</p></blockquote><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-02333f907734ae94.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><blockquote><p>wget http://192.168.1.116/fsocity.dic &gt; fsociety.txt    这个目录是robots.txt指出来的</p></blockquote><p>用来爆破后台，作为用户名字典。<a href="http://www.hackingarticles.in/brute-force-website-login-page-using-burpsuite-beginner-guide/" target="_blank">参考文献</a></p><p><a href="https://support.portswigger.net/customer/portal/articles/1964020-using-burp-to-brute-force-a-login-page" target="_blank">burp爆破</a>，扫描一段时间后，通常错误页面Length长度为4073，然后找到一个4124的，虽然没有找到用户名和密码，但是elliot这个用户名是存在的。。</p><p>吐血，居然有登陆表单的错误信息不是“无效的用户名或密码”，而是“你输入的xx用户名的密码是错的哦~”</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-a75652ac1d850bda.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>然后就换一下payload，用户名设置为elliot，密码设置为一个txt字典。</p><p>遗憾的是，并没有爆破出来，没有好的字典吧。。</p><p>呃，再试试fsociety.txt 作为密码字典，有近86万条，扫了好久。。</p><hr><p>方法二：用wpscan爆破，wpscan --url http://192.168.1.116/ --wordlist /root/fs.txt --username elliot</p><p>爆破结果，密码是<b>ER28-0652</b></p><h1><b>尝试获取webshell</b></h1><p><b>1.直接上传php脚本，有限制。</b></p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-08f9050e8898cf4f.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>2.用msfvenom生成php载荷，<a href="https://www.jianshu.com/p/52a668889512" target="_blank">参考这个实验中的方式</a>。</p><p>成功上传攻击载荷。</p><p>但是访问http://192.168.1.116/wp-content/uploads/2018/02/xxd.gif</p><p>本地没有获得metapreter。</p><p>（猜测）反弹metapreter失败了。。</p><p>这是为什么，，难道因为没有文件包含就执行不了么，不可能吧。</p><p>猜测：本地文件包含是在服务端，运行payload。而访问这个链接，服务端直接将gif文件发送过来，浏览器打开失败（本来就不是真的图片）。所以没有达到运行的目的。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-c8a8959e81a0743a.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>3.F12-响应头，获得服务器php版本，PHP/5.5.29。这个版本有点高啊，不能截断上传了。</p><p>抱着死猫碰上瞎耗子的心情，试了试，果然不能。试了试该文件名后缀为.jpg，无效。</p><p>4.<a href="http://pentestmonkey.net/tools/web-shells/php-reverse-shell" target="_blank">下载一个php-reverse-shell，然后修改ip</a>。既然不能上传新的php文件，那么修改现有的php文件。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-52efe710aefbdf89.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>只要运行一下错误页面，就获得了一个shell。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-72f68fff63937eb7.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><h1>总结：</h1><blockquote>
<p>本次突破防线，利用的是后台提示用户名和密码太“贴心”。</p>
<p>如果提示“登陆失败，错误的用户名或密码。”</p>
<p>再加上一个强密码。（本次爆破成功，密码强度还可以，不算弱密码）爆破的成功率可以忽略不计。</p>
</blockquote><blockquote>
<p>学习了wpscan、nikto扫描。</p>
<p>不要依赖单一的工具。。</p>
</blockquote><blockquote><p>学习了一种新的获取webshell的思路</p></blockquote>
          <p>前景提要：上次通过爆破后台，修改404.php获得一个webshell。现在学习提权。</p><p>id、whoami、hostname</p><blockquote><p>信息：daemon用户，uid=1说明是系统用户，主机名linux</p></blockquote><p>cd home/robot</p><blockquote>
<p>信息：获得另一个key（2/3），和passwd文件，文件内容：</p>
<p>robot:c3fcd3d76192e4007dfb496cca67e13b</p>
</blockquote><p>MD5解码：abcdefghijklmnopqrstuvwxyz</p><p>(⊙﹏⊙)这个明显是偏CTF，而不是模拟真实渗透环境啊。</p><p>su robot/abcdefghijklmnopqrstuvwxyz</p><hr><p>寻找有<a href="https://www.jianshu.com/p/45e60bed314e" target="_blank">SUID权限</a>的文件。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-e3705143f79975d2.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>于是通过nmap提权。</p><p>查看nmap版本：/usr/local/bin/nmap --version   或者 nmap -V</p><p>老版本的nmap(2.02-5.21)有一个交互模式，使得用户可以执行shell。</p><blockquote>
<p>nmap --interactive</p>
<p>!sh</p>
<p>pwd</p>
<p>cd root</p>
<p>ls</p>
</blockquote><p>获得第三个key.</p>
        </div>
      </div>
    </div>
  </body>
</html>
