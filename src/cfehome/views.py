import json
from django.http import JsonResponse
from django.shortcuts import render

from contents.forms import ContentForm
from contents.models import Content


def home_view(request):
    return render(request, "home.html")


def api_content_list_view(request):
    content_list = [
        {"id": 1, "title": "Hello world"},
        {"id": 2, "title": "Hello world again frère"},
    ]
    return JsonResponse({"data": content_list})


def api_content_create_view(request):
    if not request.method == "POST":
        return JsonResponse({}, status=400)
    data = {}
    try:
        data = json.loads(request.body)
    except:
        pass
    title = data.get("title") or None
    if "abc" in title:
        return JsonResponse(
            {"detail": f"{title} n'est pas valide, merci de retirer 'abc' du titre"},
            status=400,
        )
    form = ContentForm(data)
    if form.is_valid():
        obj = form.save()
        data = {
            "id": obj.id,
            "title": obj.title,
            "content": obj.content,
            "isCreated": True,
        }
        return JsonResponse(data, status=201)
    errors = json.loads(form.errors.as_json())
    return JsonResponse(errors, status=400)
