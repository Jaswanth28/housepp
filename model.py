import pandas as pd
import numpy  as np
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import r2_score

train=pd.read_excel('train.xlsx')
test=pd.read_excel('test.xlsx')

def rrh():
    l=['Area','Price']
    for c in l:
        train[c] = train[c].str.extract(r'(\d+)').astype(float) 
        #this operation is used to split string and typecast into float data typr
        test[c] = test[c].str.extract(r'(\d+)').astype(float)
        train[c].fillna(value=0, inplace=True) 
        # its used to fill the Nan value into 0
        test[c].fillna(value=0, inplace=True)
        q1=train[train[c]==0].index 
        # used to find the index location of 0's
        q2=test[test[c]==0].index
        for k in q1:
            train.drop(index=k, inplace=True)
             # used to drop the 0's out of the dataset
        for k in q2:
            test.drop(index=k, inplace=True)

def trv():
    u=['Bedrooms','Furnishing','Tennants','Location','Bathrooms']
    for h in u:
        if h=='Location':
            train[h] = pd.to_numeric(train[h], errors='coerce')
             # strings are converted into numeric type
            train[h].fillna(value=0, inplace=True)
        test[h] = pd.to_numeric(test[h], errors='coerce') 
        # its used to fill the Nan value into 0
        test[h].fillna(value=0, inplace=True)
        p1=test[test[h]==0].index
        p2=train[train[h]==0].index
        for x in p1:
            test.drop(index=x, inplace=True)
            # used to drop the 0's out of the dataset
        for x2 in p2:
            train.drop(index=x2, inplace=True)
    rrh()

def preps():
    train.drop(columns=['Locality','Facing'],axis=1,inplace=True)
    test.drop(['Locality','Facing'],axis=1,inplace=True)
    o1=['Immediately','West']
    o2=['Family','Bachelors','Bachelors/Family']
    v1=[5,6]
    v2=[4,5,6]
    for j1 in o1:
        train['Bathrooms'].replace(to_replace=f'{j1}', value=int(f'{v1[o1.index(j1)]}'), inplace=True)  
         #this opertation is usedto replace the string data to nuerical data
    for j2 in o2:
        train['Tennants'].replace(to_replace=f'{j2}',value=int(f'{v2[o2.index(j2)]}'),inplace=True)
        test['Tennants'].replace(to_replace=f'{j2}',value=int(f'{v2[o2.index(j2)]}'),inplace=True)
    bedrooms=['1 BHK Apartment', '1 BHK Builder Floor','1 BHK Builder floor', '1 BHK Penthouse',
       '1 BHK Service Apartment', '1 bedroom Studio Apartment', '2 BHK Apartment',
       '2 BHK Builder Floor', '2 BHK Builderfloor', '2 BHK Penthouse',
       '2 BHK Service Apartment', '3 BHK Apartment', '3 BHK Builder Floor',
       '3 BHK Builderfloor', '3 BHK Service Apartment', '4 BHK Apartment',
       '4 BHK Builderfloor', '4 BHK Penthouse',
       '5 BHK Apartment', 'Studio Apartment'
       ] # this field is obtained by using unique function applies for all the three
    fur=['Furnished', 'Unfurnished', 'Semi-Furnished', 'Bachelors/Family','Family']
    loc=['Khairatabad', 'Miyapur', 'Dilshuknagar', 'Mehdipatnam',
       'Kondapur', 'Gachibowli', 'Nagole', 'Attapur', 'Manikonda',
       'Nizampet', 'Ameerpet', 'Marredpally', 'Madhapur', 'Shamirpet',
       'KPHB', 'Secunderabad', 'Begumpet', 'Patancheru', 'Rajendranagar',
       'Ghatkesar', 'Banjara Hills', 'Narsingi', 'Himayatnagar', 'Alwal',
       'Jubilee Hills', 'Boduppal', 'Punjagutta', 'LB Nagar',
       'Narayanguda', 'Kompally', 'Oldcity', 'Uppal', 'ECIL', 'Tarnaka',
       'Hayathnagar', 'Nallakunta', 'Hitech City', 'Masab Tank',
       'Vanasthalipuram', 'Hyderabad', 'Nampally', 'Bowenpally',
       'Sainikpuri', 'Habsiguda', 'Road #', 'Pocharam', 'Nacharam',
       'Malakpet', 'Golkonda', 'Phase', 'Mallapur','Shamshabad']
    for i in bedrooms:
       train['Bedrooms'].replace(to_replace=i, value=bedrooms.index(i), inplace=True) 
          #this operation is used to replace theabove value index values in this culmn data
       test['Bedrooms'].replace(to_replace=i, value=bedrooms.index(i), inplace=True)
    for i in fur:
        train['Furnishing'].replace(to_replace=i,value=fur.index(i), inplace=True)
        test['Furnishing'].replace(to_replace=i,value=fur.index(i), inplace=True)
    for i in loc:
       train['Location'].replace(to_replace=i,value=loc.index(i), inplace=True)
       test['Location'].replace(to_replace=i,value=loc.index(i), inplace=True)
    trv()
    
preps()

r1=BaggingRegressor()
X1=train[['Bedrooms', 'Bathrooms', 'Furnishing', 'Tennants', 'Area','Location']]
y1=train['Price']
r1.fit(X1,y1)

import pickle
with open('pred_pkl','wb') as f:
    pickle.dump(r1,f)
