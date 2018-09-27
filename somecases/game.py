import random
sub_str=random.randint(1,101) #生成1-100的一个随机数
while 1:#while的意思就是，让它一直为真，也就是死循环，下面通过break来停止循环
    num=int(input('please enter a num , 1-100:'))
    if num>100 or num<1: #判断输入的数字是否在1-100之间
        print('num error,please enter 1-100.')
        continue
    else:
        if num==sub_str: #如果猜对了，结束循环
            print('You win.Game over,the num is %d'%sub_str)#不懂这个的请看下面的第十四，字符串格式化输出
            break
        elif num < sub_str:#如果猜小了，就跳出本次循环，提示猜小了
            print('The num is too small,please enter another one.')
            continue
        else:#就三种情况，大、小等于，前面两种是等于和小于，那么else就是大于了，如果猜大了，就跳出本次循环，提示猜大了
            print('The num is too big,please enter another one.')
            continue