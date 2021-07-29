## KeywordExtractor

关键词提取函数`keyword_extract()`提供了从文本中提取关键词的功能。

```python
keyword_extract(text: str, *method: int) -> list
```

第一个参数接受字符串，可以是文本内容，也可以是文件路径。

第二个参数为可选项，无参数传入时使用jieba库提供的方法；传入参数与实际使用的方法对应关系为：

| method=?   | 实际使用方法                   |
| ---------- | ------------------------------ |
| 0(default) | `jieba.analyse.extract_tags()` |
| 1          | LDA                            |
| 2          | RaKUn                          |
| 3          | TF-IDF                         |

文件结构为：

+ data：所用的数据，包括语料库，临时文件等
  + corpus：语料库，存放corpus2021.txt，所用的语料库
  + 若干stopword的txt文档：各个算法所用的停止词
  + \[算法名\]：对应算法所需要的依赖文件、临时文件
+ model：各个算法的
  + \[算法名\]：对应算法的实现
+ main.py：主要文件，提供了`keyword_extract()`
+ testdoc.txt：提供的测试样例文件
+ testdocLong.txt：提供的测试文件，文本较长

