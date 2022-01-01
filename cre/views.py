from django.shortcuts import render,redirect
from django.views.generic import ListView , DetailView ,View
from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from django.contrib.auth.models import Group 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


from .models import *
from .forms import *
from .services import *

class HomeScreen(ListView):

	model = Article
	paginate_by = 4
     
	context_object_name = 'object_list'

	def get_context_data(self,*args, **kwargs):

		context = super().get_context_data(**kwargs)
		cat = Category.objects.all()
		data = Article.objects.all()[:4]
		# filter out media from db
		music = Article.objects.filter(cat__title='Music')
		trend = Article.objects.filter(cat__title='Music')[:7]
		videos = Article.objects.filter(cat__title='Videos')
		news = Article.objects.filter(cat__title='News')

		context['news'] = news
		context["vid"] = videos 
		context['music'] = music
		context['trend'] = trend
		context["cat"] = cat
		context['data'] = data
		return context

class postDetails(DetailView):
	model = Article
	form_class = CommentForm
	

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		comments = self.get_object().comments.filter(active=True)
		frm =  self.form_class()
		new = Article.objects.all()[:10]
		cat = Category.objects.all()
		post  = Article.objects.all()
		related_query = ''

		ref = []

		title = self.get_object().title

		# if title:
		# 	related_query = post.filter(
		# 		Q(title__icontains=title)|
		# 		Q(intro__icontains=title)
		# 	) 
		data = title.split(' ')

		obj = self.get_object().id

		print('entry --->',obj)
		for i in data:
			if i != '-':
				# print(str(i))
				related_query = post.filter( Q(title__icontains=i) )
				ref.append(related_query)

		print('test --->',related_query)
				
		
		context['r_post'] = ref
		
		context["cat"] = cat
		context["frm"] = frm 
		context["comments"] = comments 
		context["new"] = new
		return context

	
	def post(self, request,pk, *args, **kwargs ):
		form = self.form_class(request.POST,request.FILES)
		
		if form.is_valid():
			instance = form.save(commit=False)
			instance.post = Article.objects.get(pk=pk)
			instance.save()		
			return redirect(self.get_object().get_absolute_url())
		return render(request,self.template_name,{'form':form})
	

class MusicScreen(ListView):
	model = Article
	paginate_by = 4

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		cat = Category.objects.all()
		music = Article.objects.filter(cat__title='Music')
		news = Article.objects.filter(cat__title='News')
		mov = Article.objects.filter(cat__title='Movies')

		context["feat"] = mov 
		context['news'] = news
		context["cat"] = cat
		context["post"] = music 
		return context 
	

class VideoScreen(ListView):
	model = Article

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		cat = Category.objects.all()
		videos = Article.objects.filter(cat__title='Videos')
		mov = Article.objects.filter(cat__title='Movies')
		news = Article.objects.filter(cat__title='News')

		context['news'] = news
		context["feat"] = mov
		context["post"] = videos 
		context["cat"] = cat
		return context 
	

class SerrieScreen(ListView):
	model = Article

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		cat = Category.objects.all()
		serrie = Article.objects.filter(cat__title='Movie Serries')
		mov = Article.objects.filter(cat__title='Movies')
		news = Article.objects.filter(cat__title='News')

		context['news'] = news
		context["feat"] = mov
		context["cat"] = cat
		context["post"] = serrie 
		return context 
	

class MovieScreen(ListView):
	model = Article

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		cat = Category.objects.all()
		movies = Article.objects.filter(cat__title='Movies')
		vid = Article.objects.filter(cat__title='Videos')
		news = Article.objects.filter(cat__title='News')

		context['news'] = news
		context["feat"] = vid
		context["cat"] = cat
		context["post"] = movies 
		return context 


class AddPostScreen(CreateView):
	model = Article
	form_class = PostForm
	template_name = "post/post-forms.html"
	
	def get(self, request, *args, **kwargs ):
		cat = Category.objects.all()
		form = self.form_class()
		context = {
			"form": form,
			'cat':cat,
		}
		return render(request,self.template_name,context)

	# def post(self, request, *args, **kwargs ):
	# 	form = self.form_class(request.POST,request.FILES)


	# 	if form.is_valid():
	# 		instance = form.save(commit=false)
			# instance.author = request.user.


class SearchScreen(ListView):
	model = Article
	template_name = 'post/search.html'


	def get(self,request, *args, **kwargs):
			query = request.GET.get('q')
			post_obj = ''
			#retrieve published queries from db 
			post = Article.objects.filter(active=True)
			cat = Category.objects.all()
			news = Article.objects.all()[:10]

			#filter the search filds
			if query:
				post_obj = post.filter(
					Q(title__icontains=query)|
					Q(intro__icontains=query)|
					Q(body__icontains=query)
					)
		
			context = {
				'query': query,
				'post_obj' : post_obj,
				'cat':cat,
				'news': news
				}
			return render(request, self.template_name, context) 