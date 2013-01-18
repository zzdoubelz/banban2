#!/usr/bin/env python
#[GCC 4.1.1  (Red Hat 4.1.1-43)] on linux2

import sys
from PySide.QtGui import *
from PySide.QtCore import *
from request import *
from book import *

class Form(QDialog):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)  
        self.initui()
        self.pageShows=5
        self.books=""
        self.currentStartIndex=0      
        self.currentPages=0    
        self.bookCount=0

    def doSearch(self,keyWord,start=0,count=5):
        if(keyWord==""):
            QMessageBox.information(self,"infomation",\
                    ("请输入查询字".decode('utf-8')),
                    QMessageBox.Ok)
            return 
        ss=bookSearch();
        print "search key :%s " % self.edit.text()
        print "search type %s" % self.sechCmbbox.currentIndex()

        books=ss.search(self.edit.text(),self.sechCmbbox.currentIndex(),start,count)
        self.bookCount=books['total']
        text="find %d books\n" % self.bookCount 
        text+="current page :%d \n"  % self.currentPages
        for item in books['book_arr']:
            s_author=""
            for author in item.author[0:-2]:
                s_author+=author+","
            if(len(item.author)>0):
                s_author+=item.author[-1]
            text+="%s\t %s \t %s \t%s\n" % (item.title,s_author,item.publisher,item.price)
            
        self.textarea.setText(text)
    def searchClick(self):
            self.currentPages=1
            self.currentStartIndex=0
            self.doSearch(self.edit.text(),self.currentStartIndex,self.pageShows)
    def nextClick(self):
            self.currentPages+=1
            self.currentStartIndex=(self.currentPages-1)*self.pageShows
            if(self.currentStartIndex<self.bookCount):
                self.doSearch(self.edit.text(),self.currentStartIndex,self.pageShows)
            if(self.currentStartIndex+self.pageShows>self.bookCount-1):
                self.nextBt.setEnabled(False)
            if(self.currentPages>1):
                self.prevBt.setEnabled(True)
    
    def pagrClick(self):
            if(self.currentPages>1):
                self.currentPages-=1
                self.currentStartIndex=(self.currentPages-1)*self.pageShows
                self.doSearch(self.edit.text(),self.currentStartIndex,self.pageShows)
                if(self.currentPages==1):
                    self.prevBt.setEnabled(False)
                if(self.currentStartIndex+self.pageShows<=self.bookCount-1):
                    self.nextBt.setEnabled(True)

            

    def initui(self):
            self.setWindowTitle("search book")
            self.srch_label=QLabel("搜索方式".decode('utf-8'))
            self.sechCmbbox=QComboBox()
            self.sechCmbbox.addItem("书名".decode('utf-8'),"name")
            self.edit=QLineEdit("enter book name here")
            self.searchButton=QPushButton("search")
            self.textarea=QTextEdit();
            self.nextBt=QPushButton("next")
            self.prevBt=QPushButton("previous")

            layout=QVBoxLayout()
            hlayout=QHBoxLayout()
            btnlayout=QHBoxLayout()
            btnlayout.addWidget(self.nextBt)
            btnlayout.addWidget(self.prevBt)

            hlayout.addWidget(self.srch_label)
            hlayout.addWidget(self.sechCmbbox)
            hlayout.addWidget(self.edit)
            hlayout.addWidget(self.searchButton)
            layout.addLayout(hlayout)
            layout.addWidget(self.textarea)
            layout.addLayout(btnlayout)
            self.setLayout(layout)
            self.searchButton.clicked.connect(self.searchClick)
            self.nextBt.clicked.connect(self.nextClick)
            self.prevBt.clicked.connect(self.pagrClick)
            self.edit.setFocus()
            self.resize(700,400)



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Form()
    form.show();
    sys.exit(app.exec_())


