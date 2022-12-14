import io
import os
import sys

from jieba.analyse import ChineseAnalyzer
from whoosh.fields import *
from whoosh.index import create_in, open_dir
from whoosh.qparser import QueryParser

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

#导入中文分词工具
analyser = ChineseAnalyzer()
#创建索引结构
schema = Schema(full_line=TEXT(stored=True,analyzer=analyser))
#数据和索引所在目录，以及索引名称
ix = create_in("novel_idx",schema=schema,indexname='allin1line')

#返回root下的文件列表
def traverseFile(root):
    flist = []
    for f in os.listdir(root):
        f_path = os.path.join(root,f)
        if os.path.isfile(f_path):
            flist.append(f_path)
            print(f_path)
        else:
            flist += traverseFile(f_path)
        return flist

#处理数据文件
writer = ix.writer()
for fn in traverseFile("novel"):
    with open(fn,'r',encoding='utf-8') as f:
        print(fn,"...")
        lines = 0
        while True:
            line1 = f.readline()
            if line1:
                writer.add_document(full_line=line1)
                lines += 1
            else:
                break
        print(fn,lines,"added")
writer.commit()
print("index finished")
index1 = open_dir("novel_idx",indexname='allin1line')
parser1 = QueryParser("full_line",index1.schema)
while True:
    with index1.searcher() as searcher:
        print("please input what you want to search:")
        key = input()
        myquery = parser1.parse(key)
        results = searcher.search(myquery,limit=2000)
        for result1 in results:
            d1 = dict(result1)['full_line']
            print(d1)