# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423008190.615561
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/areas.html'
_template_uri = 'areas.html'
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
        areas = context.get('areas', UNDEFINED)
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
        areas = context.get('areas', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <h1>This is the areas management page</h1>\n    <p><a class="btn btn-primary btn-lg" href="/homepage/areas.create" role="button">Create Area</a></p>\n\n    <div class="container col-md-9">\n      <table id="roleTable" class="table table-hover">\n        <tr >\n          <th>Name</th>\n          <th>Description</th>\n          <th>Place Number</th>\n          <th>Event</th>\n          <th>Action</th>\n        </tr>\n')
        for area in areas:
            __M_writer('        <tr>\n          <td>')
            __M_writer(str(area.name))
            __M_writer('</td>\n          <td>')
            __M_writer(str(area.description))
            __M_writer('</td>\n          <td>')
            __M_writer(str(area.placeNumber))
            __M_writer('</td>\n          <td>')
            __M_writer(str(area.event.name))
            __M_writer('</td>\n          <td>\n          <a class=\'btn btn-xl btn-primary\' href="/homepage/areas.edit/')
            __M_writer(str(area.id))
            __M_writer('/">EDIT</a>\n          </td>\n        </tr>\n')
        __M_writer('      </table>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 23, "65": 27, "35": 1, "71": 65, "45": 3, "27": 0, "52": 3, "53": 16, "54": 17, "55": 18, "56": 18, "57": 19, "58": 19, "59": 20, "60": 20, "61": 21, "62": 21, "63": 23}, "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/areas.html", "source_encoding": "ascii", "uri": "areas.html"}
__M_END_METADATA
"""
