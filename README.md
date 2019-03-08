This project basically filters the swear words by appending '*' at the respected position

This project is built on top of django.

**Some main parts to note**

**filter.py**

```python

import os

def process_string(string,):
    result = ""
    str_list = string.split()
    strn_list = [i.lower() for i in str_list]

    with open(os.path.dirname(__file__)+'/badwords.txt','r') as file:
        for word in file:
           word = word.split(', ')

    for i in strn_list:
        if i in word:
            result += '*'*len(i)+" "
        else:
             result+=i+" "
    return result
```

**views.py**

```python

from django.shortcuts import render
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from badApp import filter

@csrf_exempt
def getResult(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    if request.method == 'POST':
        # getting values from post
        string = request.POST.get('string')
        response = filter.process_string(string)
        print(response)
        return render(request, 'response.html', {"r": response})
        
```

**urls.py**

```python

from django.contrib import admin
from django.urls import path
from badApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.getResult)
]
```
