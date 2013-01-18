#!/usr/bin/env python
#[GCC 4.1.1  (Red Hat 4.1.1-43)] on linux2

import httplib,urllib
import sys
import json
from book import book


class searchBook:
    def __init__(self):
        pass
    def search(self,keyWord,atype,start,count):
        print "search key :%s " % keyWord
        print "atype :%d:" % atype
        if(atype==0):
            stype='q'
        elif(atype==1):
            stype='tag'
        else:
            print "atype error"
            return  []
        params=urllib.urlencode({stype:keyWord.encode('utf-8'),'start':start,'count':count})
        conn=httplib.HTTPConnection("api.douban.com")
        print params
        conn.request("GET","/v2/book/search?%s" % params)
        r1=conn.getresponse()
        print r1.status
        data=r1.read()
        f=open("data.txt","w")
        f.write(data)
        js=json.loads(data)
        jsbooks=js['books']

        books={}
        books['count']=js['count']
        books['start']=js['start']
        books['total']=js['total']
        books['Shuxin']=[];
        for item in jsbooks:
            mbook=book()
            mbook.load(item)
            books['Shuxin'].append(mbook)
        return books
           # print "************************************************\n\n\n"


if __name__=='__main__':
    argc=len(sys.argv)
    if(argc<2):
        print "usage %s  keyworkd start count " % sys.argv[0]
        exit(0)
    start=0;
    count=5;
    if(argc==3):
        start=sys.argv[2]
    if(argc==4):
        count=sys.argv[3]
    ss=searchBook()
    ss.search(sys.argv[1],start,count)





