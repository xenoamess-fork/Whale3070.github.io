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
    <title>about--openvpn</title>
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
        <h1 class="title">about--openvpn</h1>
        <div class="show-content">
          <p>学习下vpn的用法，所谓vpn就是虚拟专用网络。（不懂的人请仔细阅读《计算机网络-第四版》这里就不展开了）。</p><p>openvpn是一个软件，可以通过该软件，连接到专用网络。</p><hr><p><a href="https://lab.pentestit.ru/signup" target="_blank">实验注册</a>  TEST LAB </p><p>网站 https://lab.pentestit.ru/ ，登陆后可以看见右上角。点击how to connect，可以看到openvpn的账号和密钥。点config，下载openvpn配置文件。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-57dbece7590fd3be.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>kali linux输入：<b>openvpn --config 下载好的文件名</b></p><p><b>https://jhalon.github.io/pentestit-lab-10-intro/</b></p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-b3f2e5ce20112de9.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>test lab渗透实验室vpn竟然连不上。。算了，放弃</p><hr><p>2018.2.11更新，尝试连接另一个vpn网络，属于hack the box实验室。</p><blockquote><p>openvpn --version  该命令可查看软件版本</p></blockquote><p>连接步骤：1.下载openvpn的配置文件。2.连接（需要openvpn软件客户端安装并正确配置）</p><blockquote><p>openvpn --config whale3070.ovpn</p></blockquote><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-9d5fd97fa31136fa.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>这是什么意思没搞懂，，然后去搜一下，哦，initialization sequence completed说明连接成功了。</p><p>（请忽略我最下面两条随便输入的东西，输入程序没有任何反应。）</p><blockquote><p>ifconfig</p></blockquote><p>显示：eth0，这是本地网卡，192.168.1.107 ，255.255.255.0</p><p>           tun0，发现多了一个网络，10.10.15.14，子网掩码：255.255.254.0</p><p>于是可以用python脚本计算下网段，再扫下网段</p><p>nmap -sn 10.10.14.0/23</p><p>10.10.14.1 估计是网关</p><p>10.10.15.24  本机</p><p>好了，openvpn就连上了，可以愉快地做实验了。</p>
        </div>
      </div>
    </div>
  </body>
</html>
