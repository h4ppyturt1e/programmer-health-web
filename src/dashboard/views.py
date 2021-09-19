from django.shortcuts import render
from dashboard.models import UserData

# Create your views here.

def dashboard(request):
    context = {}
    context['user_data'] = UserData.objects.filter(user=request.user).first()
    return render(request, 'dashboard/temp_dash.html', context)




