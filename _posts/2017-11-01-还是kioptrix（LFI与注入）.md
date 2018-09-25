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
    <title>还是kioptrix（LFI与注入）</title>
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
        <h1 class="title">还是kioptrix（LFI与注入）</h1>
        <div class="show-content">
          <p>kiotrix level 3 虚拟机一台（分配的ip——192.168.1.114）</p><p>——这台虚拟机主要是用来测试web渗透技能的，扫描后发现开放的端口只有22、80。很正常，你随便找个网页，它所在的服务器多半也是这样，不可能开放很多端口的。<a href="https://www.jianshu.com/p/dc21906c957f" target="_blank">如何扫描端口</a></p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-e6bd048ade3213de.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-e6bd048ade3213de.PNG?imageMogr2/auto-orient/strip" data-image-slug="e6bd048ade3213de" data-width="429" data-height="249"><br><div class="image-caption"></div>
</div><blockquote><p>echo 192.168.1.114 kioptrix3.com &gt;&gt; /etc/hosts</p></blockquote><p>在kali linux配置域名和ip，就可以通过域名访问网页了，不然该虚拟机的有些链接的内容显示不完全。</p><hr><p>信息搜集：</p><blockquote>
<p>用的什么CMS?     <b> LotusCMS</b> 是个开源软件项目，在github上。</p>
<p>                               cms的版本在虚拟机网页上没有发现，然后搜索了一下，貌似只有3.0版本。</p>
<p>                               而且搜索结果有很多有关该<b>CMS远程命令执行</b>的网页。</p>
<p>服务以及版本：Apache 2.2.8     php5.2.4（通过浏览器F12，response headers获得）</p>
<p>操作系统：ubuntu5.6 with suhosin-patch</p>
</blockquote><p>主页面上有login，省了找后台的功夫了。</p><blockquote><p>http://192.168.1.114/index.php?system=Admin&amp;page=loginSubmit</p></blockquote><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-9df5dbbfd900023d.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-9df5dbbfd900023d.PNG?imageMogr2/auto-orient/strip" data-image-slug="9df5dbbfd900023d" data-width="306" data-height="379"><br><div class="image-caption"></div>
</div><hr><p>测试下该网站有无明显的注入点。明显的意思就是在页面上显示sql错误的那种。</p><p>用<a href="http://www.softpedia.com/dyn-postdownload.php/5cd650e9f952569f51ad9300a3a49207/5a00695a/1917e/4/2" target="_blank">hp scrawlr </a>爬行网站，这是windows平台的工具，有图形化界面，使用简单。</p><div class="image-package" data-index="1">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-a8a30866faf6197a.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" style="min-height:0;min-width:0;" width="auto" height="auto"><br><div class="image-caption"></div>
</div><div class="image-package" data-index="2">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-fa1b9826f61cdfc1.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" style="min-height:0;min-width:0;" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>对该工具的分析：它仅仅适用于判断非常明显的数据库错误，它只测试GET参数，如果返回500错误，会提示有注入点。</p><p>该工具的适用范围：当你不想每个页面都输入‘，看页面的反应的时候，用它吧。。</p><p>测试结果是  ：（  没有</p><hr><p>尝试搜索有无现成的exploit可用。</p><p><a href="https://www.exploit-db.com/" target="_blank">https://www.exploit-db.com/</a></p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-29a1379de5cbf7c8.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p><a href="https://www.jianshu.com/p/71e4534c9e24" target="_blank">metasploit使用简介</a> 通过搜索结果可以知道，metasploit有现成的模块可以使用。</p><p>对于利用模块的流程可以参考<a href="https://www.jianshu.com/p/dc21906c957f" target="_blank">kioptrix第一关</a>。这里不赘述了。</p><hr><p>因为有meta框架，所以获得shell变得简单。</p><p>为了达到练习目的，再深入探讨下。通过其他漏洞获得web数据库管理员账号和密码，并成功登陆的情形：</p><p><a href="https://www.jianshu.com/p/3910c32a59eb" target="_blank">本地文件包含local file include</a>:该漏洞能够读取敏感文件源代码。这里获取到了linux用户名。</p><h1>OWASP_ZAP</h1><p>和burp suite类似，不过burp是商业的，这个是开源的。该工具由owasp组织发行。owasp——应该听说过他们吧，owasp top 10就是他们总结的，web安全界传说中的组织23333.</p><p>看到扫描结果，标红的一个，<b>php代码注入</b>，经过检查，发现就是metasploit的那个漏洞利用模块使用的。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-b255baf7853f9ea8.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>看看还有没有什么新鲜的。</p><p>应用程序错误发现：说发现服务器500错误。</p><p>缓冲区溢出：就是在url上构造了一个超长的链接，检查以后发现都是些子虚乌有的玩意儿。。。。</p><h1>Paros</h1><p>java写的web扫描工具，我又手贱的试用了下kali下集成的web渗透工具。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-bbe62657d54f663c.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-b95d28cb92673b53.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>效果不好，没检出什么有用的东西。</p><p>不过有用的一点是spider，获得网站上URL的树目录，呃等等。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-27eb5eedca096082.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>gallery.php(id)，是不是sql注入。。？</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-ca2a8f4d62bab912.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>可是我没有输入单引号，它怎么说sql语法错误，这个鬼设计。。。</p><p>url再输入？id=1，显示正常页面。</p><p>em。。。。 没有传参就出错，传参就正常，结合上图could not select category</p><p>说明sql语句可能如下：<a href="https://www.jianshu.com/p/4469faff917f" target="_blank">理由参考</a></p><blockquote><p>select 列名 from 表名 where 目录（category）</p></blockquote><p>这里category——目录应该是id=1，如果没有正确传参，那么sql查询语句就会出错。</p><p>再次验证一下，通过id=1，页面正常，id=1' ，页面出错，错误提示和上图一样。基本可以确认漏洞。<a href="https://www.jianshu.com/p/e8b7f72d7c3b" target="_blank">理由</a>。</p><p>用sqlmap如行云流水般的获取到数据库管理员账号和密码。这里就不展开sqlmap用法了，不然文章就太长了。</p><p>下一步是登陆后台，传webshell，获取最高权限。</p><p><a href="https://www.jianshu.com/p/cc45299e6b2c" target="_blank">后续</a></p>
        </div>
      </div>
    </div>
  </body>
</html>
