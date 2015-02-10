# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423350340.891025
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'header', 'footer']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def footer():
            return render_footer(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n  <head>\n    \n    <title>CHF Delux</title>\n    <link rel="icon" type="image" href="http://ifunny.co/public/images/favicons/favicon-195.png"/>\n    \n')
        __M_writer('    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\n    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\n    <script \n    src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.3.1/js/bootstrap-datepicker.js">\n    </script>\n    \n\n  \n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n  \n  </head>\n  <body>\n  \n    <header>\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\n  </header>\n\n')
        __M_writer('        \n')
        __M_writer('\n\n  <div class="container" id="theContent">\n    ')
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


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        user = context.get('user', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n        <nav class="navbar navbar-inverse navbar-fixed-top navbar-left">\n        <div class="container-fluid">\n          <div class="navbar-header" id="navBarTop">\n            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">\n              <span class="icon-bar"></span>\n              <span class="icon-bar"></span>\n              <span class="icon-bar"></span>\n            </button>\n            <a class="navbar-brand" href="#">Colonial Heritage Foundation</a>\n\n          </div>\n          <div id="navbar" class="collapse navbar-collapse">\n            <ul class="nav nav-pills pull-right" role="tablist" id="headerBadges">\n              <li><a href="/homepage/index">Home</a></li>\n              <li><a href="/homepage/users">Users</a></li>\n              <li><a href="/homepage/events">Events</a></li>\n              <li><a href="/homepage/areas">Areas</a></li>\n              <li><a href="/homepage/saleitems">Sale Items</a></li>\n              <li><a href="/homepage/items">Items</a></li>\n              <li><a href="/homepage/products">Products</a></li>\n\n')
        if user.is_authenticated:
            __M_writer('                <li><a href="/homepage/">Logged in as ')
            __M_writer(str(request.user.username))
            __M_writer('</a></li>\n')
        else:
            __M_writer('                <li><a href="/homepage/login">Login</a></li>\n')
        __M_writer('            </ul>\n          </div>\n        </div>\n      </nav>\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\n      <div id="footerText" class="container">\n        <ul class="navbar-text col-md-10">\n          <p><h6><a href="/homepage/login">Login</a></h6></p>\n          <p><h6><a href="/homepage/login.logout_view">Logout</a></h6></p>  \n          <p><h6><a href="/homepage/permissions">Permission</a></h6></p>            \n          <p><h6><a href="/homepage/about">About</a></h6></p>\n          <p><h6><a href="/homepage/contact">Contact</a></h6></p>\n          <p><h6><a href="/homepage/terms">Terms</a></h6></p>\n        </ul>\n      </div>\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"68": 76, "113": 107, "74": 76, "80": 32, "18": 0, "88": 32, "89": 54, "90": 55, "91": 55, "92": 55, "93": 56, "94": 57, "95": 59, "32": 2, "33": 4, "34": 5, "101": 82, "38": 5, "39": 16, "40": 26, "41": 26, "42": 26, "107": 82, "47": 63, "48": 69, "49": 73, "54": 78, "59": 93, "60": 97, "61": 97, "62": 97, "16": 4}, "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/base.htm", "source_encoding": "ascii", "uri": "base.htm"}
__M_END_METADATA
"""
