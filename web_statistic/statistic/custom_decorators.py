from django.shortcuts import render_to_response

def responding_static_page(page):
    def wrapper(func):
        def wrapp(*args, **kwargs):
            data = func(*args, **kwargs)
            return render_to_response(page, data)
        return wrapp
    return wrapper