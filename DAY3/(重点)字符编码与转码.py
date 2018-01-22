# Author: Li tianyang
#-*-coding:gbk-*-
#当文件编码是什么的时候  头文件就写成什么
#上一行只是文件编码
#所有不同国家的编码都需要通过Unicode作为媒介来转换，在python3中默认都是Unicode，python2中默认是ASCII

s= "你好"    #此处会报错，文件编码以GBK编码，
            #程序里面还是Unicode


'''记住 金角大王的那个图 '''

#编码应用比较多的场景应该是爬虫了，互联网上很多网站用的编码格式很杂，虽然整体趋向都变成utf-8，但现在还是很杂，
#所以爬网页时就需要你进行各种编码的转换，不过生活正在变美好，期待一个不需要转码的世界。
#编码is a piece of fucking shit, noboby likes it