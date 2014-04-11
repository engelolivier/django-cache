#-*- coding: utf-8 -*-
import os
import hashlib
from django.http import HttpResponse, HttpResponseBadRequest


def custom_cache(func):
    
    def cache(request, *args, **kwargs):
        
        if is_cache_exist(request):
            path = md5_cache_filename(request)
            with open(path, "r") as file:
                return HttpResponse(file.read())
        
        path = md5_cache_filename(request)
        html = func(request, *args, **kwargs)
        
        with open(path, "w") as file:
            file.write(html.content)
        
        return HttpResponse(html)
        
    return cache

def md5_cache_filename(request):
    
    filemd5 = md5(request.path_info)
    path = '/data/cache/%s' % filemd5
    return path

def is_cache_exist(request):
    
    try:
        path = md5_cache_filename(request)
        return os.path.isfile(path)
    except:
        return False

def md5(string):
    """
    Retourne le md5 d'une string
    """
    return hashlib.md5(string.encode("utf")).hexdigest()