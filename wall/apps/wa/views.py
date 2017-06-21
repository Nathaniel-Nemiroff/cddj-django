# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from models import users, messages, comments

import re#,bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

# Create your views here.
def index(request):
	usrmsg = messages.objects.all()#mysql.query_db("select * from users join messages on messages.user_id = ursers.id")
	msg = ''
	if('regmsg' in request.session):
		msg=request.session['regmsg']

	if usrmsg:
		print '------------------------------------'
		print usrmsg[0]
		print '------------------------------------'

	context={
		'message':msg,
		'user_messages':usrmsg
	}
	return render(request, 'index.html', context)

def wall(request):
	usrmsg=messages.objects.all()#mysql.query_db("select * from users join messages on messages.user_id = users.id")
	msg = ''
	if('regmsg' in request.session):
		msg=request.session['regmsg']

	for message in usrmsg:
		message.commentlist=comments.objects.filter(message_id=message)
		#mysql.query_db("select * from comments join users on users.id = comments.user_id where message_id = "+str(message['id']))

	print '------------------------------------'
	print usrmsg
	print '------------------------------------'

	context = {'message':msg,'user_messages':usrmsg}

	return render(request, 'index.html', context)

def newmsg(request):
	if request.POST['newmsg'] and 'id' in request.session:
		mssg = messages.objects.create(user_id=users.objects.filter(id=request.session['id'])[0],message=request.POST['newmsg'])
		#mysql.query_db('insert into messages (user_id, message, created_at, updated_at) values ('+str(request.session['id'])+',"'+request.POST['newmsg']+'", NOW(), NOW())')
	return redirect('/')

def newcmnt(request):
	if request.POST['newcmnt'] and 'id' in request.session:
		cmt = comments.objects.create(message_id=messages.objects.filter(id=request.POST['msgnum'])[0], user_id=users.objects.filter(id=request.session['id'])[0], comment=request.POST['newcmnt'])
		#mysql.query_db('insert into comments (message_id, user_id, comment, created_at, updated_at) values ('+request.POST['msgnum']+','+str(request.session['id'])+',"'+request.POST['newcmnt']+'", NOW(), NOW())')
	return redirect('/wall')

def register(request):
	if request.method=='POST':
		flash=''
		first=request.POST['first']
		last=request.POST['last']
		mail=request.POST['email']
		pswd=request.POST['pswd']
		conf=request.POST['conf']

		check=True
		if(len(first)<2 or len(last)<2):
			check=False
			flash+='Names must be more than one character long!\n'
		if( not NAME_REGEX.match(first) or not NAME_REGEX.match(last)):
			check=False
			flash+='Name must contain only alphabetic characters!\n'
		if(not EMAIL_REGEX.match(mail)):
			check=False
			flash+='Email is not valid!\n'
		if(len(pswd)<8):
			check=False
			flash+='Password must be at least 8 characters!\n'
		if(not pswd == conf):
			check=False
			flash+='Passwords must be the same!\n'

		context = {'messages':flash}

		if(check):
			#hashsalt=bcrypt.gensalt()
			#hashpass = bcrypt.hashpw(pswd.encode('UTF_8'), hashsalt)
			#mysql.query_db("insert into users (first_name, last_name, email, password, salt, created_at, updated_at) values('"+first+"','"+last+"','"+email+"','"+hashpass+"','"+hashsalt+"',NOW(), NOW())")
			usr = users.objects.create(first_name=first,last_name=last, email=mail, password=pswd)
			request.session['regmsg']='Welcome '+usr.first_name+' '+usr.last_name
			request.session['id']=usr.id
			return redirect('/wall')
		else:
			return render(request, 'register.html',context)
	else:
		return render(request, 'register.html')


def login(request):
	if request.POST:
	
		passchk = users.objects.filter(email=request.POST['email'])#mysql.query_db("select * from users where email = '"+request.POST['email']+"'")
		context = { 'messages':'' }

		if not passchk:
			context['messages'] = 'Username or password incorrect!'
			return render(request, 'login.html')
		#hashch=bcrypt.hashpw(request.POST['pswd'].encode('UTF_8'),passchk[0]['salt'].encode('UTF_8'))

		print '------------------------------------'
		print passchk[0].email
		print '------------------------------------'

		if request.POST['pswd'] == passchk[0].password:
			request.session['regmsg']='Welcome '+passchk[0].first_name+' '+passchk[0].last_name
			request.session['id']=passchk[0].id
			return redirect('/wall')
		else:
			context['messages']='Username or password incorrect!'
			return render(request, 'login.html',context)
	return render(request, 'login.html')

def logout(request):
	request.session.pop('regmsg')
	request.session.pop('id')
	return redirect('/')
