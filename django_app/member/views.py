from django.contrib.auth import authenticate, login, logout as django_logout
from django.http import HttpResponse
from django.shortcuts import render, redirect


def login_check(request):
    # memberlogin.html 생성
    #   username, password, button이 있는 HTML 생성
    #   POST요청이 올 경우 좌측 코드를 기반으로 로그인 완료 후 post_list로 이동
    #   실패할 경우 HttpResponse로 'Login invalid' 띄워주기

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('post:post_list')
        else:
            HttpResponse('Login invalid')

    else:
        if request.user.is_authenticated:
            return redirect('post:post_list')
        return render(request, 'member/login.html')

def logout(request):
    django_logout(request)
    return redirect('post:post_list')