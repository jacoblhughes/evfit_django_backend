from accounts.models import Profile

def profile_information(request):
    context = Profile.objects.all().order_by('-id')
    return {'profile_information': context}