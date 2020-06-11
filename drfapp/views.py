from django.shortcuts import render
from drfapp.models import Article

def get_article(request):
	queryset = Article.objects.all()
	context = {
	  "queryset":queryset
	}
	return render(request, 'home_page.html', context)
   
 


	# filter_backends = [SearchFilter]
	# search_fields = ['content', 'created_by__first_name']

	# def get_queryset(self, *args, **kwargs):
	# 	queryset  = Article.objects.all()
	# 	query  = self.request.GET.get('q')
	# 	if query:
	# 		queryset=queryset.filter(
 #                Q(content__icontains=query)
	# 			).distinct()

	# 	return queryset


	# def get_queryset(self):
	# 	return Article.objects.filter(created_by=self.request.user)

	
   
    # Filtering against the URL
	# def get_queryset(self):
	# 	username = self.kwargs['username']
	# 	return Article.objects.filter(created_by=username)
	#  