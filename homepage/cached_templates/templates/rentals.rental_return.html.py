# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427749866.301684
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/rentals.rental_return.html'
_template_uri = 'rentals.rental_return.html'
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
        rental = context.get('rental', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        rented_items = context.get('rented_items', UNDEFINED)
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
        rental = context.get('rental', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        rented_items = context.get('rented_items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <h1>Return Rental\n')
        __M_writer('\n')
        __M_writer('\n  </h1>\n  <hr>\n  <div class="col-md-4">\n    <h3>Rental Information:</h3>\n    <table class="table table-striped">\n      <div>\n        <tr>\n          <td>Rentee</td>\n          <td>')
        __M_writer(str(rental.memberName))
        __M_writer('</td>\n        </tr>\n        <tr>\n          <td>Username</td>\n          <td>')
        __M_writer(str(rental.memberName.username))
        __M_writer('</td>\n        </tr>\n        <tr>\n          <td>Rental Date</td>\n          <td>')
        __M_writer(str(rental.rentalTime.strftime('%m/%d/%Y')))
        __M_writer('</td>\n        </tr>\n        <tr>\n          <td>Due Date</td>\n          <td>')
        __M_writer(str(rental.dueDate.strftime('%m/%d/%Y')))
        __M_writer('</td>\n        </tr>\n      </div>\n    </table>\n  </div>\n  <div class="col-md-8">\n')
        __M_writer('      <h3>Rented Items: <input type="submit" value="Save Changes" class="pull-right btn btn-info btn-sm"></h3>\n      <table class="table table-striped">\n        <div>\n        <tr>\n          <th>Picture</th>\n          <th>Item</th>\n          <th>Price / day</th>\n          <th>Quantity</th>\n          <th>Condition</th>\n        </tr>\n')
        for r in rented_items:
            __M_writer('          <tr>\n            <td><img class="productImage" src="')
            __M_writer(str(STATIC_URL))
            __M_writer('homepage/media/Glasses.jpg"></td>\n            <td>')
            __M_writer(str(r.item.name))
            __M_writer('</td>\n            <td>')
            __M_writer(str(r.item.STP))
            __M_writer('</td>\n            <td>QTY</td>\n            <td>\n              <select data-rid="')
            __M_writer(str(r.id))
            __M_writer('" id="condition" class="form-control change_condition">\n                <option value="')
            __M_writer(str(r.item.condition))
            __M_writer('">')
            __M_writer(str(r.item.condition))
            __M_writer('</option>\n                <option value="invalid" disabled>-------</option>\n                <option value="Looks New">Looks New</option>\n                <option value="Slightly Used">Slightly Used</option>\n                <option value="Moderately Used">Moderately Used</option>\n                <option value="Heavily Used">Heavily Used</option>\n                <option value="Destroyed">Destroyed</option>\n              </select>\n\n            </td>\n          </tr>\n')
        __M_writer('        </div>\n      </table>\n')
        __M_writer('  </div>\n\n \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "rentals.rental_return.html", "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/rentals.rental_return.html", "line_map": {"64": 29, "65": 33, "66": 33, "67": 40, "68": 50, "69": 51, "70": 52, "71": 52, "72": 53, "73": 53, "74": 54, "75": 54, "76": 57, "77": 57, "78": 58, "79": 58, "80": 58, "81": 58, "82": 70, "83": 73, "89": 83, "27": 0, "37": 1, "47": 3, "56": 3, "57": 10, "58": 12, "59": 21, "60": 21, "61": 25, "62": 25, "63": 29}}
__M_END_METADATA
"""
