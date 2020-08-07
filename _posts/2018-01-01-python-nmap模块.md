---
title: python-nmap模块
categories:
- code-basic
tags:
- MyHistoryArticle
- code-basic
---
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>python-nmap模块</title>
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
        <h1 class="title">python-nmap模块</h1>
        <div class="show-content">
          <blockquote><p>easy_install python-nmap （pip install python-nmap也可以哦） 安装模块<br></p></blockquote><p>nmap是xml形式的输出，python-nmap的功能是，解析nmap的输出。</p><hr><br><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-99f67b0d6b7e5ce9.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-99f67b0d6b7e5ce9.PNG?imageMogr2/auto-orient/strip" data-image-slug="99f67b0d6b7e5ce9" data-width="847" data-height="265"><br><div class="image-caption"></div>
</div><br><p>写个脚本使用python-nmap模块，发现不只需要安装该模块，还需要安装nmap。。<br></p><p>我的物理机上没有安装nmap，在kali上运行脚本。</p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-ef86f4bb57019538.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-ef86f4bb57019538.PNG?imageMogr2/auto-orient/strip" data-image-slug="ef86f4bb57019538" data-width="637" data-height="93"><br><div class="image-caption"></div>
</div><p>我不太懂。。既然要用nmap，为什么不直接用nmap，而是写个脚本调用nmap…… 这不是多此一举吗？</p><p>唔…… 也许可以再改造下，收集个ip的字典，扫描后写入到一个文件，用正则筛选扫描结果，最后输出我们感兴趣的开放的端口。。？   这想法不错：》<br></p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-771055699df4e278.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-771055699df4e278.PNG?imageMogr2/auto-orient/strip" data-image-slug="771055699df4e278" data-width="960" data-height="432"><br><div class="image-caption"></div>
</div><br>
        </div>
      </div>
    </div>
  </body>
</html>
