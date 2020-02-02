from accounts.models import Profile

def profile_information(request):
    context = Profile.objects.all()
    return {'profile_information': context}