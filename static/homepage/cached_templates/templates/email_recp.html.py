# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427999960.565695
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/email_recp.html'
_template_uri = 'email_recp.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        item_list2 = context.get('item_list2', UNDEFINED)
        qty = context.get('qty', UNDEFINED)
        rental_return = context.get('rental_return', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        product_list2 = context.get('product_list2', UNDEFINED)
        __M_writer = context.writer()
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n\n\n\n\n\n\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        item_list2 = context.get('item_list2', UNDEFINED)
        qty = context.get('qty', UNDEFINED)
        rental_return = context.get('rental_return', UNDEFINED)
        def content():
            return render_content(context)
        product_list2 = context.get('product_list2', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\t<div id="thankyou"class="container col-md-12">\n    \t<h1>Thank You</h1>\n    \t<hr>\n\t</div>\n\n    <div class="container col-md-12">\n    <h3>Receipt for Payment</h3>\n')
        if product_list2:
            __M_writer('        <table id="shopping_cartTable">\n            <tr>\n                <th>Product</th>\n                <th>Price</th>\n                <th>Quantity</th>\n            </tr>\n')
            for product in product_list2:
                __M_writer('            <tr>\n                <td>')
                __M_writer(str(product.name))
                __M_writer('</td>\n                <td>$')
                __M_writer(str(product.currentPrice))
                __M_writer('</td>\n                <td>')
                __M_writer(str(qty))
                __M_writer('</td>\n            </tr>\n')
            __M_writer('        </table>\n')
        if item_list2:
            __M_writer('        <table id="shopping_cartTable">\n            <tr>\n                <th>Item</th>\n                <th>Price / day</th>\n                <th>Quantity</th>\n            </tr>\n')
            for item in item_list2:
                __M_writer('            <tr>\n                <td>')
                __M_writer(str(item.name))
                __M_writer('</td>\n                <td>$')
                __M_writer(str(item.STP))
                __M_writer('</td>\n                <td>')
                __M_writer(str(qty))
                __M_writer('</td>\n            </tr>\n')
            __M_writer('        </table>\n')
        if rental_return:
            __M_writer('            <div><span>Damage Fee:</span> $')
            __M_writer(str(rental_return.damageFee))
            __M_writer('</div>\n            <br>\n            <div><span>Late Fee:</span> $')
            __M_writer(str(rental_return.lateFee))
            __M_writer('</div>\n            <br>\n            <div><span>Total Fee:</span> $')
            __M_writer(str(rental_return.totalFee))
            __M_writer('</div>\n')
        __M_writer('    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "email_recp.html", "source_encoding": "ascii", "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/email_recp.html", "line_map": {"64": 35, "65": 36, "66": 36, "67": 37, "68": 37, "69": 40, "70": 42, "71": 43, "72": 43, "73": 43, "74": 45, "75": 45, "76": 47, "77": 47, "78": 49, "16": 0, "84": 78, "31": 51, "37": 1, "47": 1, "48": 10, "49": 11, "50": 17, "51": 18, "52": 19, "53": 19, "54": 20, "55": 20, "56": 21, "57": 21, "58": 24, "59": 26, "60": 27, "61": 33, "62": 34, "63": 35}}
__M_END_METADATA
"""
