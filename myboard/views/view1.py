from django.shortcuts import render


def Main(request):
    ss = "<div><b style='text-size:24pt'>메인화면</b></div>"
    return render(request, 'main.html', {'head':ss})