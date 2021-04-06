---
categories:
- linux
tags: 
    - linux
---
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>shell script</title>
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
        <h1 class="title">shell script</h1>
        <div class="show-content">
          <p><a href="http://www.jianshu.com/p/e464c9d89bbb" target="_blank">shell</a>  接下来继续学习bash脚本</p><p><b>read命令</b>，接受用户输入，有点类似python里 raw_input()函数。</p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-079b4356e2c4e837.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-079b4356e2c4e837.PNG?imageMogr2/auto-orient/strip" data-image-slug="079b4356e2c4e837" data-width="573" data-height="160"><br><div class="image-caption"></div>
</div><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-d7fb12f65a3a1217.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-d7fb12f65a3a1217.PNG?imageMogr2/auto-orient/strip" data-image-slug="d7fb12f65a3a1217" data-width="335" data-height="86"><br><div class="image-caption">脚本执行结果</div>
</div><p>由于不同操作系统路径可能不一样，将绝对路径写入脚本，使得脚本有更好的适应性。</p><p>read -p(prompt) 是提示的意思，字符串里的是提示，后面的是变量名。${firstname}是取变量名的内容意思。</p><p>echo -e，这个参数是处理特殊字符的意思，字符串里有 \n 换行符，所以不会将 \n输出到屏幕上，而是执行换行。</p><hr><p>[   ] 判断符号，中括号里面的字符<b>左右都需要有空格</b>，因为Linux里，该符号除了判断，还有其他含义，为了不混淆，所以记得加空格。</p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-5aed633c340515d4.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-5aed633c340515d4.PNG?imageMogr2/auto-orient/strip" data-image-slug="5aed633c340515d4" data-width="533" data-height="177"><br><div class="image-caption"></div>
</div><blockquote>
<p>#<b>sh yes_no.sh                   运行结果如下</b><br>Please input (Y/N):<b> y</b><br>OK, continue</p>
<p>#<b>sh yes_no.sh</b></p>
<p>Please input(Y/N):<b>n</b></p>
<p>oh,interrup!</p>
</blockquote><p>-o（or）连接两个判断，yn变量等于Y或等于y，那么输出ok,continue，并结束程序</p><p>&amp;&amp; 代表and</p><p>|| 代表or</p><hr><blockquote><p>条件判断 if…… then……</p></blockquote><p>这个语句很简单就不举例子了，if 后面接条件，满足就执行 then  后面的语句。</p><p>如果不满足条件呢？</p><blockquote>
<p>if …… ;then ……</p>
<p>else……</p>
<p>fi</p>
</blockquote><p>else语句接，不满足条件后执行的语句</p><p>fi是if的倒写，表示条件语句over了。</p><p>如果是多项条件判断：elif…… ;then…… 加在if-then 语句之后。</p><hr><blockquote><p>条件判断while […… ] do…… done……</p></blockquote><p>经过上面的程序示范，应该很容易就能看懂下面的shell script，当输入的变量yn不等于yes或YES，就一直循环提示的字符串"please input …… "</p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-21e5a543d1899749.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-21e5a543d1899749.PNG?imageMogr2/auto-orient/strip" data-image-slug="21e5a543d1899749" data-width="521" data-height="128"><br><div class="image-caption"></div>
</div><hr><blockquote><p>固定次数循环    for…… do…… done</p></blockquote><p>for后面是变量$animal，第一次循环，$animal = dog，第二次循环，$animal = cat</p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-f4a0684def9ff5ad.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-f4a0684def9ff5ad.PNG?imageMogr2/auto-orient/strip" data-image-slug="f4a0684def9ff5ad" data-width="316" data-height="106"><br><div class="image-caption"></div>
</div><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-3e33909ed6169f93.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-3e33909ed6169f93.PNG?imageMogr2/auto-orient/strip" data-image-slug="3e33909ed6169f93" data-width="289" data-height="68"><br><div class="image-caption"></div>
</div><hr><p><b>案例一</b>：将经常要运行的命令写入。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-65d44c0423fa6e55.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><blockquote>
<p>chmod +x  burp.sh</p>
<p>./burp.sh</p>
</blockquote><p><b>案例二</b>：用选择功能，简化每次输入的命令。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-64a43228fca2b50b.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>总结，1.变量要用$ {   }标识 </p><p>           2.每一个特定符号要用引号括起来。</p><p>           3.if 语句要用[    ]括起来，然后需要两侧加空格。</p><p>           4.cd转换路径，路径左侧不能加/，如cd /tool （错误），“/tool”表示根目录下的tool文件夹</p>
        </div>
      </div>
    </div>
  </body>
</html>
