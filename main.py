from PyQt5 import uic,QtWidgets,QtGui
import pandas as pd
from PyQt5.QtWidgets import * 
import sys
import pandas as pd
import numpy  as np
import pickle
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics._pairwise_distances_reduction import _datasets_pair
from sklearn.metrics._pairwise_distances_reduction import _middle_term_computer

with open('models/pred_pkl','rb') as f:
    model=pickle.load(f)

def tth(x1,x2,x3,x4,x5,x6):
    obs=[[x1,x2,x3,x4,x5,x6]]
    z=model.predict(obs)
    print(z)
    o=(f'Predicted House Price: {z[0]}')
    m.res.setText(o)

def ll():
    x1=m.bed.currentIndex()-1
    x2=m.bath.currentIndex()-1
    x3=m.fur.currentIndex()-1
    x4=m.tt.currentIndex()-1
    x5=m.area.text()
    x6=m.loc.currentIndex()-1
    s=[x1,x2,x3,x4,x6]
    c=0
    z=0
    for i in s :
        if i==-1:
            m.res.setText('enter valid values')
        else:
            c+=1
    if x5=='':
        m.res.setText('enter valid values')
    else:
        z=1
    if c==5 and z==1:
        m.res.clear()
        tth(x1,x2,x3,x4,x5,x6)

j=QtWidgets.QApplication([])
r=0
m=uic.loadUi('resources/ut1.ui')
m.show()
m.setWindowIcon(QtGui.QIcon('resources/pjkt.jpg'))
m.setWindowTitle('Home')
m.pred.clicked.connect(ll)
sys.exit(j.exec_())