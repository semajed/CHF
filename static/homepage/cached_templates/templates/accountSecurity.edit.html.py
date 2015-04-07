# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425538659.681836
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/accountSecurity.edit.html'
_template_uri = 'accountSecurity.edit.html'
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
        __M_writer = context.writer()
        __M_writer('\n\n    <div class="container">\n        <form method=\'POST\'>\n        <h2>Account Security Information:</h2>\n        <div><span class="label label-danger">Important:</span> You will be logged out once you change your password. You can log back in immediately after changing your password.</div>\n        <hr>\n            <div class="container" id="addressForm">\n                <table>\n                    ')
        __M_writer(str(form))
        __M_writer('\n                </table>\n            </div>\n            <button class=\'btn btn-xl btn-primary\' type="submit"><i class="glyphicon glyphicon-ok"></i></button>\n            <a class=\'btn btn-xl btn-default pull-right\' href="javascript:history.back(-1);">Cancel</a>\n        </form>\n\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/accountSecurity.edit.html", "uri": "accountSecurity.edit.html", "line_map": {"35": 1, "52": 3, "53": 12, "54": 12, "27": 0, "60": 54, "45": 3}, "source_encoding": "ascii"}
__M_END_METADATA
"""
