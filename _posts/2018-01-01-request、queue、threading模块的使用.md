---
title: request、queue、threading模块的使用
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
    <title>request、queue、threading模块的使用</title>
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
        <h1 class="title">request、queue、threading模块的使用</h1>
        <div class="show-content">
          <div class="image-package">
<img data-height="77" data-width="477" data-image-slug="6e7c263f10c3bbfc" src="http://upload-images.jianshu.io/upload_images/2883590-6e7c263f10c3bbfc.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-6e7c263f10c3bbfc.PNG?imageMogr2/auto-orient/strip"><br><div class="image-caption"></div>
</div><p>知识点一：urllib2模块，可以被用来做web交互。因为谷歌被墙，访问失败，所以改成百度试下。</p><br><div class="image-package">
<img data-height="214" data-width="814" data-image-slug="a4b6852b935ffd2d" src="http://upload-images.jianshu.io/upload_images/2883590-a4b6852b935ffd2d.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-a4b6852b935ffd2d.PNG?imageMogr2/auto-orient/strip"><br><div class="image-caption"></div>
</div><hr><p>也可以自定义特定的http头，cookie,POST请求之类的。</p><div class="image-package">
<img data-height="193" data-width="452" data-image-slug="bc36d850b475d034" src="http://upload-images.jianshu.io/upload_images/2883590-bc36d850b475d034.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-bc36d850b475d034.PNG?imageMogr2/auto-orient/strip"><br><div class="image-caption"></div>
</div><hr><p>知识点二：Queue模块,提供队列操作。队列，是python中线程常用的交换数据的形式。</p><div class="image-package">
<img data-height="413" data-width="503" data-image-slug="9f7d19f8b9f9bc74" src="http://upload-images.jianshu.io/upload_images/2883590-9f7d19f8b9f9bc74.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-9f7d19f8b9f9bc74.PNG?imageMogr2/auto-orient/strip"><br><div class="image-caption">先进先出队列</div>
</div><div class="image-package">
<img data-height="342" data-width="491" data-image-slug="385dd8890f95d1bb" src="http://upload-images.jianshu.io/upload_images/2883590-385dd8890f95d1bb.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-385dd8890f95d1bb.PNG?imageMogr2/auto-orient/strip"><br><div class="image-caption">先进后出队列</div>
</div><p>？为何先进后出 结果为0，1，2，3，4。因为range(5）都是从4开始数的，4，3，……，所以先数的，就要排在后面输出。</p><hr><p>知识点三：线程模块threading</p><div class="image-package">
<img data-height="472" data-width="516" data-image-slug="872f32f0970daed3" src="http://upload-images.jianshu.io/upload_images/2883590-872f32f0970daed3.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-872f32f0970daed3.PNG?imageMogr2/auto-orient/strip"><br><div class="image-caption">继承thread类，创建线程</div>
</div><div class="image-package">
<img data-height="373" data-width="666" data-image-slug="8e06bc1a8df0f29c" src="http://upload-images.jianshu.io/upload_images/2883590-8e06bc1a8df0f29c.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-8e06bc1a8df0f29c.PNG?imageMogr2/auto-orient/strip"><br><div class="image-caption">第二种方法，创建threading.Thread对象，来创建线程<br>
</div>
</div>
        </div>
      </div>
    </div>
  </body>
</html>
