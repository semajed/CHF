# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428451433.300678
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/forgot_password.html'
_template_uri = 'forgot_password.html'
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
        gotUser = context.get('gotUser', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        gotUser = context.get('gotUser', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <h1>Forgot Password</h1>\n')
        if gotUser is True:
            __M_writer('    \t<div>')
            __M_writer(str(user.secQuestion))
            __M_writer('</div>\n')
        __M_writer("    <form method='POST'>\n\t    <table>\n\t    \t")
        __M_writer(str(form))
        __M_writer('\n\t    </table>\n')
        if gotUser is False:
            __M_writer('\t    <button id="" class=\'btn btn-xl btn-primary\' type="submit">Find User</button>\n')
        else:
            __M_writer('\t    <button id="" class=\'btn btn-xl btn-primary\' type="submit">Send Email</button>\n\t    <hr>\n\t    <span class="label label-danger">Important </span>\n\t    <p> Once you enter the valid answer to the question, check your email for more instructions.</p>\n')
        __M_writer('    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/forgot_password.html", "uri": "forgot_password.html", "line_map": {"64": 12, "65": 13, "66": 14, "27": 0, "68": 20, "37": 1, "74": 68, "47": 3, "67": 15, "56": 3, "57": 5, "58": 6, "59": 6, "60": 6, "61": 8, "62": 10, "63": 10}, "source_encoding": "ascii"}
__M_END_METADATA
"""
