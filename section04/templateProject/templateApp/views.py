from django.shortcuts import render

# Create your views here.
def index(request):
    val = 'Hello'
    return render(request, 'index.html', context={'value' : 'Hello'})

def home(request, f_name, l_name):
    my_name = 'Taro'
    your_name = f'{f_name} {l_name}'

    favourite_fruits = ['Apple', 'Grape']
    my_info = {
        'name' : 'Taro',
        'age' : 18
    }
    status = 20
    return render(request, 'home.html', context={
        'name':my_name,
        'your_name':your_name,
        'ff':favourite_fruits,
        'info':my_info,
        'status':status
    })

# def mypage(request):
#     return render(request, 'base.html')

def sample1(request):
    return render(request, 'sample1.html')

def sample2(request):
    return render(request, 'sample2.html')

def sample(request):
    name = 'ichiro'
    height = 177.5
    weight = 73
    bmi = weight / (height / 100) ** 2
    page_url = 'ホームページ: https://www.google.com'
    favourite_fruits = [
        'Apple', 'Grape', 'Lemon'
    ]
    msg1 = """hello
    my name is
    ichiro
    """
    msg2 = '1234567890'
    return render(request, 'sample.html', context={
        'name': name,
        'bmi': bmi,
        'page_url': page_url,
        'ff': favourite_fruits,
        'msg1': msg1,
        'msg2': msg2
    })

class Country:

    def __init__(self, name, population, capital):
        self.name = name
        self.population = population
        self.capital = capital


def sample3(request):
    country = Country('Japan', 10000000, 'Tokyo')
    return render(request, 'sample3.html', context={
        'country':country
    })