<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>11.13google搜索语法</title>
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
        <h1 class="title">11.13google搜索语法</h1>
        <div class="show-content">
          <p>参考<a href="http://blog.csdn.net/cnasp/article/details/618686" target="_blank">Google hacking for penetration testers</a> <br></p><p>1搜集目标的信息，越多越好。</p><p>2列出可以攻击的ip地址列表。</p><p>使用工具时候，要分清哪些会跟目标接触。和目标联络的，叫主动侦察。</p><p>网上搜集信息，叫被动侦察。</p><hr><p>查找与四川大学的url有联系的网站</p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-004da08b98483ee9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-004da08b98483ee9.png?imageMogr2/auto-orient/strip" data-image-slug="004da08b98483ee9" data-width="501" data-height="587"><br><div class="image-caption"></div>
</div><hr><p>搜索所有<b>指向川大网站</b>的链接</p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-10b3f928650fcff9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-10b3f928650fcff9.png?imageMogr2/auto-orient/strip" data-image-slug="10b3f928650fcff9" data-width="557" data-height="572"><br><div class="image-caption"></div>
</div><hr><p>搜索<b>链接包含的关键字+网页包含的关键字</b>。后面的网页关键字也可以不加。</p><p><br></p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-5643ecec2203a00d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-5643ecec2203a00d.png?imageMogr2/auto-orient/strip" data-image-slug="5643ecec2203a00d" data-width="614" data-height="589"><br><div class="image-caption"></div>
</div><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-87046162ed1bf073.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-87046162ed1bf073.png?imageMogr2/auto-orient/strip" data-image-slug="87046162ed1bf073" data-width="585" data-height="623"><br><div class="image-caption"></div>
</div><hr><p>allinurl,查询<b>链接中的关键字</b>，和inurl不同的是，不查询网页的关键字。并且搜索结果要包含全部的关键字（all+inurl的含义）</p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-4817045ecfe438e3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-4817045ecfe438e3.png?imageMogr2/auto-orient/strip" data-image-slug="4817045ecfe438e3" data-width="670" data-height="584"><br><div class="image-caption"></div>
</div><p><br></p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-d53dd5a483b6c2fa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-d53dd5a483b6c2fa.png?imageMogr2/auto-orient/strip" data-image-slug="d53dd5a483b6c2fa" data-width="645" data-height="576"><br><div class="image-caption"></div>
</div><p>看看两次查询有何不同。inurl查询了网页内容，下面有红色字体的。。</p><hr><p>查询网页标题，allintitle,intitle，区别就是all,前者要包含全部的关键字。</p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-35212c98a6682930.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-35212c98a6682930.png?imageMogr2/auto-orient/strip" data-image-slug="35212c98a6682930" data-width="697" data-height="581"><br><div class="image-caption"></div>
</div><p><br></p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-4c7a6fd72cbf5cfc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-4c7a6fd72cbf5cfc.png?imageMogr2/auto-orient/strip" data-image-slug="4c7a6fd72cbf5cfc" data-width="739" data-height="620"><br><div class="image-caption"></div>
</div><p>类似的，intext搜索网页正文部分，filetype搜索指定类型的文件。</p><hr><p>只显示网页快照里的信息cache:xxx.com</p>
        </div>
      </div>
    </div>
  </body>
</html>
