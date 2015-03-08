# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425779133.493038
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/items.html'
_template_uri = 'items.html'
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
        items = context.get('items', UNDEFINED)
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
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <h1>Item Management     <a role="button"class=\'btn btn-xl btn-danger pull-right\' href="/homepage/items.late/">All over-due items</a>\n</h1>\n    <hr>\n    <p><a class="btn btn-primary btn-lg" href="/homepage/items.create" role="button">Create Item</a></p>\n\n    <div class="container col-md-9">\n      <table id="roleTable" class="table table-hover">\n        <tr >\n          <th>Name</th>\n          <th>Description</th>\n          <th>Value</th>\n          <th>Rental Price</th>\n          <th>Due Date</th>\n          <th>Action</th>\n        </tr>\n')
        for item in items:
            __M_writer('        <tr>\n          <td>')
            __M_writer(str(item.name))
            __M_writer('</td>\n          <td>')
            __M_writer(str(item.description))
            __M_writer('</td>\n          <td>')
            __M_writer(str(item.value))
            __M_writer('</td>\n          <td>')
            __M_writer(str(item.STP))
            __M_writer('</td>\n          <td>')
            __M_writer(str(item.dueDate))
            __M_writer('</td>\n          <td>\n          <a class=\'btn btn-xl btn-primary\' href="/homepage/items.edit/')
            __M_writer(str(item.id))
            __M_writer('/">EDIT</a>\n          </td>\n        </tr>\n')
        __M_writer('      </table>\n    </div>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/items.html", "uri": "items.html", "line_map": {"64": 25, "65": 27, "66": 27, "35": 1, "73": 67, "45": 3, "27": 0, "67": 31, "52": 3, "53": 19, "54": 20, "55": 21, "56": 21, "57": 22, "58": 22, "59": 23, "60": 23, "61": 24, "62": 24, "63": 25}, "source_encoding": "ascii"}
__M_END_METADATA
"""
