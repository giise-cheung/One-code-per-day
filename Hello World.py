import time
import os


class main:
    def __init__(self):
        self.judge()


    def judge(self):
        X = input("输入你需要的功能(1.弹窗显示,2执行CMD): ")
        if X =='1':
            self.showvbs()
        elif X == '2':
            self.cmdtext()
        else:
            print('你的输入有误,请重新输入!')

    def showvbs(self):
        a=input("输入你想说的话A: ")#input是Pyhton系统自带函数,用于获取在控制台获取键盘输入,所获取的输入都是字符形式.
        b=input("输入你想说的话B: ")

        text= a + b #text是新声明变量,把a跟b的输入文字会将两段文字组合成一句.
        showtime=(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))#获取当前电脑时间,已yyyy-mm-dd hh:mm:ss的形式显示
        cmd = """mshta vbscript:msgbox("""+'"'+text+' '+showtime+'"'+""",64,"Hello world")(window.close)"""#CMD的VBS命令,用于弹窗.其中我们将text跟showtime结合起来.使得弹窗显示动态内容.
        #os.system(cmd)#利用os包执行上面的CMD命令
        os.system(cmd)
  
    def cmdtext(self):
        text = input("输入你的CMD命令: ")
        print(os.popen(input("输入你的CMD命令: ")).read())
        cmd = """mshta vbscript:msgbox("""+'"已执行CMD命令: '+text+' '+(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+'"'+""",64,"Hello world")(window.close)"""
        os.system(cmd)


if __name__ == "__main__":
    main=main()
