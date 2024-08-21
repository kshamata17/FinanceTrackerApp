from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'financetrackerapp/home.html')

def transaction_list(request):
    return render(request, 'financetrackerapp/transactions.html')
