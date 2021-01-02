import time
import os


class main:
    def __init__(self):
        self.judge()


    def judge(self):
        X = input("输入你需要的功能(1.弹窗显示,2执行CMD): ")#获取判断条件.
        if X =='1':#如果输入的X的结果为1,则执行显示弹窗的模块.
            self.showvbs()
        elif X == '2':#如果X的输入结果为2,则执行调用CMD命令的模块
            self.cmdtext()
        else:#如果输入不在1跟2内,提示输入有误.
            cmd = """mshta vbscript:msgbox("你的输入有误,请重新输入!",64,"错误")(window.close)"""#VBS弹窗
            os.system(cmd)#执行上面的CMD内容,调用windows的VBS弹窗


    def showvbs(self):
        a=input("输入你想说的话A: ")#input是Pyhton系统自带函数,用于获取在控制台获取键盘输入,所获取的输入都是字符串形式.
        b=input("输入你想说的话B: ")

        text= a + b #text是新声明变量,把a跟b的输入文字会将两段文字组合成一句.
        showtime=(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))#获取当前电脑时间,已yyyy-mm-dd hh:mm:ss的形式显示
        cmd = """mshta vbscript:msgbox("""+'"'+text+' '+showtime+'"'+""",64,"显示输入")(window.close)"""#CMD的VBS命令,用于弹窗.其中我们将text跟showtime结合起来.使得弹窗内容可变.
        #os.system(cmd)#利用os包执行上面的CMD命令
        os.system(cmd)
  
    def cmdtext(self):
        text = input("输入你的CMD命令: ")
        print(os.popen(input("输入你的CMD命令: ")).read())#执行并在python控制台输出CMD执行结果.
        cmd = """mshta vbscript:msgbox("""+'"已执行CMD命令: '+text+' '+(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+'"'+""",64,"CMD命令执行")(window.close)"""
        os.system(cmd)


if __name__ == "__main__":
    main=main()
