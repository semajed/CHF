# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427428001.873462
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/rentals.html'
_template_uri = 'rentals.html'
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
        rentals = context.get('rentals', UNDEFINED)
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
        rentals = context.get('rentals', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n  <h1>Rentals Management \n  \n  <a role="button" class=\'btn btn-xl btn-danger pull-right filter_button\' href="/homepage/rentals.late/">View all over-due rentals</a>\n  <a role="button"class=\'btn btn-xl btn-info pull-right filter_button\' href="/homepage/rentals/">View all rentals</a>\n  <span id="filter_text"class="pull-right">Filter Rentals:</span>\n  </h1>\n  <hr>\n  <p>\n')
        __M_writer('    <div class="container col-md-12">\n      <table id="roleTable" class="table table-hover">\n        <tr >\n          <th>Name</th>\n          <th>Rental Date</th>\n          <th>Due Date</th>\n          <th>Handling Agent</th>\n          <th>Edit Rental</th>\n          <th>Return Rental</th>\n        </tr>\n')
        for rental in rentals:
            __M_writer('        <tr>\n          <td>')
            __M_writer(str(rental.memberName))
            __M_writer('</td>\n          <td>')
            __M_writer(str(rental.rentalTime.strftime('%m/%d/%Y')))
            __M_writer('</td>\n          <td>')
            __M_writer(str(rental.dueDate.strftime('%m/%d/%Y')))
            __M_writer('</td>\n          <td>')
            __M_writer(str(rental.handlingAgent))
            __M_writer('</td>\n          <td>\n          <a class=\'btn btn-xl btn-primary\' href="/homepage/rentals.edit/')
            __M_writer(str(rental.id))
            __M_writer('/">EDIT</a>\n          </td>\n          <td>\n          <a class=\'btn btn-xl btn-warning\' href="/homepage/rentals.rental_return/')
            __M_writer(str(rental.id))
            __M_writer('/">RETURN</a>\n          </td>\n        </tr>\n')
        __M_writer('      </table>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"64": 31, "65": 31, "66": 34, "35": 1, "68": 38, "74": 68, "45": 3, "27": 0, "67": 34, "52": 3, "53": 14, "54": 24, "55": 25, "56": 26, "57": 26, "58": 27, "59": 27, "60": 28, "61": 28, "62": 29, "63": 29}, "uri": "rentals.html", "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/rentals.html"}
__M_END_METADATA
"""
