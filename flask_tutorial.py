# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 19:21:29 2020

@author: Anand Jebakumar
"""

from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
from shutil import copyfile

def cropImage(inp):
    print('entering crop subroutine')
    src = './static/inputImage.png'
    dst = './static/outputImage.png'
    # clear existing input and output files if any
    if os.path.isfile(src):
        os.remove(src)
        print('removed src')
    if os.path.isfile(dst):
        os.remove(dst)
        print('removed dst')
    # this just saves the input image and copies it to the output
    # rewrite this so the output is cropped
    inp.save(src)
    copyfile(src, dst) 
    
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('image_cropper.html')

@app.route('/',methods=['POST'])
def getFile():
    if request.method == 'POST':
        result = request.form
        try:
            cropRatio = float(request.form['cropRatio'])
            print(cropRatio)
        except ValueError:
            print('Error: enter numerical value')
            cropRatio = 1.0
        inputImage = request.files['file']
        cropImage(inputImage)
    return render_template('image_cropper.html', num=cropRatio)

if __name__ == '__main__':
   app.run()
'''
<form action="http://localhost:5000/" method="post" enctype = "multipart/form-data">
'''