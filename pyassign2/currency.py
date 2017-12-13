"""currency.py: Return amount of currency received in the given exchange..

__author__ = "zhanzhaohuang"
__pkuid__  = "1700011730"
__email__  = "1700011730@pku.edu.cn"
"""
from urllib.request import urlopen
import random

def before_space(s):
    """Return substring of s; up to, but not including, the first space 
    """
    if ' ' in s:
        n=s.index(' ')
        text1=s[:n]
        return text1
    else:
        return None

def after_space(s):
    """Return Substring of s after the first space 
    """
    if ' ' in s:
        n=s.index(' ')
        text1=s[n+1:]
        return text1
    else:
        return None

def first_inside_quotes(s):
    """Return The first substring of s between two (double) quote characters 
    """
    q="'" and '"'
    n1=s.index(q)
    text=s[n1+1:]
    n2=text.index(q)
    text1=text[:n2]
    return text1

def get_from(s):
    """Return The FROM value in the response to a currency query. 
    """
    q=s.index('from')
    s=s[q+5:]
    p=s.index(':')
    s=s[p+1:]
    text=first_inside_quotes(s)
    return text

def get_to(s):
    """Return The TO value in the response to a currency query. 
    """
    q=s.index('to')
    s=s[q+3:]
    p=s.index(':')
    s=s[p+1:]
    text=first_inside_quotes(s)
    return text

def has_error(s):
    """Return True if the query has an error; False otherwise. 
    """
    if get_to(s)=="" and get_from(s)=="":
        return True

def currency_response(x,y,z):
    """Return a JSON string that is a response to a currency query.
    """
    n='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+x+'&to='+y+'&amt='+z
    doc = urlopen(n)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr

def iscurrency(y):
    """Return True if currency is a valid (3 letter code for a) currency. It returns False otherwise.
    """
    x='USD'
    z='2.5'
    n=currency_response(x,y,z)
    if has_error(n) != True:
        return True
    else:
        return False

def exchange(currency_from,currency_to,amount_from):
    """Return amount of currency received in the given exchange.
    """
    jstr=currency_response(currency_from,currency_to,amount_from)
    amount_to=float(before_space(get_to(jstr)))
    return amount_to

def main():
    currency_from=input()
    currency_to=input()
    amount_from=input()
    if iscurrency(currency_from)==True and iscurrency(currency_to)==True:
        amount_to=exchange(currency_from,currency_to,amount_from)
        print(amount_to)

if __name__ == '__main__':
    main()

def test_before_space():
    text1='hello  world'
    text2=' hello world'
    text3='helloworld'
    n=0
    if before_space(text1) == 'hello':
        n=n+1
    if before_space(text2) == '':
        n=n+1
    if before_space(text3) == None:
        n=n+1
    if n!=3:
        return False

def test_after_space():
    text1='hello  world'
    text2=' hello world'
    text3='helloworld'
    n=0
    if after_space(text1) == ' world':
        n=n+1
    if after_space(text2) == 'hello world':
        n=n+1
    if after_space(text3) == None:
        n=n+1
    if n!=3:
        return False

def test_first_inside_quotes():
    text1='hello "world"'
    text2='"hello" "world"'
    text3='""hello world'
    n=0
    if first_inside_quotes(text1) == 'world':
        n=n+1
    if first_inside_quotes(text2) == 'hello':
        n=n+1
    if first_inside_quotes(text3) == '':
        n=n+1
    if n != 3:
        return False

def test_get_from():
    text1='{ "from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" }'
    text2='{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }'
    n=0
    if get_from(text1) == '2.5 United States Dollars':
        n=n+1
    if get_from(text2) == '':
        n=n+1
    if n != 2:
        return False

def test_get_to():
    text1='{ "from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" }'
    text2='{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }'
    n=0
    if get_to(text1) == '2.0952375 Euros':
        n=n+1
    if get_to(text2) == '':
        n=n+1
    if n != 2:
        return False

def test_has_error():
    text1='{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }'
    text2='{ "from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" }'
    n=0
    if has_error(text1) == True:
        n=n+1
    if has_error(text2) == None:
        n=n+1
    if n != 2:
        return False

def test_currency_response():
    x1='USD'
    x2='usd'
    y1='EUR'
    y2='eur'
    z1='2.5'
    z2='aba'
    text1='{ "from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" }'
    text2='{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }'
    text3='{ "from" : "", "to" : "", "success" : false, "error" : "Exchange currency code is invalid." }'
    text4='{ "from" : "", "to" : "", "success" : false, "error" : "Currency amount is invalid." }'
    n=0
    if currency_response(x1,y1,z1) == text1:
        n=n+1
    if currency_response(x2,y1,z1) == text2:
        n=n+1
    if currency_response(x1,y2,z1) == text3:
        n=n+1
    if currency_response(x1,y1,z2) == text4:
        n=n+1
    if currency_response(x2,y2,z1) == text2:
        n=n+1
    if n !=5:
        return False

def test_iscurrency():
    list1=['AED','LKR','AFN','LRD','ALL','LSL','AMD','ANG','BHD','COP']
    n=random.randrange(0,10)
    if iscurrency(list1[n]) != True:
        return False
    
def test_all():
    n=0
    text1='Module a1 passed all tests'
    if test_before_space() != False:
        n=n+1
    if test_after_space() != False:
        n=n+1
    if test_first_inside_quotes() != False:
        n=n+1
    if test_get_from() != False:
        n=n+1
    if test_get_to() != False:
        n=n+1
    if test_has_error != False:
        n=n+1
    if test_currency_response() != False:
        n=n+1
    if test_iscurrency() != False:
        n=n+1
    if n==8:
        return text1
print(test_all())

