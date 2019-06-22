from django.shortcuts import render, reverse
from django.http import HttpResponse, JsonResponse
from .models import *
import json
# Create your views here.


def area(request):
    areas0 = Area.objects.get(pk=5)
    areas = Area.objects.filter(parrent_area__isnull=False).filter(pk__in=[1,2,3,4])
    # areas = Area.objects.filter(parrent_area__isnull=False)

    result = reverse('mytest:area')
    print(result)

    cookie = request.COOKIES
    print(dir(cookie))
    if 'name' in cookie.keys():
        print(request.COOKIES['name'])
        return render(request, 'mytest/area.html', {'list': areas, 'list0': areas0})
    else:
        res = render(request, 'mytest/area.html', {'list': areas, 'list0': areas0})
        # print(res, dir(res))
        res.set_cookie('name', 'ggb')
        print(res.content)
        print(res.cookies)
        return res

    # return render(request, 'mytest/area.html', {'list': areas, 'list0': areas0})


def select(request):
    if request.method == 'POST':
        aid = request.POST['id']
        addr = request.POST['addr']
        # print(aid, addr)
        selected = Area.objects.get(pk=aid)
        # print(type(selected))
        child = selected.area_set.all()
        # print(type(child))
        list1 = [c.title for c in child]
        # print(list1)
        # print(selected.title, selected.parrent_area.title)
        # print(type(selected.title), type(selected.parrent_area.title))
        dict1 = {"now": selected.title,"par":selected.parrent_area.title,"childs": list1}
        return HttpResponse(json.dumps(dict1))

