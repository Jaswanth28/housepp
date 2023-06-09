from PyQt5 import uic,QtWidgets,QtGui
import pandas as pd
from PyQt5.QtWidgets import * 
import sys
import pandas as pd
import numpy  as np
import pickle
import git
import os
import shutil
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics._pairwise_distances_reduction import _datasets_pair
from sklearn.metrics._pairwise_distances_reduction import _middle_term_computer

repo_url = "https://github.com/jaswanth28/models"
repo_name = "models"

if os.path.isdir(repo_name):
    print(f"Repository '{repo_name}' already exists")
else:
    print(f"Cloning repository '{repo_name}'...")
    git.Repo.clone_from(repo_url, repo_name)
    print(f"Repository '{repo_name}' cloned successfully")

def update_local_files_if_changed(repo_path="models"):
    repo = git.Repo(repo_path)
    repo.remotes.origin.fetch()
    remote_commit = repo.git.rev_parse("origin/master")
    try:
        with open(os.path.join(repo_path, ".git", "refs", "heads", "master"), "r") as f:
            local_commit = f.read().strip()
    except FileNotFoundError:
        local_commit = ""

    if remote_commit != local_commit:
        print("Updating local files with changes from Git repository...")
        repo.git.reset("--hard", "origin/master")
        print("Local files updated successfully.")
    else:
        print("Local files are up-to-date with the Git repository.")


def update():
    update_local_files_if_changed()

with open('models/pred_pkl','rb') as f:
    model=pickle.load(f)

def tth(x1,x2,x3,x4,x5,x6):
    obs=[[x1,x2,x3,x4,int(x5),x6]]
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
m.upd.clicked.connect(update)
sys.exit(j.exec_())