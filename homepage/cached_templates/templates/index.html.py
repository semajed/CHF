# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422752610.266152
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
        def content():
            return render_content(context._locals(__M_locals))
        allRoles = context.get('allRoles', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        __M_writer(str(allRoles))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="jumbotron">\n      <div class="container">\n        <h1>Colonial Heritage Foundation</h1>\n        <p>\n       \t\tThis paragraph will be an explanation of the fondation and what they do. Eventually, it would be great to have a carosel of images displaying 3 things: Events, merchandise, and volunteer opportunities.\n        </p>\n        <p><a class="pull-left" href="#">Sign in</a></p>\n        <p><a class="btn btn-primary btn-lg pull-right" href="/homepage/users.create" role="button">Create Account</a></p>\n      </div>\n    </div>\n   \n\n    \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/index.html", "source_encoding": "ascii", "uri": "index.html", "line_map": {"59": 53, "35": 1, "53": 3, "40": 18, "41": 19, "27": 0, "47": 3}}
__M_END_METADATA
"""
