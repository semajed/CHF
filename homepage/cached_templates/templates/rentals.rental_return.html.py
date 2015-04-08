# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428451999.279773
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
        rented_items = context.get('rented_items', UNDEFINED)
        rental = context.get('rental', UNDEFINED)
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
        rented_items = context.get('rented_items', UNDEFINED)
        rental = context.get('rental', UNDEFINED)
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
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
        __M_writer('</td>\n        </tr>\n      </div>\n    </table>\n      <form method="POST">\n        <div class="fees">\n          ')
        __M_writer(str(form))
        __M_writer('\n          <input class=\'btn btn-warning col-md-8\' type=\'submit\' value="Return">\n        </div>\n      </form>\n  </div>\n  <div class="col-md-8">\n    <h3>Rented Items:</h3>\n    <table class="table table-striped">\n      <div>\n      <tr>\n        <th>Picture</th>\n        <th>Item</th>\n        <th>Price / day</th>\n        <th>Value</th>\n        <th>Quantity</th>\n        <th>Condition</th>\n      </tr>\n')
        for r in rented_items:
            __M_writer('        <tr>\n          <td><img class="productImage" src="')
            __M_writer(str(r.photo.image))
            __M_writer('"></td>\n          <td>')
            __M_writer(str(r.item.name))
            __M_writer('</td>\n          <td>$')
            __M_writer(str(r.item.STP))
            __M_writer('</td>\n          <td>$')
            __M_writer(str(r.item.value))
            __M_writer('</td>\n          <td>QTY</td>\n          <td>\n            <select data-rid="')
            __M_writer(str(r.id))
            __M_writer('" id="condition" class="form-control change_condition">\n              <option value="')
            __M_writer(str(r.item.condition))
            __M_writer('">')
            __M_writer(str(r.item.condition))
            __M_writer('</option>\n              <option value="invalid" disabled>-------</option>\n              <option value="Looks New">Looks New</option>\n              <option value="Slightly Used">Slightly Used</option>\n              <option value="Moderately Used">Moderately Used</option>\n              <option value="Heavily Used">Heavily Used</option>\n              <option value="Destroyed">Destroyed</option>\n            </select>\n          </td>\n        </tr>\n')
        __M_writer('      </div>\n    </table>\n  </div>\n\n\n\n \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "rentals.rental_return.html", "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/rentals.rental_return.html", "source_encoding": "ascii", "line_map": {"64": 29, "65": 33, "66": 33, "67": 39, "68": 39, "69": 56, "70": 57, "71": 58, "72": 58, "73": 59, "74": 59, "75": 60, "76": 60, "77": 61, "78": 61, "79": 64, "80": 64, "81": 65, "82": 65, "83": 65, "84": 65, "85": 76, "27": 0, "91": 85, "37": 1, "47": 3, "56": 3, "57": 10, "58": 12, "59": 21, "60": 21, "61": 25, "62": 25, "63": 29}}
__M_END_METADATA
"""
