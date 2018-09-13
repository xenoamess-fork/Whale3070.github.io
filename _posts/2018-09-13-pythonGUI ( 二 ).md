---

title: pythonGUI ( 二 )
categories:
- code
tags: 
    - code
---
继续上一篇。
我前些日子在某公司实习时候，负责writeup等文档的处理，需要批量给收到的文档打水印，因此写了一个python脚本。
现在把该脚本从命令行执行，添加图形化界面。

该程序的功能有：
1. 给png图片批量添加水印，可以选择两种不同的水印。
2. 给gif图批量添加水印。
3. 提取word文档中的所有图片，添加水印。
![1](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0913/1.PNG)
## 优化方案：
- 优化前：该程序通过文件后缀，png、gif、docx决定不同的执行方案。但是每一次都需要选择打哪一种水印（i、e）
- 优化后：现在用pythonGUI的单选按钮，默认水印i。
			  再用输入框，接受图片所在路径

## 构建图形界面
按照上一篇学到的知识，先画出图形化界面。
此时点击start，并没有任何作用，后面再加点击后的行为。
![2](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0913/2.PNG)
![3](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0913/3.PNG)

## 添加点击后的效果
运行前
![4](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0913/4.PNG)

运行后：
![5](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0913/5.PNG)

## 替换点击后的效果
上一步确认了点击是有效果的，然后定义几个函数，替换点击的效果。

问题：此时遇到了问题。因为我当初写代码时候很随意，现在代码乱七八糟的。该程序总共有三个py文件，其中一个是主文件，两个自定义的模块文件png、unzip。

---
错误示范：
该函数获取两个路径，把path路径下的压缩文件解压缩，然后保存到savepath路径下。

因为调用了zipfile模块，所以不走心地前面加了一个my （┬_┬），而且因为懒得打字，还丢掉了file...

```
def myzip(path,savepath):
    f=zipfile.ZipFile(path,'r')

    for file in f.namelist():
        f.extract(file,savepath)
```
正确示范：
`def extractDocx(path,savepath):`
- 名称应该**有意义**，它是做什么的，怎么用
  废话没有意义。Variable一词永远不应当出现在变量名中。Table一词永远不应当出现在表名中。
话说我经常用var作为变量名～>_<～
- 使用**可搜索**的变量名

---
整理前（213行），居然还找出了两个定义了却没有使用到的函数╭（′▽‵）╭
![6](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0913/6.PNG)

梳理后（174行），将变量名整理了，并且只用调用judgment函数，即可运行程序。
这样方面了后面，再添加GUI的代码。
![](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0913/7.PNG)

---

运行前
![8](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0913/8.PNG)

运行后
![9](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0913/9.PNG)
![10](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0913/10.PNG)

添加图形化界面程序初步
