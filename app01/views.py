from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def get_json(request):
    return render(request,'get_json.html')


def do_json(request):
    '''获取员工信息返回'''
    dict = {'name':'zhanyy','age':23,'sex':'男','salary':11000}
    return JsonResponse(dict)