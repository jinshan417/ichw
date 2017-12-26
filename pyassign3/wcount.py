
#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Peng Jinshan"
__pkuid__  = "1600012182"
__email__  = "jinshan@pku.edu.cn"
"""
from urllib.request import urlopen

def wcount(lines, topn=10):


  doc = urlopen(lines)
  docstr = doc.read()
  doc.close()
  jstr = docstr.decode()

  s=jstr.replace(',',' ')
  b=s.replace('.',' ')
  c=b.replace('?',' ')
  d=c.replace('_',' ')
  e=d.replace(']',' ')
  f=e.replace('[',' ')
  g=f.replace('*',' ')
  h=g.replace('%',' ')
  i=h.replace('!',' ')
  j=i.replace('"',' ')
  k=j.replace(':',' ')
  l=k.replace(';',' ')
  m=l.replace('(',' ')
  n=m.replace(')',' ')
  o=n.replace('-',' ')
  p=o.replace('_',' ')
  q=p.replace('/',' ' )
  x=q.replace('/',  ' ')

  x=x.lower()
  newstr=x.split()
  pure=set(newstr)
  print(newstr)
  '''we get the words in the passage'''

  dic={}
  for item in pure:
      number=newstr.count(i)
      dic[i]=number
  print(dic)
  lis=list(dic.values())
  lis.sort(reverse=True)
  for i in lis[:topn]:
     result=list(dic.keys)[lis(dic.values()).index(i)].ljust(10)+str(i)
     return result


