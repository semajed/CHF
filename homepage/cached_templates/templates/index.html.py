# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428024712.698177
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n')
        if request.user.username != '':
            __M_writer('\t\t<div id="personalHello">\n\t\t\t<h1 >Hello, ')
            __M_writer(str(request.user.get_full_name()))
            __M_writer('!</h1>\n\t\t</div>\n')
        else:
            __M_writer('\t\t<div id="personalHello">\n\t\t\t<h1>Hello, Visitor!</h1>\n\t\t</div>\n')
        __M_writer('\t<hr>\n    <div class="jumbotron">\n      <div class="container">\n        <h1>Colonial Heritage Foundation</h1>\n        <p>\n            This paragraph will be an explanation of the fondation and what they do. Eventually, it would be great to have a carosel of images displaying 3 things: Events, merchandise, and volunteer opportunities.\n        </p>\n        <p><a class="btn btn-primary btn-lg pull-right" href="/homepage/users.userCreate" role="button">Create Account</a></p>\n\n      </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"66": 60, "35": 1, "40": 25, "46": 4, "59": 10, "53": 4, "54": 5, "55": 6, "56": 7, "57": 7, "58": 9, "27": 0, "60": 14}, "uri": "index.html", "source_encoding": "ascii", "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/index.html"}
__M_END_METADATA
"""
