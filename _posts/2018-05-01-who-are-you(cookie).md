---

title: FourCTFQues
categories:
- CTF
tags: 
    - CTF
---
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>who are you(cookie)</title>
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
        <h1 class="title">who are you(cookie)</h1>
        <div class="show-content">
          <p>访问题目地址，http://106.75.72.168:2222/</p><blockquote><p>Sorry. You have no permissions.</p></blockquote><p>没有访问权限？干脆扫一下端口，这是什么服务？</p><blockquote><p>2222/tcp open  http    Apache httpd 2.4.7 ((Ubuntu))</p></blockquote><p>扫一下目录</p><blockquote>
<p>+ http://106.75.72.168:2222/index.php (CODE:200|SIZE:112)</p>
<p>+ http://106.75.72.168:2222/server-status (CODE:403|SIZE:295)                 </p>
<p>==&gt; DIRECTORY: http://106.75.72.168:2222/uploads/                             </p>
</blockquote><p>注意index.php，本来我以为php脚本里面写了过滤规则，只有特定的ｉｐ才能访问。但是客户端是看不到php文件的。。所以如果题目是这样那就没法做了。</p><p>在 Internet 中，Cookie 实际上是指小文本数据，是由 Web 服务器创建的，将信息存储在用户计算机上的文件。</p><blockquote><p>role=Zjo1OiJ0aHJmZyI7; PHPSESSID=ao2t75c24bggl37ammfp7rjt50</p></blockquote><p>role是身份的意思，base64解码一下，得到f:5:"thrfg";</p><p>找个在线rot13－凯撒解密，得到s:5:"guest";</p><p>guest换成admin，再凯撒编码，得到f:5:"nqzva";</p><p>再base64编码，得到Zjo1OiJucXp2YSI7</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-c9b59d2ed6b9f96e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>方法二，写个脚本。。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-f95c78314ffdb726.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-ca1e0e7e33194ac2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>访问这个uploads的路径，显示是空白？？？</p><p>因为题目提示会接收filename、data参数，经过尝试，filename参数任意ｐｏｓｔ提交，会提示文件路径，（每次都会改变）。我提交的data参数的值会显示在该文件路径网页上。</p><p>暗示我们可以写入一句话木马。但是有正则表达式过滤。</p><p>于是通过data[]＝一句话木马，即可绕过。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-38bb9b80e4a71a61.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption">运行该脚本即可获得ｆｌａｇ<br>
</div>
</div><h4>总结：</h4><p>１．cookies与session的区别。</p><p>session是一个会话，通过服务端和客户端的交互，来识别不同用户。通过服务端给不同用户标识不同session id来确定具体的用户。</p><p>cookies是存在用户浏览器上的小文本文件，session具体是通过cookies来实现的。</p><p>２．目标采用preg_match来进行正则匹配，可以考虑用数组来绕过。</p><p>因为正则只能匹配字符串类型。</p>
        </div>
      </div>
    </div>
  </body>
</html>
