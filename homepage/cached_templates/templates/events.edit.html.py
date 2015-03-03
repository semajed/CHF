# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425360869.960647
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/events.edit.html'
_template_uri = 'events.edit.html'
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
        event = context.get('event', UNDEFINED)
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
        event = context.get('event', UNDEFINED)
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer("\n    <h1>Event Form</h1>\n    <form method='POST'>\n\t    <table>\n\t    \t")
        __M_writer(str(form))
        __M_writer('\n\t    </table>\n \n\t\t<br>\n\t    <button class=\'btn btn-xl btn-primary\' type="submit">Save</button>\n\t    <a class=\'btn btn-xl btn-danger\' href="/homepage/events.delete/')
        __M_writer(str(event.id))
        __M_writer('/">DELETE</a>\n')
        if event.name == "":
            __M_writer('\t    \t<a class=\'btn btn-xl btn-default\' href="/homepage/events.delete/')
            __M_writer(str(event.id))
            __M_writer('/">Cancel</a>\n')
        elif event.name != "":
            __M_writer('\t    \t<a class=\'btn btn-xl btn-default\' href="/homepage/events/">Cancel</a>\n')
        __M_writer('\t    <p>warning: if you delete an event, it will delete all areas attached to it.</p>\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/events.edit.html", "line_map": {"64": 16, "65": 18, "27": 0, "36": 1, "71": 65, "46": 3, "54": 3, "55": 7, "56": 7, "57": 12, "58": 12, "59": 13, "60": 14, "61": 14, "62": 14, "63": 15}, "uri": "events.edit.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
