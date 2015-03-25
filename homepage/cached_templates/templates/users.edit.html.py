# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426199138.319238
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/users.edit.html'
_template_uri = 'users.edit.html'
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
        request = context.get('request', UNDEFINED)
        form = context.get('form', UNDEFINED)
        user = context.get('user', UNDEFINED)
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
        def content():
            return render_content(context)
        request = context.get('request', UNDEFINED)
        form = context.get('form', UNDEFINED)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n    <div class="container">\n        <form method=\'POST\' enctype="multipart/form-data">\n        <h2>User Information:</h2>\n        <hr>\n            <div class="container" id="addressForm">\n                <table>\n                    ')
        __M_writer(str(form))
        __M_writer('\n                </table>\n            </div>\n            <hr>\n            <button class=\'btn btn-xl btn-primary\' type="submit"><i class="glyphicon glyphicon-ok"></i></button>\n            <a class=\'btn btn-xl btn-danger\' href="/homepage/users.delete/')
        __M_writer(str(user.id))
        __M_writer('/"><i class="glyphicon glyphicon-trash"></i></a>\n')
        if user.username == "":
            __M_writer('                <a class=\'btn btn-xl btn-default pull-right\' href="/homepage/users.delete/')
            __M_writer(str(user.id))
            __M_writer('/">Cancel</a>\n')
        elif user.username != "":
            __M_writer('                <a class=\'btn btn-xl btn-default pull-right\' href="javascript:history.back(-1);">Cancel</a>\n')
        __M_writer('        </form>\n        <hr>\n')
        if request.user.username != '':
            __M_writer('            <h3>Change Account Security Details\n                <span>\n                    <a class="btn btn-warning pull-right" href="/homepage/accountSecurity.edit/')
            __M_writer(str(user.id))
            __M_writer('/" role="button">Edit Security</a>\n                </span>\n            </h3>\n\n            <p>Change the following:</p>\n            <ul>\n                <li>Password</li>\n                <li>Security Question</li>\n                <li>Security Answer</li>\n            </ul>\n')
        __M_writer('\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 18, "65": 19, "66": 20, "27": 0, "68": 24, "37": 1, "70": 27, "71": 27, "72": 38, "78": 72, "47": 3, "67": 22, "69": 25, "56": 3, "57": 11, "58": 11, "59": 16, "60": 16, "61": 17, "62": 18, "63": 18}, "uri": "users.edit.html", "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/users.edit.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
