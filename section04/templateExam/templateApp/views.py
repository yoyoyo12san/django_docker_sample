from django.shortcuts import render

# Create your views here.


class Member:
    def __init__(self, id, name, pic, join):
        self.id = id
        self.name = name
        self.pic = pic
        self.join = join

members_list = [
        Member(0, 'Taro', 'img/pic11.jpg', '2016/09/07'),
        Member(1, 'Jiro', 'img/pic12.jpg', '2017/04/18'),
        Member(2, 'Hanako', 'img/pic13.jpg', '2018/12/20')
    ]

def home(request):
    return render(request, 'home.html', context={
        'members': members_list
    })

def members(request):
    return render(request, 'members.html', context={
        'members': members_list
    })

def member(request, id):
    return render(request, 'member.html', context={
        'member':members_list[id]
    })