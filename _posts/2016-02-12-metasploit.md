---
categories:
- tools
tags: 
    - tools
---
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>metasploit</title>
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
        <h1 class="title">metasploit</h1>
        <div class="show-content">
          <div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-68657d0e296bc7cc.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-68657d0e296bc7cc.PNG?imageMogr2/auto-orient/strip" data-image-slug="68657d0e296bc7cc" data-width="646" data-height="324"><br><div class="image-caption"></div>
</div><p>可以<a href="http://www.freebuf.com/articles/network/33905.html" target="_blank">参考</a> ，freebuf对于这些内容介绍的非常全</p><p>msfconsole</p><p>msfupdate 更新meta</p><p><b>1.show expoits  /显示可用的渗透攻击模块</b></p><p>1.1.show auxiliary / 显示辅助模块</p><p>1.2.back / 返回上一级</p><hr><p><b>3.search xxx / 查找某漏洞对应的攻击模块</b></p><p><b>4.use xxx / 找到模块后，复制模块的路径xxx</b>，用use选项使用</p><p><b>5.show options / 显示可用参数</b></p><p><b>6.show targets / 显示受影响漏洞os版本的信息</b></p><p>6.1 info / 更详细的信息</p><p><b>7 set RHOST XXX / 设置目标ip(XXX</b>)</p><p>7.1 set TARGET N / 设置目标的os版本的数字编号，os版本编号应该在第五步列出来了。os版本应该在设置目标ip之前，就探测清楚了。</p><p>7.2 show options / 检查我们设置的参数是否正确</p><p><b>8.1 exploit / 开始利用漏洞</b></p><hr><p><b>help  当你不确定命令xx的时候，用help xx，显示帮助信息</b></p><p><a href="https://jingyan.baidu.com/article/454316ab693a00f7a6c03a75.html" target="_blank">连接postgres数据库</a></p><p>db_status</p><p>db_connect 连接数据库情况</p><p>import xx.xml 将xx.xml导入数据库</p><p>db_hosts -c address 显示数据库中已经扫描的ip</p><blockquote>
<p>[!] Database not connected or cache not built, using slow search</p>
<p>如果你看到了这个消息，说明没有连接数据库或者没有建立缓存</p>
<p>db_rebuild_cache　　重建数据库缓存，方便快速搜索</p>
</blockquote><p>msf &gt; db_connect msf123:123456@127.0.0.1/msf1</p>
        </div>
      </div>
    </div>
  </body>
</html>
