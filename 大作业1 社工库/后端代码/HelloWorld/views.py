# from django.http import HttpResponse
#
#
# def hello(request):
#     return HttpResponse("Hello world!")

from django.shortcuts import render
from django.http import JsonResponse
from fastapi import FastAPI,Response
from fastapi.responses import JSONResponse
import json


def runoob(request):
    import datetime
    context = {}
    context['hello'] = 'Hello World!'
    context['name'] = 'IceWire, my load!'
    context['quantity'] = 12345
    context['time'] = datetime.datetime.now()
    context['skip'] = "<a href='https://www.runoob.com/'>点击跳转</a>"
    context['num'] = 99
    context['views_list'] = ['index1','index2']
    return render(request, 'runoob.html', context)

def showData(request):
    import HelloWorld.Mssql_connect as MS
    con = MS.MssqlController()
    con.ConnectMssql(17, '127.0.0.1', 'GroupData1', 'SA', '3140224')
    dbname = request.GET.get("dbname")
    key = request.GET.get("key")
    sql = ""
    if dbname == "qqq":
        sql = "select top 100 * from qqq where QQNum like '%"+ key +"%' or Nick like '%"+ key +"%' or QunNum like '%"+ key +"%';"
    else:
        sql = "select top 100 * from list where Title like '%"+ key +"%' or QunNum like '%"+ key +"%';"
    datalist = con.Select(sql)
    jsondata = MS.DataToJson(datalist, dbname)
    # headers = {"Access-Control-Allow-Origin" : "*"}
    # content = {'data' : jsondata}
    response = JsonResponse({'data' : jsondata})
    response["Access-Control-Allow-Origin"] = "*"
    return response

