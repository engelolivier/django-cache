
#-*- coding: utf-8 -*-

################################
#  EXEMPLE DE VIEW
################################

import cache.py

@custom_cache
def category(request, slug, *args, **kwargs):
    
  ...

  return render(request, os.path.dirname(os.path.abspath(__file__)) + '/templates/category.html', locals() )