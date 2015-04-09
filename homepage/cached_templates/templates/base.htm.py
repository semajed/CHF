# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428550881.559019
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['header', 'content']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def header():
            return render_header(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n  <head>\n    \n    <title>Colonial Heritage Foundation</title>\n    <meta name="description" content="The Colonial Heritage Foundation is a place for people to gather to buy products from different time periods. It is also a place to view public events put on by the Colonial Heritage Foundation." />\n    <meta name="keywords" content="Colonial, heritage, foundation, time period, public, events, products, rental, fun, experience, local, event" />\n    <link rel="icon" type="image" href="http://ifunny.co/public/images/favicons/favicon-195.png"/>\n    \n')
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
        

        __M_writer('  \n  </div>\n\n')
        __M_writer('\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  \n  </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        user = context.get('user', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n        <nav class="navbar navbar-inverse navbar-fixed-top navbar-left">\n        <div class="container-fluid">\n          <div class="navbar-header" id="navBarTop">\n            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">\n              <span class="icon-bar"></span>\n              <span class="icon-bar"></span>\n              <span class="icon-bar"></span>\n            </button>\n            <a class="navbar-brand" href="#"><h4>Colonial Heritage Foundation</h4></a>\n\n          </div>\n          <div id="navbar" class="collapse navbar-collapse offcanvas">\n            <ul class="nav nav-pills pull-right" role="tablist" id="headerBadges">\n            <li><a href="/homepage/index">Home</a></li>\n            <li><a href="/homepage/event_catalog">Events</a></li>\n            <li class="dropdown">\n                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Browse Catalogs<span class="caret"></span></a>\n                <ul class="dropdown-menu" role="menu">\n                  <li><a href="/homepage/catalog">Product Catalog</a></li>\n                  <li class="divider"></li>\n                  <li><a href="/homepage/rental_catalog">Rental Catalog</a></li>\n                </ul>\n              </li>\n')
        if request.user.is_superuser or request.user.is_staff:
            __M_writer('              <li class="dropdown">\n                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Management <span class="caret"></span></a>\n                <ul class="dropdown-menu" role="menu">\n                  <li><a href="/homepage/users">Users</a></li>\n                  <li><a href="/homepage/events">Events</a></li>\n                  <li><a href="/homepage/areas">Areas</a></li>\n                  <li><a href="/homepage/saleitems">Sale Items</a></li>\n                  <li><a href="/homepage/items">Items</a></li>\n                  <li><a href="/homepage/products">Products</a></li>\n                  <li><a href="/homepage/rentals">Rentals</a></li>\n')
            if user.is_superuser:
                __M_writer('                  <li><a href="/homepage/permissions">Permission</a></li>\n')
            __M_writer('                </ul>\n              </li>\n')
        __M_writer('\n')
        if request.user.is_authenticated():
            __M_writer('                <li class="dropdown">\n                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Logged in as ')
            __M_writer(str(request.user.first_name))
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


"""
__M_BEGIN_METADATA
{"uri": "base.htm", "source_encoding": "ascii", "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/base.htm", "line_map": {"96": 104, "66": 38, "80": 80, "74": 38, "75": 63, "76": 64, "77": 74, "78": 75, "79": 77, "16": 4, "81": 81, "18": 0, "83": 83, "84": 83, "85": 86, "86": 86, "87": 86, "88": 91, "89": 92, "90": 94, "31": 2, "32": 4, "33": 5, "82": 82, "37": 5, "38": 18, "39": 23, "40": 23, "41": 25, "42": 25, "43": 28, "44": 32, "45": 32, "46": 32, "108": 102, "51": 99, "56": 106, "57": 120, "58": 122, "59": 122, "60": 122, "102": 104}}
__M_END_METADATA
"""
