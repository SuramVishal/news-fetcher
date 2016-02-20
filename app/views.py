from __future__ import print_function
from AlchemyAPI.alchemyapi import AlchemyAPI
from datetime import datetime
from threading import Timer
import requests
import threading
import time

from flask import render_template, flash, redirect,request,url_for
from app import app
from .forms import LoginForm

import json


@app.route('/index')
@app.route('/execute',methods=['GET','POST'])
def execute1():
	formdata=request.form['openid']
        keys=formdata.split(',');
        inp=open('feeds.db','r');
	des=""
        arr=""
	for line in inp:
		if "-|" not in line:
			des=des+line+"~^";
		else:
                        flag=0;
			for i in range(0,len(keys)):
				if( keys[i] in des.lower()):
					flag=1;


			if flag==1:
				alchemyapi = AlchemyAPI()
				response = alchemyapi.keywords('text','s', {'sentiment':1})

				if response['status'] == 'OK':
		                        senticount=0;
					for keyword in response['keywords']:
						if keyword['sentiment']['type']<0:
		                                   senticount=senticount+1
		                        if senticount<5:
		                           arr=arr+"~^---------------------------~^"+des
					
				else:
					arr=arr+"Error in keyword extaction call: ', response['statusInfo']"
		
			des=""			   
			
			 


    # formdata=request.args['formdata']
    #title='yolo'
    #descrip='descrip'
    #timestamp='29 Feb'
    #models.insert_article(title,descrip,timestamp)
    #results=models.select_all()
        data=arr.split('~^')
        return render_template('print.html',title='Print Output',data=data)
@app.route('/')
@app.route('/takeinput', methods=['GET', 'POST'])
def login():
    form = LoginForm()
   # if form.validate_on_submit(): 
     #  formdata=form.data
    #  urlx=flash.url_for('execute1',formdata=formdata)
    #   return redirect(url_for('/execute',formdata=formdata))
      # return render_template('print.html',title='Print',form=form)
    return render_template('login.html',
                           title='Keyword Entry',
                           form=form)
