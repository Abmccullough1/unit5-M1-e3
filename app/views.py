from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
# Create your views here.

def near_hundred(request: HttpRequest,num: int) -> HttpResponse:
    if (abs(num-100) <=10 or abs(num-200) <=10):
        return HttpResponse(True)
    else:
        return HttpResponse(False)
    
def string_splosion(request: HttpRequest,word: str)->HttpResponse:
    result = ''
    for i in range(len(word)):
        result += word[:i+1]
    return HttpResponse(result)

def cat_dog(request:HttpRequest, cd: str) -> HttpResponse:
   count1 = 0
   count2 = 0 

   if 'dog' and 'cat' not in cd:
        return True
   for i in range(len(cd)-1):
        if cd[i:i+3] == 'cat':
            count1 += 1
        if cd[i:i+3] == 'dog':
            count2 += 1
   if count1 == count2:
        return HttpResponse(True)
   else:
        return HttpResponse(False)
   
def lone_sum(request: HttpRequest,a: int, b: int, c: int) ->HttpResponse:
     if a == b and b == c:
        return HttpResponse(0)
     elif a == b:
        return HttpResponse(c)
     elif b == c:
        return HttpResponse(a)
     elif c == a:
        return HttpResponse(b)
     else:
         return HttpResponse(a + b + c)