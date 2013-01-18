#!/usr/bin/env python
#[GCC 4.1.1  (Red Hat 4.1.1-43)] on linux2

from PySide.QtGui import *
from PySide.QtCore import *

class Form(QDialog):
    def __init__(self,parent=None,bookitem):
        super(Form,self).__init__(parent)

