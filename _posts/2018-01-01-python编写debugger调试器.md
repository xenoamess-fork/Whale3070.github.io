---
title: 2018-01-01-python编写debugger调试器
categories:
- code-basic
tags: - code-basic
- myHistory
---


ce-width, initial-scale=1.0">
    <title>python编写debugger调试器</title>
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
        <h1 class="title">python编写debugger调试器</h1>
        <div class="show-content">
          <p>http://blog.csdn.net/u012763794/article/details/52174275#t21<br></p><p>？what and why</p><p>是跟踪程序的程序，为了发现目标程序的错误</p><p>？How</p><p>通过调用一系列API实现对目标程序的附加，停止等等操作。debugger必须容易读写寄存器，并修改它们的值。debugger会一直循环，直到调试事件发生。</p><h4>断点</h4><p>调试器通常需要中断程序，操作系统提供的中断操作有两种，一种是硬件中断，一种是软件中断。</p><p>硬件中断来自于硬件，如键盘被按下，鼠标按下。</p><p>软件中断是一个指令，让操作系统停止应用程序，这个指令是 int 0x80（对应硬件平台i386、OS linux）<br></p><p><b>软断点</b>：是一个单字节的指令，碰到该指令就停下来，把控制权交给调试器。</p><p>interrupt 3指令 = 0xcc（操作码）</p><p>黑盒调试器和白盒调试器区别：有没有程序源代码的区别。</p><p><b>黑盒调试器运行在什么样的权限下？</b></p><p>rin3 user模式 最小权限 exe文件运行的   ，（WINDBG、Ollydbg   运行在这个模式下）<br></p><p>rin0 kerner模式 最大权限 操作系统以及驱动等等（运行的 PYDBG）</p><hr><p>用python写一个debugger调试器。</p><p>首先建立一个框架，一个主程序my_test.py（负责组织调用其他模块），一个定义变量的模块my_debugger_defines.py，还有一个bugger模块,my_debugger.py（定义了具体的实现）。将这三个模块放在同一个文件夹下。</p><p>运行<b>my_test.py</b>脚本。该脚本很简单，就是三行，第一行导入my_debugger模块，第二行使用该模块下的debugger函数，第三行，给这个函数导入位于某位置的函数作为参数。</p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-7cab6a66ddb47cb1.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-7cab6a66ddb47cb1.PNG?imageMogr2/auto-orient/strip" data-image-slug="7cab6a66ddb47cb1" data-width="551" data-height="293"><br><div class="image-caption"></div>
</div><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-e6ce4d542ebe0673.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-e6ce4d542ebe0673.PNG?imageMogr2/auto-orient/strip" data-image-slug="e6ce4d542ebe0673" data-width="572" data-height="190"><br><div class="image-caption"></div>
</div><p><b>debugger模块</b>里，定义了一个类debugger，定义了两个方法，一个是初始化变量的方法，一个是加载进程的方法。第二个方法的具体实现调用了一个windowsAPI，用来加载一个程序。</p><hr><p><b>如何调用windowsAPI？</b></p><p>1，首先你要有一本《windowsAPI》，可以根据功能查找API的名称和参数。</p><p>2，在Python中，你需要在开头的时候说明要使用的库：</p><p>kernel32 = windll.kernel32</p><p>前面是<b>名字</b>，后面是告诉计算机<b>路径</b>，在哪里找到它。在后面我们调用kernel32动态链接库中的函数的时候就可以直接用kernel32</p><p>这个称呼，计算机就会在给出的地址去调用kernel32了。</p><p>3，</p><p>class calculate():  #<b>定义一个类</b>。</p><p>def _init_(self):  #定义一个特殊方法，初始化参数的。要调用的API的参数可以在这里初始化。</p><p>   pass</p><p>def add(self,plus):#<b>定义一个方法</b>。</p><p>if kernel32.XXXXXXXXX(AA,BB,CC,DD) #<b>给出API函数的名字，参数</b>。</p><p>print "success!" #调用成功，并打印出success.</p>
        </div>
      </div>
    </div>
  </body>
</html>
