from accounts.models import Profile
from accounts.models import NewProspect

def profile_information(request):
    context = Profile.objects.all()
    return {'profile_information': context}

def new_prospects(request):
    context = NewProspect.objects.all()[:5]
    return {'new_prospects': context}