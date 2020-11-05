from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.urls import reverse

from django.db.utils import *

from app_blog.models import *

# Create your views here.
def auth(request):
	# return HttpResponse('hello world')
	return render(request, "auth.html", {})

def loginUser(request):
	form_email = request.POST.get("input_email")
	form_password = request.POST.get("input_password")

	try:
		user = User.objects.get(email=form_email)
	except User.DoesNotExist:
		return HttpResponse('user not exist with given email')

	db_password = user.password 

	if(db_password!=form_password):
		return HttpResponse('you enter wrong password')

	blog = Blog.objects.all()

	context = {'user': user, 'msg': 'account login successfully', 'all_blog': blog}

	request.session['USER_ID'] = user.id
	print('*session during login  ', request.session['USER_ID'])

	return render(request, 'index.html', context)

def signupUser(request):
	form_name = request.POST.get("input_name")
	form_email = request.POST.get("input_email")
	form_password = request.POST.get("input_password")

	try:
		user = User(name=form_name, email=form_email, password=form_password)
		user.save()
	except IntegrityError:
		return HttpResponse('use unique email address, there is user register with given email')

	blog = Blog.objects.all()

	context = {'user': user, 'msg': 'account created successfully', 'all_blog': blog}

	request.session['USER_ID'] = user.id

	return render(request, 'index.html', context)

def logoutUser(request):
	try:
		del request.session['USER_ID']
	except KeyError:
		return HttpResponse('you are not login')
	return render(request, 'auth.html', {})

def indexRedirect(request):
	print('*session during redirect  ', request.session['USER_ID'])
	try:
		user_id = request.session['USER_ID']
	except KeyError:
		return HttpResponse('you are not login')

	user = User.objects.get(id=user_id)

	blog = Blog.objects.all()

	context = {'user': user, 'msg': 'redirect to home page', 'all_blog': blog}

	return render(request, 'index.html', context)

def registerAsAuthor(request, arg_user_id):
	user = User.objects.get(id=arg_user_id)
	Author(user_id=user).save()
	user.role = 1
	user.save()

	blog = Blog.objects.all()

	context = {'user': user, 'msg': 'you became author successfully', 'all_blog': blog}

	return render(request, 'index.html', context)

def authorPanel(request, arg_user_id):
	# return HttpResponse(Author.objects.get(id=arg_author_id).user_id.name)
	print('*session authorpanel  ', request.session['USER_ID'])
	user = User.objects.get(id=arg_user_id)
	author = Author.objects.get(user_id = user)
	author_blogs = Author.objects.get(id = author.id).blog_points_to_author.all()

	category = Category

	context = {'author': author, 'all_blogs': author_blogs, 'blog_category': category}

	return render(request, 'author.html', context)

def blogDelete(request, arg_blog_id):
	blog = Blog.objects.get(id=arg_blog_id)
	author = blog.author_id	

	try:
		blog.delete()
	except:
		return HttpResponse('error in blogDelete view')
	
	return redirect(authorPanel, author.user_id.id)

def blogAdd(request):	
	form_author_id = int(request.POST.get("input_author_id"))
	form_title = request.POST.get("input_title")
	form_category = request.POST.get("input_category")	
	form_body = request.POST.get("input_body")

	author = Author.objects.get(id = form_author_id)

	try:
		# UPDATE
		form_blog_id = int(request.POST.get("input_blog_id"))
		# return HttpResponse(form_blog_id)	

		try:
			Blog(id=form_blog_id, author_id=author, category=form_category, title=form_title, body=form_body).save()
		except:
			return HttpResponse('error in blogAdd view update')	

		print('** update')
	except:
		# INSERT
		try:
			Blog(author_id=author, category=form_category, title=form_title, body=form_body).save()
		except:
			return HttpResponse('error in blogAdd view insert')	

		print('** insert')
	return redirect(authorPanel, author.user_id.id)