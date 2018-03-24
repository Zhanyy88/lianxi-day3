from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def get_json(request):
    return render(request,'get_json.html')


def do_json(request):
    '''获取员工信息返回'''
    dict = {'name':'zhanyy','age':23,'sex':'男','salary':11000}
    return JsonResponse(dict)


def set_cookie(request):
    ''' 保存cookie数据'''

    response = HttpResponse('保存cookie数据成功')

    # 保存cookie数据：（服务器会把cookie数据发送给浏览器保存）
    response.set_cookie('username','admin')
    response.set_cookie('good_id',(1,2,3,4,))
    return response


def get_cookie(request):
    '''获取cookie数据'''
    #读取cookie数据：（浏览器会自动上传该网站的cookie 数据）

    username = request.COOKIES['username']
    # username = request.COOKIES.get('username')
    id = request.COOKIES.get('good_id')

    info = 'username = %s   good_id = %s'%(username,id)
    return HttpResponse(info)


def set_session(request):
    '''保存Session数据'''

    # 保存session数据：默认会保存到数据库中，有效期为两周
    request.session['name'] = 'zhanyy'
    request.session['code'] = '666'

    return HttpResponse('保存session数据成功')


def get_session(request):
    '''读取session数据'''

    #读取session数据
    name = request.session.get('name')
    code = request.session.get('code')

    info = 'name =%s   ,code = %s'%(name,code)

    return HttpResponse(info)