from langconv import *
with open('question_labels.json', 'r',encoding='UTF-8') as f:
    question_labels = json.load(f)

q_zh = []   #   Data中问题的中文
for line in question_labels:
    q_zh.append(line['q_zh'])

print(q_zh)
def Traditional2Simplified(sentence):
    sentence = langconv.Converter('zh-hans').convert(sentence)
    return sentence

q_zh_jian = []
for line in q_zh:
    q_zh_jian.append(Traditional2Simplified(line))

print(q_zh_jian)