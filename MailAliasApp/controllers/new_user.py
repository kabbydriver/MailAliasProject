from django.http import HttpResponse
from django.shortcuts import render
from MailAliasApp.models import User

def index(request):

	if request.method == 'POST':
		user = User.User(first_name="Kakoos", last_name="Swami")
		user.save()

	return render(request, "NewUserForm.html", {'form': User.NewUserForm()})
