<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>kiotrix靶机（139端口samba）</title>
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
        <h1 class="title">kiotrix靶机（139端口samba）</h1>
        <div class="show-content">
          <p><a href="http://www.kioptrix.com" target="_blank">靶机下载地址</a> </p><p>攻击机kali linux：192.168.1.111   靶机kiotrix level 1 linux：192.168.1.104</p><hr><p>unicornscan -mT -r500 -I 192.168.1.104</p><p>unicornscan -mU -r500 -I 192.168.1.104</p><p>先扫所有TCP端口、再扫UDP端口。</p><p>-mT 默认tcp扫描</p><p>-r500 每秒发送500个数据包</p><p>-I 输出扫描信息</p><p>-mU udp扫描</p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-fa6f5a3bd13c870c.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-fa6f5a3bd13c870c.PNG?imageMogr2/auto-orient/strip" data-image-slug="fa6f5a3bd13c870c" data-width="702" data-height="240"><br><div class="image-caption"></div>
</div><p>确定了靶机开放的TCP、UDP端口。</p><p>TCP：22，80，111，139，443，1024 ；UDP ,111,137</p><hr><p>根据上一步扫描出的端口，用nmap再扫描，确定端口的详细信息。</p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-441f95b4048dae68.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-441f95b4048dae68.PNG?imageMogr2/auto-orient/strip" data-image-slug="441f95b4048dae68" data-width="741" data-height="403"><br><div class="image-caption"></div>
</div><p>nmap -n -sTUV -pT:22,80,111,139,443,1024,U:111,137 192.168.1.104</p><p>-sTUV：表示扫描TCP和UDP的端口，确定端口的状态，并且输出相关软件的版本信息；</p><p>-p：表示指定扫描的范围，以及需要扫描的端口；</p><hr><p>上一步看到139端口开放了samba服务</p><p>-L 连接到ip    -N表示没有密码用匿名登陆</p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-93db6759bfb44e4a.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-93db6759bfb44e4a.PNG?imageMogr2/auto-orient/strip" data-image-slug="93db6759bfb44e4a" data-width="668" data-height="408"><br><div class="image-caption"></div>
</div><p>获得samba 版本2.2.1a</p><p>在exploit-db上寻找现成的exploit</p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-9358c0c102056e0c.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-9358c0c102056e0c.PNG?imageMogr2/auto-orient/strip" data-image-slug="9358c0c102056e0c" data-width="1223" data-height="166"><br><div class="image-caption"></div>
</div><hr><p>也可以直接在metasploit上搜索</p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-d4220f5b1dde1385.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-d4220f5b1dde1385.PNG?imageMogr2/auto-orient/strip" data-image-slug="d4220f5b1dde1385" data-width="773" data-height="346"><br><div class="image-caption"></div>
</div><p>根据description选择恰当的漏洞利用模块，设置恰当的目标ip、端口、回连的本机ip、端口</p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-143f99ff3f676306.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-143f99ff3f676306.PNG?imageMogr2/auto-orient/strip" data-image-slug="143f99ff3f676306" data-width="810" data-height="302"><br><div class="image-caption"></div>
</div><p>获取了root权限之后，输入mail以及1，可以看到kioptrix制作者给我们的留言</p><p>“如果你看到了这个，说明你拿到了root权限，恭喜。</p><p>第二关不会这样简单…… ”</p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-13610fda58827bec.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-13610fda58827bec.PNG?imageMogr2/auto-orient/strip" data-image-slug="13610fda58827bec" data-width="759" data-height="324"><br><div class="image-caption"></div>
</div><p>23333</p>
        </div>
      </div>
    </div>
  </body>
</html>
