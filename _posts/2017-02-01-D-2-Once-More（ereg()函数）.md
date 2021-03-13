<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>D.2.Once More（ereg()函数）</title>
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
        <h1 class="title">D.2.Once More（ereg()函数）</h1>
        <div class="show-content">
          <p>http://www.shiyanbar.com/ctf/1805</p><p>1.ereg（），对比解析函数，与大小写有关，看两个字符串是不是相等的。</p><p>2.strpos() 函数查找字符串在另一字符串中第一次出现的位置。strpos(<i>string</i>,<i>find</i>,<i>start</i>)</p><p>3.strlen()，返回字符串的长度。</p><p>4.在科学计数法中，为了使公式简便，可以用带“E”的格式表示。例如103乘10的6次方，可简写为“103E+6”的形式</p><hr><p>分析一下题，第一个if,要求password不为空，这个就不说了</p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-9d17517171c67cce.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-9d17517171c67cce.png?imageMogr2/auto-orient/strip" data-image-slug="9d17517171c67cce" data-width="713" data-height="612"><br><div class="image-caption"></div>
</div><p>第二个if，不太熟悉啊。。对比大小写的全部英文字母加十个数字，如果===表示恒等，要求字符串的值和类型完全相等。后面的FALSE是什么意思，是恒等还是不等的时候输出”你的密码必须为字母或数字“？那我们就试试吧。</p><p>哦，好像是要求我们密码必须为字母或者数字，如果加了什么奇奇怪怪的符号就会显示下图的结果。</p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-55e02617187b2ee1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-55e02617187b2ee1.png?imageMogr2/auto-orient/strip" data-image-slug="55e02617187b2ee1" data-width="698" data-height="338"><br><div class="image-caption"></div>
</div><p>第三个else if，要求密码长度小于8，数值大于9999999，而7位数最大也就是七个9，要大于它，就用科学记数法。</p><p>第四个if，要求密码里包含*-*，</p><p>据说ereg()函数，在遇到%00时候就会停止。</p><p>构造1E7%00*-*（10的7次方，由于浏览器解码将%00当成十六进制的一个字符，前面三个加这一个加后面*-*，总共7个字符。）</p><p>于是提交password=1E7%00*-*</p>
        </div>
      </div>
    </div>
  </body>
</html>
