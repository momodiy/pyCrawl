## 坑点
- 1.文件名与包名不能相同
- 2.标签节点转化为字符串

在文件保存时，write方法需要接收一个字符串类型的方法否则会抛出一个异常，转化需用到get_text()方法。

    # 将节点信息转化为字符串；strip设置为true意为去除首尾字符串的空格
    node.text('', strip=True)
    
 - 3.命令行执行文件操作的python文件
在命令行中执行用于文件操作的python文件，首先需要用`cd`命令切换文件路径至待执行的文件的路径下，否则直接执行时，文件内的路径读取将会从你命令行的当前路径开始读取，导致文件保存失败等异常。

举个栗子，刚打开命令行此时的路径为 `C:\Users\Stevenlee`，此时要想执行`F:\python\demo\fileOperate.py`文件，当直接使用命令`python F:\python\demo\fileOperate.py`执行文件时会基于`C:\Users\Stevenlee`这个路径进行文件操作，可能会出现一些异常，因此使用命令行操作文件时应首先执行`cd F:\python\demo\`切换路径，再通过命令`python fileOperate.py`执行。