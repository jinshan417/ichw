
#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Peng Jinshan"
__pkuid__  = "1600012182"
__email__  = "jinshan@pku.edu.cn"
"""

import sys
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

  q.lower()
  newstr=q.split()
  pure=set(newstr)
  '''we get the words in the passage'''

  dic={}
  for item in pure:

      number=newstr.count(i)
      dic[i]=number

  lis=list(dic.values())
  lis.sort(reverse=True)
  for i in lis[:topn]:
     print(list(dic.keys)[lis(dic.values()).index(i)].ljust(10)+str(i))
    # your code goes here



  pass

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
print(wcount(' http://www.gutenberg.org/cache/epub/19033/pg19033.txt 20',10 ))
