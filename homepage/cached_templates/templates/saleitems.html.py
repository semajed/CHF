# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425626472.463914
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/saleitems.html'
_template_uri = 'saleitems.html'
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
        saleitems = context.get('saleitems', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        saleitems = context.get('saleitems', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <h1>Sale Item Management</h1>\n    <hr>\n    <p><a class="btn btn-primary btn-lg" href="/homepage/saleitems.create" role="button">Create Sale Item</a></p>\n\n    <div class="container col-md-9">\n      <table id="roleTable" class="table table-hover">\n        <tr >\n          <th>Name</th>\n          <th>Description</th>\n          <th>Low Price</th>\n          <th>High Price</th>\n          <th>Area</th>\n          <th>Action</th>\n        </tr>\n')
        for saleitem in saleitems:
            __M_writer('        <tr>\n          <td>')
            __M_writer(str(saleitem.name))
            __M_writer('</td>\n          <td>')
            __M_writer(str(saleitem.description))
            __M_writer('</td>\n          <td>')
            __M_writer(str(saleitem.lowPrice))
            __M_writer('</td>\n          <td>')
            __M_writer(str(saleitem.highPrice))
            __M_writer('</td>\n          <td>')
            __M_writer(str(saleitem.area.name))
            __M_writer('</td>\n          <td>\n          <a class=\'btn btn-xl btn-primary\' href="/homepage/saleitems.edit/')
            __M_writer(str(saleitem.id))
            __M_writer('/">EDIT</a>\n          </td>\n        </tr>\n')
        __M_writer('      </table>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 24, "65": 26, "66": 26, "35": 1, "73": 67, "45": 3, "27": 0, "67": 30, "52": 3, "53": 18, "54": 19, "55": 20, "56": 20, "57": 21, "58": 21, "59": 22, "60": 22, "61": 23, "62": 23, "63": 24}, "source_encoding": "ascii", "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/saleitems.html", "uri": "saleitems.html"}
__M_END_METADATA
"""
