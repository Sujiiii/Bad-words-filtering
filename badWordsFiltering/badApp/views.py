from django.shortcuts import render

# Create your views here.
# importing required packages
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from badApp import filter
# disabling csrf (cross site request forgery)
@csrf_exempt
def getResult(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    # if post request came
    if request.method == 'POST':
        # getting values from post
        string = request.POST.get('string')
        response = filter.process_string(string)
        print(response)
        return render(request, 'response.html', {"r": response})
