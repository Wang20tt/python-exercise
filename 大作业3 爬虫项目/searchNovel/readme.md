

首先get_ThreeKingdoms.py获取目标网站http://sanguo.5000yan.com/所有url

![image-20210418231916212](C:\Users\xukai\AppData\Roaming\Typora\typora-user-images\image-20210418231916212.png)

共一百二十回

然后再分别对每一回进行爬取

![image-20210418232026578](C:\Users\xukai\AppData\Roaming\Typora\typora-user-images\image-20210418232026578.png)

爬取所有正文内容。并存入novel/三国演义.txt文件中

![image-20210418224705622](C:\Users\xukai\AppData\Roaming\Typora\typora-user-images\image-20210418224705622.png)

![image-20210418224816059](C:\Users\xukai\AppData\Roaming\Typora\typora-user-images\image-20210418224816059.png)

然后在使用jieba+whoosh进行全文检索

![image-20210418232247087](C:\Users\xukai\AppData\Roaming\Typora\typora-user-images\image-20210418232247087.png)

还未完全完成，完成一部分