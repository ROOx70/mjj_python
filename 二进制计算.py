
from random import *    #导入random模块
    
class Wind:
    "用于绘制窗口的类"

    def __init__(self,wide=20,high=8):
        "用于初始化的方法"
        self.wide = wide    #初始化宽度
        self.high = high    #初始化高度
        

    def print_rt(self,title='',text_play='',text_set='',text_quit='',text_1='',set_3=-1,set_4=-1,set_5=-1,set_6,ps_text='',ps='off'):
        "用于打印界面的方法"
        
        for i in range(1,self.high+1):

            if i == 1:  #当是界面的第一行时
                tit = len(title)    #变量tit用于统计title实参文字数量方在下面再添加文字是不打乱原本绘制窗口的符号#
                self.s_t = (self.wide - tit)     #用宽度减去输入字的数量从而计算出#号的数量
                print('#'*self.s_t+title+'#'*self.s_t)    
            
            elif i == 2 and ps == 'on':
                print('#'+' '*(self.wide*2-2)+'#'+' '*5+f'ps:{ps_text}')

            elif i == 3:    #当界面是第三行时
                ply = len(text_play)    
                pl = (self.wide-ply+set_3)  
                print('#'+' '*pl+text_play+' '*pl+'#')

            elif i == 4:
                set_0 = len(text_set) 
                se = (self.wide-set_0+set_4)
                print('#'+' '*se+text_set+' '*se+'#')

            elif i == 5:
                qui = len(text_quit)   
                qu = (self.wide-qui+set_5)
                print('#'+' '*qu+text_quit+' '*qu+'#')

            elif i == 6:
                text_01 = len(text_1)   
                qu = (self.wide-text_01+set_6)
                print('#'+' '*text_01+text_1+' '*text_01+'#')

            elif i >1 and i <self.high:     #当中间没有文字时择默认打印
                print('#'+' '*(self.wide*2-2)+'#')    #先打印第一个#然后再通过减去总宽度两边的#算出中间空的大小
            
            else:
                print('#'*self.wide*2)    #当在窗口最后排时打印宽度大小的#
def ran(end_num,end_num_1):
    randnums = []
    for i in range(1,end_num-1):
        randnum = randint(1,end_num_1)
        randnums.append(randnum)
    if end_num == 4

        ###############################################主程序的调用############################
Wind().print_rt('终端开发','开始','','退出',ps_text='用回车键可以实现按钮切换',ps='on')
while True:
        input('')
        Wind().print_rt('终端开发','>>开始<<','','退出',ps_text='用回车键可以实现按钮切换',ps='off',set_3=1)
        xuanzhe = input(' '*8+'(y/n):')

        ###############################################开始功能制作############################

        if xuanzhe.lower() =='y':

            Wind().print_rt('工具栏','二进制计算','','退出',ps_text='用回车键可以实现按钮切换',ps='on')
            q =True
            while q:
                input('')
                Wind().print_rt('工具栏','>>二进制计算<<','','退出',ps_text='开发:明靖杰',ps='on',set_3=1)
                xuanzhe = input(' '*8+'(y/n):')

                if xuanzhe.lower() =='y':
                    Wind().print_rt('二进制计算','简单','普通','困难',ps_text='用回车键可以实现按钮切换',ps='off')
                    while q:
                        input('')
                        Wind().print_rt('二进制计算','>>简单<<','普通','困难',ps_text='简单(1~50)',ps='on')
                        xuanzhe = input(' '*8+'(y/n):')
                        ###########二进制简单功能编写#########
                        if xuanzhe.lower() =='y':
                            ran(3,50)
                            Wind().print_rt('二进制计算',str(randnums_ez[0]),'普通','困难',ps_text='简单(1~50)',ps='on')

                        elif xuanzhe.lower() =='n':
                            pass

                    

                elif xuanzhe.lower() =='n':

                    Wind().print_rt('工具栏','二进制计算','','>>退出<<',ps_text='用回车键可以实现按钮切换',ps='off',set_5=1)
                    xuanzhe = input(' '*8+'(y/n):')

                    if xuanzhe.lower() =='y':
                        q = False

                    elif xuanzhe.lower() =='n':
                        pass

                
        elif xuanzhe.lower() =='n':

        ##############################################退出功能制作############################

            Wind().print_rt('终端开发','开始','','>>退出<<',ps_text='用回车键可以实现按钮切换',ps='off',set_5=1)
            xuanzhe = input(' '*8+'(y/n):')

            if xuanzhe.lower() =='y':

                exit()
            elif xuanzhe.lower() =='n':
                pass        
            
        

    



