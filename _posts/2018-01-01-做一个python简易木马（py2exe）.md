---
title: 做一个python简易木马（py2exe）
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
    <title>做一个python简易木马（py2exe）</title>
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
        <h1 class="title">做一个python简易木马（py2exe）</h1>
        <div class="show-content">
          <p>1，先下载需要用到的库。<b><a href="https://sourceforge.net/projects/pywin32/files/pywin32/" target="_blank">pythoncom</a></b>和<b><a href="http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook" target="_blank">pyhook</a></b>是没有的，所以要自己下载。</p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-4b8ac636f05b6f64.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-4b8ac636f05b6f64.PNG?imageMogr2/auto-orient/strip" data-image-slug="4b8ac636f05b6f64" data-width="740" data-height="364"><br><div class="image-caption"></div>
</div><p>2，创建四个文件，记录键盘的，截取屏幕的，客户端，服务端。</p><p>3，在虚拟机上测试一下。</p><p>4，用py2exe.exe 将三个模块转换成一个exe文件(根据你的python版本选择py2exe，win32 or win64）</p><p><a href="http://www.py2exe.org/index.cgi/Tutorial" target="_blank">py2exe模块</a> ：该模块可以使没有安装python的windows主机可以运行python程序。</p><p>http://www.cnblogs.com/jans2002/archive/2006/09/30/519393.html</p><p>http://blog.csdn.net/puma004/article/details/40742953</p><hr><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-d943fac697ed42fd.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240"><br><div class="image-caption"></div>
</div><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-1d054604d981e621.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-1d054604d981e621.PNG?imageMogr2/auto-orient/strip" data-image-slug="1d054604d981e621" data-width="908" data-height="550"><br><div class="image-caption"></div>
</div><p><br></p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-0145f8983e7551bc.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-0145f8983e7551bc.PNG?imageMogr2/auto-orient/strip" data-image-slug="0145f8983e7551bc" data-width="785" data-height="354"><br><div class="image-caption"></div>
</div><p><br></p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-35142c5180924864.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-35142c5180924864.PNG?imageMogr2/auto-orient/strip" data-image-slug="35142c5180924864" data-width="949" data-height="799"><br><div class="image-caption">这是运行脚本后截图桌面的照片</div>
</div><hr><p>确认你装好了py2exe ,就可以开始了。</p><p>首先编写一个脚本，setup.py。目的是包括我们以前写的所有python模块以及一些动态链接库。</p><p>转到命令行下相应目录，python setup.py install</p><p>python setup.py py2exe</p><p>cd dist (应用程序被放在创建的dist目录下）</p><p>xxx.exe（运行该程序）</p><p>我现在还做不到将几个模块连接起来，经验不够。</p>
        </div>
      </div>
    </div>
  </body>
</html>
