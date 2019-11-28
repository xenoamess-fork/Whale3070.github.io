---
categories:
- buffer overflow
tags: 
- buffer overflow
---
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>shellcode（payload）</title>
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
        <h1 class="title">shellcode（payload）</h1>
        <div class="show-content">
          <p>shellcode：缓冲区溢出中植入进程的代码，直译就是——可执行的代码。一般是汇编语言写的。</p><p>exploit：劫持程序，跳转去执行shellcode（payload)。</p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-300a37b97d39d4af.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-300a37b97d39d4af.PNG?imageMogr2/auto-orient/strip" data-image-slug="300a37b97d39d4af" data-width="660" data-height="305"><br><div class="image-caption"></div>
</div><p>在实际漏洞调试时，有缺陷的函数可能包含在动态链接库中。这时候被动态加载后、函数在栈中的地址可能会变化。必须让程序自动定位shellcode起始位置。</p><p><b>定位shellcode</b></p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-01dd378f11b213cc.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-01dd378f11b213cc.PNG?imageMogr2/auto-orient/strip" data-image-slug="01dd378f11b213cc" data-width="634" data-height="402"><br><div class="image-caption"><br></div>
</div><p><br></p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-9301c74be98cd23b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-9301c74be98cd23b.png?imageMogr2/auto-orient/strip" data-image-slug="9301c74be98cd23b" data-width="550" data-height="301"><br><div class="image-caption"></div>
</div><p>写个程序，内存中搜索定位user32.dll，在它之后寻找ESP的机器码。</p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-8789fdcdaba253ae.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-8789fdcdaba253ae.PNG?imageMogr2/auto-orient/strip" data-image-slug="8789fdcdaba253ae" data-width="628" data-height="439"><br><div class="image-caption"></div>
</div><hr><p>或者用ollydbg的插件</p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-fa925c7a7a6d8de2.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-fa925c7a7a6d8de2.PNG?imageMogr2/auto-orient/strip" data-image-slug="fa925c7a7a6d8de2" data-width="616" data-height="454"><br><div class="image-caption"></div>
</div><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-be866c6ff4f614b2.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-be866c6ff4f614b2.PNG?imageMogr2/auto-orient/strip" data-image-slug="be866c6ff4f614b2" data-width="596" data-height="533"><br><div class="image-caption"><br></div>
</div><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-1ba503309f5f7fdc.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-1ba503309f5f7fdc.PNG?imageMogr2/auto-orient/strip" data-image-slug="1ba503309f5f7fdc" data-width="500" data-height="404"><br><div class="image-caption"></div>
</div><hr><p><br>选择一个作为esp定位点，7e429353</p><p>exitProcess函数入口点7C81CAFA （调用该API，正常退出不会报错）<br></p><p>messageBoxA函数入口点7E4507EA</p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-b1e2f00d410ed175.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-b1e2f00d410ed175.PNG?imageMogr2/auto-orient/strip" data-image-slug="b1e2f00d410ed175" data-width="715" data-height="357"><br><div class="image-caption"></div>
</div><p>感谢failwest大大的教程。</p><p>后面再学习shellcode的编写，就是用汇编语言写好指令程序，再用ollydbg转成二进制代码。<br></p>
        </div>
      </div>
    </div>
  </body>
</html>
