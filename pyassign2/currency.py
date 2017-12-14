from urllib.request import urlopen

'''获取字符串函数
引用自作业说明
将URL请求转换成正常的字符串'''
def newstr(link):
    doc = urlopen(link)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode()
    return jstr


'''货币数目分离函数
彭金山
从字符串中获取所兑换货币的数量，并转化为浮点数'''
def answer(newstr):
    money=newstr.split()
    eur=money[9][1:]
    eur1=float(eur)
    return eur1


'''货币转化函数
彭金山
输入两种货币名称以及数量（用空格隔开），输出目标货币的兑换数量'''
def exchange(currency_from,currency_to,amount_from):
    a=str(currency_from)
    b=str(currency_to)
    c=str(amount_from)
    ori=' http://cs1110.cs.cornell.edu/2016fa/a1server.php? '
    new=' http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+a+'&to='\
        +b+'&amt='+c
    sen=newstr(new)
    eur1=answer(sen)
    return eur1

#输入输出举例
currency_from,currency_to,amount_from=input().split()
print(exchange(currency_from,currency_to,amount_from))

'''测试函数1
彭金山
测试字符串转换函数'''
def a1():
    assert '{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }'==\
       newstr(' http://cs1110.cs.cornell.edu/2016fa/a1server.php? ')


'''测试函数2
彭金山
测试货币数目分离函数'''
def a2():
    assert 8.38095==answer('{ "from" : "10 United States Dollars", "to" : "8.38095 Euros", "success" : true, "error" : "" }')


'''测试函数3
彭金山
测试最终输出结果'''
def a3():
    assert 8.38095==exchange('USD','EUR',10)

'''测试函数完全版
彭金山
测试所有的测试函数'''
def testall():
    a1()
    a2()
    a3()
    print("All tests passed")


