import bs4
import requests,sys
from bs4 import BeautifulSoup
class downloader(object):
    def __init__(self):
        self.server = 'http://sanguo.5000yan.com/'
        self.names = []     #章节名
        self.urls = []      #章节链接
        self.nums = 0       #章节数

    def get_download_url(self):
        req = requests.get(url = self.server)
        req.encoding = 'GBK'
        req.encoding = 'utf-8'
        html = req.text
        html.replace('\xa0','\n')
        ul_bf = bs4.BeautifulSoup(html,'lxml')
        ul = ul_bf.find_all('ul', class_='paiban')
        a_bf = BeautifulSoup(str(ul[0]),"lxml")
        a = a_bf.find_all('a')
        self.nums = len(a)
        for each in a:
            self.names.append(each.string)
            self.urls.append(each.get('href'))

    def get_contents(self,target,name,path):
        write_flag = True
        req = requests.get(url=target)
        req.encoding = 'GBK'
        req.encoding = 'utf-8'
        html = req.text
        bf = BeautifulSoup(html, 'lxml')
        div = bf.find_all('div', class_='grap')
        div_bf = BeautifulSoup(str(div[0]),'lxml')
        divIn = div_bf.find_all('div')
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
        for each in divIn:
            content = each.text.replace('\xa0','')
            with open(path, 'a', encoding='utf-8') as f:
                f.writelines(content)
        with open(path, 'a', encoding='utf-8') as f:
            f.write(''+'\n\n')


if __name__ == '__main__':
    dl = downloader()
    dl.get_download_url()
    print('《三国演义》正在下载：')
    for i in range(dl.nums):
        dl.get_contents(dl.urls[i],dl.names[i], 'novel/三国演义.txt')
        sys.stdout.write("已下载：%.3f%%" % float(i/dl.nums*100) + '\r')
        sys.stdout.flush()
    print('《三国演义》下载完成')

