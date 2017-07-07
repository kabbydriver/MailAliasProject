from django.http import HttpResponse
from django.shortcuts import render
from MailAliasApp.models import User

def index(request):

	if request.method == 'POST':
		user = User.User(first_name=request.POST['first_name'], last_name=request.POST['last_name'])
		print user

	return render(request, "NewUserForm.html", {'form': User.NewUserForm()})
