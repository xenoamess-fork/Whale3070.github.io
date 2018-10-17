[靶机下载地址](https://www.vulnhub.com/entry/rotating-fortress-101,248/)
## 扫描
感觉有两种特别难突破防线，一种可以搜集的信息特别特别少，端口只开了一两个；一种信息特别特别多，不知道从哪里下手==

这种貌似就是特别少的那种。
端口：80（http）、27025（unknown）

#### http服务
访问80端口，自动跳转/Janus.php，只有一行字，你不是admin。。
除此之外没有任何可用页面（网站地图爬行过）

#### unknown服务
![1]($res/1.PNG)
先扫描这个端口，发现nmap扫不出什么服务，nc和浏览器得到一样的response，拒接连接。
应该是我没有用正确的方式连接造成的。

## info1
把cookie从0改为1，得到的信息：
```
<html>

  <title>Janus</title>

  <body>Welcome Back Admin Last edited file was: /LELv3FfpLrbX1S4Q2FHA1hRtIoQa38xF8dzc8O9z/home.html Flag: 1{7daLI]} ggez</body>

</html>
```
## web分析
访问下这个页面，这么长url，难怪扫不出来..
http://192.168.1.131/LELv3FfpLrbX1S4Q2FHA1hRtIoQa38xF8dzc8O9z/home.html

源码注释：   
```
<!-- Loki here: once you guys get past isolation come to chat.php and we can try and regain control -->

 <!--
    <video  width=100% height=auto autoplay loop>
    <source src="/LELv3FfpLrbX1S4Q2FHA1hRtIoQa38xF8dzc8O9z/resources/Harpocrates.mp4">
    -->
```
于是访问下resources这个目录，找了一圈没啥有用的。

`dirb http://192.168.1.131/LELv3FfpLrbX1S4Q2FHA1hRtIoQa38xF8dzc8O9z/`

## info2
icons一般是图标之类的资源文件，没必要去看。
```
User-agent: *
Disallow: /
Disallow: /icons/loki.bin
Disallow: /eris.php
```
/eris.php
![2]($res/2.PNG)

初步判断是命令执行，在如图所示的exec command中可以反弹shell，但是需要用户名和密码，如果错误就会提示`ACCESS_DENIED`
```
<form action="eris.php" method="post">
Name: <input type="text" name="username"> <br>
Password: <input type="text" name="pass"> <br>
Exec Command: <input type="text" name="command"> <br>
```
当然也有可能是sql注入，尝试下特殊字符--;#'"
```
[Debain][SQL Server]Syntax error converting the varchar value '--' to a column of data type int. /eris/bypasser.asp, line 113
```
## 尝试sqlmap
将burp的requests文件保存为rotate.txt
sqlmap -r /root/Desktop/rotate.txt --dbs
失败。
sqlmap -u "http://192.168.1.131/LELv3FfpLrbX1S4Q2FHA1hRtIoQa38xF8dzc8O9z/eris.php" --data="username="
放弃

## 文件下载
返回/icons/loki.bin，点击后下载了loki.bin
```
file loki.bin
loki.bin: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=5ee04fe5ea96173af27612ff707628d8e684db16, not stripped
```
vi loki.bin
看到了连接拒接、连接感谢，于是联想到一开始那个unknown的端口

于是运行下
```
./loki.bin
Enter Password: rxmg7n83qv98by（瞎猜的密码）

access_denied 
```
## 二进制分析
通过一样的access_denied，说不定是让我们分析这个bin文件，获得口令后，就可以执行命令。
![3]($res/3.PNG)
web狗拿起键盘就是干！
![4]($res/4.PNG)
ida分析，elf格式64位的程序，可以看到分支跳转密码。

首先，分析下，密码是不是明文写在程序中的。
![5]($res/5.PNG)
看来不是。

静态分析了一下，但是ollydbg是windows平台的，不能运行linux可执行程序，这下就犯愁了。
kali搜索一下db (debugger)，还真找到了edb，没用过。。

#### EDB
A Linux equivalent of the famous Olly _debugger_ on the Windows platform.
貌似和ollydbg差不多，先找到输入密码后的跳转地址。
![6]($res/6.PNG)
jnz结果不为零（或不相等）则转移。
jz=jump if zero，一般与cmp连用，用以判断两数是否相等。
在这里，绿色的是条件符合继续执行（不跳转），红色是不符（跳转）。
现在问题是，我们不知道需要输入什么密码，才能跳转到access_granted。

#### strings字符串分析
```
#strings loki.bin
/lib64/ld-linux-x86-64.so.2
libc.so.6
gets
puts
putchar
printf
__cxa_finalize
strcmp
__libc_start_main
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
=q# 
5j# 
=!# 
=n" 
=p! 
=r  
AWAVI
AUATL
[]A\A]A^A_
access_denied 
access_granted! 
Enter Password: 
;*3$"
backd00r_pass123
GCC: (Debian 7.3.0-21) 7.3.0
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.7090
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
buffer.c
__FRAME_END__
__init_array_end
_DYNAMIC
__init_array_start
__GNU_EH_FRAME_HDR
_GLOBAL_OFFSET_TABLE_
__libc_csu_fini
putchar@@GLIBC_2.2.5
_ITM_deregisterTMCloneTable
puts@@GLIBC_2.2.5
tmp2
_edata
printf@@GLIBC_2.2.5
__libc_start_main@@GLIBC_2.2.5
__data_start
strcmp@@GLIBC_2.2.5
__gmon_start__
__dso_handle
_IO_stdin_used
access_granted
gets@@GLIBC_2.2.5
__libc_csu_init
__bss_start
main
access_denied
__TMC_END__
_ITM_registerTMCloneTable
__cxa_finalize@@GLIBC_2.2.5
.symtab
.strtab
.shstrtab
.interp
.note.ABI-tag
.note.gnu.build-id
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rela.dyn
.rela.plt
.init
.plt.got
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.init_array
.fini_array
.dynamic
.got.plt
.data
.bss
.comment
```
buffer.c，strcmp
猜测，是让我们用缓冲区溢出的方法得到密码。
这个程序应该是用c语言写的，strcmp是复制函数，典型的用不好就会导致溢出。

输入超长密码，显示段错误。
![Screenshot from 2018-10-14 00-54-50]($res/Screenshot%20from%202018-10-14%2000-54-50.png)

![Screenshot from 2018-10-14 01-01-05]($res/Screenshot%20from%202018-10-14%2001-01-05.png)

#### IDA Pro
F5反编译（ida专业版才有这个功能。。）
```
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char *v3; // rdi
  char s1; // [rsp+0h] [rbp-200h]
  int i; // [rsp+1FCh] [rbp-4h]

  for ( i = 0; i <= 18; ++i )
  {
    envp = (const char **)i;
    tmp[i] = *((_DWORD *)&g + i);
  }
  printf("Enter Password: ", argv, envp);
  gets(&s1);
  putchar(10);
  if ( !strcmp(&s1, tmp) )
    return access_granted(&s1, tmp);
  v3 = &s1;
  if ( !strcmp(&s1, tmp2) )
  {
    for ( i = 0; i <= 74; ++i )
      tmp[i] = *((_DWORD *)&s + i);
    printf(tmp, tmp2);
    v3 = byte_9 + 1;
    putchar(10);
  }
  return access_denied(v3, tmp2);
}
```
- `strcmp(&s1, tmp)`
如果一致，就成功了。比较s1 and tmp，s1是输入的字符串
- `tmp[i] = *((_DWORD *)&g + i);`
tmp是从g取出18位

双击g这个数组，因为tmp从这里取值，18位。目的是定位，然后查看对应的hex view面板，十六进制
![7]($res/7.PNG)

![口令就是xBspsiONMSNXeVuiomF]($res/TIM%E5%9B%BE%E7%89%8720181017151015.png)

[wp](https://hackso.me/rotating-fortress-1.0.1-walkthrough/)贴这儿了，最近