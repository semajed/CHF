# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423349717.412411
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
        form = context.get('form', UNDEFINED)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n    <div class="container">\n\t    <form method=\'POST\'>\n\t    <h2>User Information:</h2>\n\t    \t<div class="container" id="addressForm">\n\t\t\t    <table>\n\t\t\t    \t')
        __M_writer(str(form))
        __M_writer('\n\t\t\t    </table>\n\t\t    </div>\n\t\t    <button class=\'btn btn-xl btn-primary\' type="submit">Save</button>\n\t\t    <a class=\'btn btn-xl btn-danger\' href="/homepage/users.delete/')
        __M_writer(str(user.id))
        __M_writer('/">DELETE</a>\n')
        if user.username == "":
            __M_writer('\t\t    \t<a class=\'btn btn-xl btn-default\' href="/homepage/users.delete/')
            __M_writer(str(user.id))
            __M_writer('/">Cancel</a>\n')
        elif user.username != "":
            __M_writer('\t\t    \t<a class=\'btn btn-xl btn-default\' href="/homepage/users/">Cancel</a>\n')
        __M_writer('\t    </form>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 18, "65": 20, "27": 0, "36": 1, "71": 65, "46": 3, "54": 3, "55": 10, "56": 10, "57": 14, "58": 14, "59": 15, "60": 16, "61": 16, "62": 16, "63": 17}, "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/users.edit.html", "source_encoding": "ascii", "uri": "users.edit.html"}
__M_END_METADATA
"""
