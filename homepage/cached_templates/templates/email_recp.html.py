# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428452661.119723
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
        def content():
            return render_content(context._locals(__M_locals))
        rental_return = context.get('rental_return', UNDEFINED)
        cart_product_list = context.get('cart_product_list', UNDEFINED)
        cart_item_list = context.get('cart_item_list', UNDEFINED)
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
        def content():
            return render_content(context)
        rental_return = context.get('rental_return', UNDEFINED)
        cart_product_list = context.get('cart_product_list', UNDEFINED)
        cart_item_list = context.get('cart_item_list', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\t<div id="thankyou"class="container col-md-12">\n    \t<h1>Thank You</h1>\n    \t<hr>\n\t</div>\n\n    <div class="container col-md-12">\n    <h3>Receipt for Payment</h3>\n')
        if cart_product_list:
            __M_writer('        <table id="shopping_cartTable">\n            <tr>\n                <th>Product</th>\n                <th>Quantity</th>\n                <th>Price / Product</th>\n                <th>Collective Cost</th>\n            </tr>\n')
            for product in cart_product_list:
                __M_writer('            <tr>\n                <td>')
                __M_writer(str(product.name))
                __M_writer('</td>\n                <td>')
                __M_writer(str(product.qty))
                __M_writer('</td>\n                <td>$')
                __M_writer(str(product.currentPrice))
                __M_writer('</td>\n                <td>$')
                __M_writer(str(product.collective_cost))
                __M_writer('</td>\n            </tr>\n')
            __M_writer('        </table>\n')
        if cart_item_list:
            __M_writer('        <table id="shopping_cartTable">\n            <tr>\n                <th>Item</th>\n                <th>Quantity</th>\n                <th>Price / Item</th>\n                <th>Collective Cost</th>\n            </tr>\n')
            for item in cart_item_list:
                __M_writer('            <tr>\n                <td>')
                __M_writer(str(item.name))
                __M_writer('</td>\n                <td>')
                __M_writer(str(item.qty))
                __M_writer('</td>\n                <td>$')
                __M_writer(str(item.STP))
                __M_writer('</td>\n                <td>$')
                __M_writer(str(item.collective_cost))
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
{"source_encoding": "ascii", "uri": "email_recp.html", "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/email_recp.html", "line_map": {"64": 38, "65": 39, "66": 39, "67": 40, "68": 40, "69": 41, "70": 41, "71": 44, "72": 46, "73": 47, "74": 47, "75": 47, "76": 49, "77": 49, "78": 51, "79": 51, "16": 0, "86": 80, "30": 55, "80": 53, "36": 1, "45": 1, "46": 10, "47": 11, "48": 18, "49": 19, "50": 20, "51": 20, "52": 21, "53": 21, "54": 22, "55": 22, "56": 23, "57": 23, "58": 26, "59": 28, "60": 29, "61": 36, "62": 37, "63": 38}}
__M_END_METADATA
"""
