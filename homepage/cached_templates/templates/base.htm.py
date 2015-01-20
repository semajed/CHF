# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421350640.558426
_enable_loop = True
_template_filename = '/Library/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['footer', 'content', 'leftSideBar', 'header']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def leftSideBar():
            return render_leftSideBar(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n  <head>\n    \n    <title>CHF Delux</title>\n    <link rel="icon" type="image/png" href="http://ifunny.co/public/images/favicons/favicon-195.png" />\n    \n')
        __M_writer('    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\n    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\n    \n\n  \n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n  \n  </head>\n  <body>\n  \n    <header>\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\n  </header>\n\n    \n    <div class="col-sm-3 col-md-2 sidebar pull-right">\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'leftSideBar'):
            context['self'].leftSideBar(**pageargs)
        

        __M_writer('\n    </div>\n\n  <div class="container">\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('  \n  </div>\n\n  <div class = "navbar navbar-default navbar-fixed-bottom" id="footer">\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\n  </div>\n\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  \n  </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\n      <div class = "container">\n        <p class = "navbar-text pull-left">Site built by Jasper Wright</p>\n        <a href="http://youtube.com" class="navbar-btn btn-info btn-sm pull-right" id="subscribe">Subscribe</a>\n      </div>\n    ')
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


def render_leftSideBar(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def leftSideBar():
            return render_leftSideBar(context)
        __M_writer = context.writer()
        __M_writer('\n        <ul class="nav nav-sidebar">\n            <li><a href="/index">Home</a></li>\n            <li><a href="/about">About</a></li>\n            <li><a href="/contact">Contact</a></li>\n            <li><a href="/terms">Terms</a></li>\n          </ul>\n          <ul class="nav nav-sidebar">\n            <li><a href="">Nav item</a></li>\n            <li><a href="">Nav item again</a></li>\n            <li><a href="">One more nav</a></li>\n            <li><a href="">Another nav item</a></li>\n            <li><a href="">More navigation</a></li>\n          </ul>\n          <ul class="nav nav-sidebar">\n            <li><a href="">Nav item again</a></li>\n            <li><a href="">One more nav</a></li>\n            <li><a href="">Another nav item</a></li>\n          </ul>\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\n        <nav class="navbar navbar-inverse navbar-fixed-top navbar-left">\n        <div class="container-fluid">\n          <div class="navbar-header" id="navBarTop">\n            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">\n              <span class="icon-bar"></span>\n              <span class="icon-bar"></span>\n              <span class="icon-bar"></span>\n            </button>\n            <a class="navbar-brand" href="#">Colonial Heritage Foundation</a>\n\n          </div>\n          <div id="navbar" class="collapse navbar-collapse">\n            <ul class="nav nav-pills pull-right" role="tablist" id="headerBadges">\n              <li role="presentation"><a href="#">Profile</a></li>\n              <li role="presentation"><a href="#">Messages <span class="badge">3</span></a></li>\n            </ul>\n          </div>\n        </div>\n      </nav>\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Library/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/base.htm", "line_map": {"64": 92, "65": 92, "66": 92, "72": 83, "78": 83, "16": 4, "18": 0, "84": 77, "90": 77, "96": 54, "33": 2, "34": 4, "35": 5, "102": 54, "39": 5, "40": 16, "41": 23, "42": 23, "43": 23, "108": 29, "48": 49, "114": 29, "53": 73, "120": 114, "58": 79, "63": 88}, "uri": "base.htm"}
__M_END_METADATA
"""
