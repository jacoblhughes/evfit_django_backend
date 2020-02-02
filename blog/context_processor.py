from blog.models import BlogPost

def recent_five(request):
    context = BlogPost.objects.filter(status=1).order_by('-created_on')
    return {'recent_five': context}