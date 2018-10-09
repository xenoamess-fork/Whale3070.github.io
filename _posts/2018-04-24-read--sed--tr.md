
shell script（二）
===
续上篇。
## 案例三：用“read”，接受输入作为命令的变量。
![1](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0424/1.PNG)
一看到这么多没见过的命令，先别慌！其实很简单。
和上一个案例中一样，read用于读取使用者的输入，然后作为上图倒数两行命令的参数使用。
（解释：qcow2是一个虚拟机文件，这个命令的作用是压缩虚拟机的大小，方便在网络上传输）
这脚本会要求使用者提供需要压缩的虚拟机文件的名字（虚拟机通常很大），和压缩好的你起的名。
然后它就会去执行了！
很方便，再也不用输入很长很长的命令了。

## 案例四：sed
**s**team **ed**itor
可以分析标准输入数据，处理后再标准输出。
```
参数：
‐n 只有经过处理的那一行才会被列出来。
‐e ？
‐f 写入到某个档案里
‐r 使用延伸型正则表达式。
操作：
a‐‐add
c‐‐replace
s‐‐replace
d‐‐delete
i‐‐insert
p‐‐print
```
- 案例一（删除）
nl /etc/passwd | sed '2,5d' 把passwd文件的2‐5行删除
但是它只会更改后输出，不会更改原文件。
- 案例二（替换）
`sed 's/hello/world' input.txt > output.txt`
 把hello替换为world，输出到output.txt文件
`sed ‐i 's/hello/world' input.txt` 把hello替换为world，修改原文件。
如果input.txt有三个hello，上面的命令只会替换第一个。
`sed ‐i 's/hello/world/g' input.txt` 替换每一处匹配
`sed ‐i 's/hello/world/2g' input.txt` 从第二处匹配开始，替换后面所有匹配（忽略第一
处）
- 案例三（删除）
`sed '/^$/d' file` 删除空白行
- 案例四（替换）
`echo this is an example | sed 's/\w\+/[&]/g' \w+`匹配每个单词，用[&]替换它
结果：[this] [is] [an] [example]
- 案例五
有一些虚拟机，它们有各自的xml文档。但是虚拟机开机后，发现鼠标和物理机的不同步。
于是修改xml文档，用bash脚本批量修改。
![2](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0424/2.PNG)
## 案例五：用tr进行文本的替换
![3](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0424/3.PNG)
该脚本，将中文的左尖角替换为英文的，替换后，发现变成了三个英文左尖角。
可能是字节长度不同的原因。
于是再用‐s 参数压缩一下，把三个压缩为一个。


