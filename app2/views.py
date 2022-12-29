from django.shortcuts import render

# Create your views here.
def jinja_print2(request):
     g={'name':'python','phno':7337377537}


     return render(request,'jinja_print2.html',context=g)