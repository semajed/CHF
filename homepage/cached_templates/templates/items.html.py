# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425361615.510737
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
        items = context.get('items', UNDEFINED)
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
        items = context.get('items', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <h1>This is the item management page</h1>\n    <p><a class="btn btn-primary btn-lg" href="/homepage/items.create" role="button">Create Item</a></p>\n\n    <div class="container col-md-9">\n      <table id="roleTable" class="table table-hover">\n        <tr >\n          <th>Name</th>\n          <th>Description</th>\n          <th>Value</th>\n          <th>Rental Price</th>\n          <th>Owner</th>\n          <th>Action</th>\n        </tr>\n')
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
            __M_writer(str(item.owner.first_name))
            __M_writer(' ')
            __M_writer(str(item.owner.last_name))
            __M_writer('</td>\n          <td>\n          <a class=\'btn btn-xl btn-primary\' href="/homepage/items.edit/')
            __M_writer(str(item.id))
            __M_writer('/">EDIT</a>\n          </td>\n        </tr>\n')
        __M_writer('      </table>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 23, "65": 23, "66": 23, "67": 25, "68": 25, "69": 29, "75": 69, "27": 0, "35": 1, "45": 3, "52": 3, "53": 17, "54": 18, "55": 19, "56": 19, "57": 20, "58": 20, "59": 21, "60": 21, "61": 22, "62": 22, "63": 23}, "uri": "items.html", "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/items.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
