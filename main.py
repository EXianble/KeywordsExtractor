import model.rakun.rakun as ra
import model.tfidf.TFIDF as ti
import model.lda.LDA as lda
import os
import jieba.analyse

_get_abs_path = lambda path: os.path.normpath(os.path.join(os.getcwd(), path))

_get_module_path = lambda path: os.path.normpath(os.path.join(os.getcwd(), os.path.dirname(__file__), path))


def jieba_method(input):
    print(_get_abs_path(input))
    if os.path.isfile(_get_abs_path(input)):
        f = open(_get_abs_path(input), 'rb')
        content = f.read()
        tags = jieba.analyse.extract_tags(content, 20)
        f.close()
        return tags
    else:
        tags = jieba.analyse.extract_tags(input, 20)
        return tags

# main func
def keyword_extract(text: str, *method: int) -> list:
    '''
    :param text: a file directed to the inputs, or a text to analyze
    :param method: which method should this func use,
                    default(0) as jieba.analyse.extract_tags(), and
                    1 for LDA,
                    2 for RaKUn,
                    3 for TF-IDF without ca of jieba,
                    4 soooooon... :(
    :return: a list of keywords
    '''
    if len(method) == 0:
        return  jieba_method(text)

    if len(method) == 1:
        if method[0] == 0:
            # jieba method
            return jieba_method(text)
        elif method[0] == 1:
            # LDA
            return lda.keyword_extraction(text)
        elif method[0] == 2:
            # RaKUn method
            return ra.rakun(text, 'file')
        elif method[0] == 3:
            # TF-IDF
            return ti.tfidf_extract(text)
        else:
            print('2nd param should be 0~3')
            return

    else:
        print('there should be only 2 params')
        return

if __name__ == '__main__':
    text = '发票代开输入单位名称或者清单的时候，可以输入除汉字以外其他国家的文字吗？纳税人打开专票点击下一步提示：你提交的表格数据有误，请修改正确后提交，如何处理？发票代开缴纳税款后点击下一步提示：未查询到纳税人预收税款信息单张票面货物或应税劳务名称超过八行的情况,选择邮寄方式,是否能够收到发票?'

    print(keyword_extract(text, 0), end='\n\n')
    print(keyword_extract('testdoc.txt', 0), end='\n\n')
    print(keyword_extract('testdocLong.txt', 0), end='\n\n')

    # print(keyword_extract(text, 1), end='\n\n')
    # print(keyword_extract('testdoc.txt', 1),end='\n\n')
    # print(keyword_extract('testdocLong.txt', 1), end='\n\n')

    # print(keyword_extract(text, 2), end='\n\n')
    # print(keyword_extract('testdoc.txt', 2),end='\n\n')
    # print(keyword_extract('testdocLong.txt', 2), end='\n\n')
    print()
    # print(keyword_extract(text, 3), end='\n\n')
    # print(keyword_extract('testdoc.txt', 3), end='\n\n')
    # print(keyword_extract('testdocLong.txt', 3), end='\n\n')
