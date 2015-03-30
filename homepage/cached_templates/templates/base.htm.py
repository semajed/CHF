# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427424206.174338
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'footer', 'header']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n  <head>\n    \n    <title>CHF Delux</title>\n    <link rel="icon" type="image" href="http://ifunny.co/public/images/favicons/favicon-195.png"/>\n    \n')
        __M_writer('    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\n    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\n    <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.3.1/js/bootstrap-datepicker.js">\n    </script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.form.js">\n    </script>\n     <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.loadmodal.js">\n    </script>\n')
        __M_writer('    \n\n  \n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n  \n  </head>\n  <body>\n  \n    <header>\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\n  </header>\n\n\n  <div class="container" id="theContent">\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('  \n  </div>\n\n  <div class="navbar navbar-inverse" id="footer">\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\n  </div>\n\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  \n  </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n      Site content goes here in sub-templates.\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\n      <div id="footerText" class="container">\n        <ul class="navbar-text col-md-10">\n          <p><h6><a href="/homepage/about">About</a></h6></p>\n          <p><h6><a href="/homepage/contact">Contact</a></h6></p>\n          <p><h6><a href="/homepage/terms">Terms</a></h6></p>\n        </ul>\n      </div>\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        user = context.get('user', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\n\n        <nav class="navbar navbar-inverse navbar-fixed-top navbar-left">\n        <div class="container-fluid">\n          <div class="navbar-header" id="navBarTop">\n            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">\n              <span class="icon-bar"></span>\n              <span class="icon-bar"></span>\n              <span class="icon-bar"></span>\n            </button>\n            <a class="navbar-brand" href="#">Colonial Heritage Foundation</a>\n\n          </div>\n          <div id="navbar" class="collapse navbar-collapse offcanvas">\n            <ul class="nav nav-pills pull-right" role="tablist" id="headerBadges">\n            <li><a href="/homepage/index">Home</a></li>\n            <li class="dropdown">\n                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Browse Catalogs<span class="caret"></span></a>\n                <ul class="dropdown-menu" role="menu">\n                  <li><a href="/homepage/catalog">Product Catalog</a></li>\n                  <li class="divider"></li>\n                  <li><a href="/homepage/rental_catalog">Rental Catalog</a></li>\n                </ul>\n              </li>\n')
        if request.user.is_superuser or request.user.is_staff:
            __M_writer('              <li class="dropdown">\n                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Management <span class="caret"></span></a>\n                <ul class="dropdown-menu" role="menu">\n                  <li><a href="/homepage/users">Users</a></li>\n                  <li><a href="/homepage/events">Events</a></li>\n                  <li><a href="/homepage/areas">Areas</a></li>\n                  <li><a href="/homepage/saleitems">Sale Items</a></li>\n                  <li><a href="/homepage/items">Items</a></li>\n                  <li><a href="/homepage/products">Products</a></li>\n                  <li><a href="/homepage/rentals">Rentals</a></li>\n')
            if user.is_superuser:
                __M_writer('                  <li><a href="/homepage/permissions">Permission</a></li>\n')
            __M_writer('                </ul>\n              </li>\n')
        __M_writer('\n')
        if request.user.is_authenticated():
            __M_writer('                <li class="dropdown">\n                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Logged in as ')
            __M_writer(str(request.user.get_full_name()))
            __M_writer(' <span class="caret"></span></a>\n                <ul class="dropdown-menu" role="menu">\n')
            __M_writer('                  <li><a href="/homepage/account/')
            __M_writer(str(request.user.id))
            __M_writer('/">View my Account</a></li>\n                  <li class="divider"></li>\n                  <li><a href="/homepage/index.logout_view">Logout</a></li>\n                </ul>\n              </li>\n')
        else:
            __M_writer('                <li><a id="show_login_dialog">Login</a></li>\n')
        __M_writer('            </ul>\n          </div>\n        </div>\n      </nav>\n\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 4, "18": 0, "33": 2, "34": 4, "35": 5, "39": 5, "40": 16, "41": 21, "42": 21, "43": 23, "44": 23, "45": 26, "46": 30, "47": 30, "48": 30, "53": 96, "58": 103, "63": 115, "64": 119, "65": 119, "66": 119, "72": 101, "78": 101, "84": 107, "90": 107, "96": 36, "104": 36, "105": 60, "106": 61, "107": 71, "108": 72, "109": 74, "110": 77, "111": 78, "112": 79, "113": 80, "114": 80, "115": 83, "116": 83, "117": 83, "118": 88, "119": 89, "120": 91, "126": 120}, "uri": "base.htm", "source_encoding": "ascii", "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/base.htm"}
__M_END_METADATA
"""
