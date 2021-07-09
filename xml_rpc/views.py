from django.shortcuts import render


def index(request):
    xml=[
        {'title':'first xml'},
        {'title':'second xml'}
    ]
    return render(request,'xml_rpc/index.html' ,{
        'xml': xml
    })