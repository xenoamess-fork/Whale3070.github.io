---

title: pythonGUI ( 一 )
categories:
- code
tags: 
    - code
---

## 参考资料：
《python GUI Programming Cookbook》
《Expert Python Programming》python高级编程
《代码整洁之道》

##  学习时间2018-0901——20181231

## 学习目标：

- 初级目标:
熟悉GUI的模块属性的调用。
习惯于全英文技术书籍的阅读。
- 中级目标：
熟练掌握python高级语法。
- 高级目标 
通过案例联系数据结构知识进行学习。
通过案例学习《代码整洁之道》，养成良好编码习惯
自定义项目练习。

python是动态类型语言，它可以从变量定义推断出类型。
主要使用tkinter模块，使用了titile属性——**标题**
Lable属性——设置**标签内容**
![1](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0910/1.PNG)

---

定义了一个函数，设置了点击后的行为
![2](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0910/2.PNG)

GUI是事件驱动的，点击就创建了一个事件。

---

按键输入的属性：
![3](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0910/3.PNG)

---

添加下拉选择框，坐标（1，1）：
![4](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0910/4.PNG)

---

定义点击后的显示文本
![5](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0910/5.PNG)

---

添加选择（是/否）按钮
![6](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0910/6.PNG)

---

添加单选按钮
![7](https://raw.githubusercontent.com/Whale3070/Whale3070.github.io/master/images/0910/7.PNG)

## 总结：
python图形化编程，一如python的风格，拿来即用地简单。通过使用tk库的不同属性，定义框框大小、按钮button的类型，字符串所在的位置。

一个有图形界面的程序就完成了。
- mark一下，免得遗忘。
1. xx = tk.Tk()
**xx是tk库的一个实例，以下都用xx举例**
2. 程序首要标题      
 `xx.title('mytitle')`
3. 程序定义框框坐标
column是横坐标，从上到下，从0开始，递增+1。
row是纵坐标，从左边到右边，从0开始，递增+1。
`ttk.Label(xx,text='new').grid(column=0,row=0)`
4. 点击后，程序响应行为：
首先定义一个行为函数，使得后面可以调用
定义了clickMe函数，点击new按钮，文字变为old。
```
def clickMe():
   myaction.configure(text='old')
myaction = ttk.Button(xx,text='new',command=clickMe)
```
5. 字符输入框
先创建tk的字符串变量实例name。
再创建ttk的输入框实例。
```
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)
nameEntered.focus()
```
6. 选择框
先创建tk的字符串变量实例chVarEn。
再创建tk的选择框实例。
```
chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win,text="Enabled",variable=chVarEn)
check3.select()
check3.grid(column=2,row=4,sticky=tk.W)
```
7. 单选框
还是三行搞定
先创建tk的字符串变量实例radVar。
再创建tk的单选框实例。
第三行设置一下坐标。
```
radVar = tk.IntVar()
rad1=tk.Radiobutton(xx,text=COLOR1,variable=radVar,value=1,command=radCall)
rad1.grid(column=0,row=5,sticky=tk.W)
```

