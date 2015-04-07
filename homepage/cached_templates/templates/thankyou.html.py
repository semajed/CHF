# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428447924.422747
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/thankyou.html'
_template_uri = 'thankyou.html'
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
        rental_return = context.get('rental_return', UNDEFINED)
        cart_product_list = context.get('cart_product_list', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        order = context.get('order', UNDEFINED)
        cart_item_list = context.get('cart_item_list', UNDEFINED)
        rental = context.get('rental', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n\n\n\n\n\n\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        rental_return = context.get('rental_return', UNDEFINED)
        cart_product_list = context.get('cart_product_list', UNDEFINED)
        def content():
            return render_content(context)
        order = context.get('order', UNDEFINED)
        cart_item_list = context.get('cart_item_list', UNDEFINED)
        rental = context.get('rental', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\t<div id="thankyou"class="container col-md-12">\n    \t<h1>Thank You</h1>\n    \t<hr>\n\t</div>\n\n    <div class="container col-md-12">\n    <h3>Receipt for Payment</h3>\n')
        if cart_product_list:
            __M_writer('        <table id="shopping_cartTable" class="table table-hover">\n            <tr>\n                <th>Picture</th>\n                <th>Product</th>\n                <th>Quantity</th>\n                <th>Price</th>\n            </tr>\n')
            for product in cart_product_list:
                __M_writer('            <tr>\n                <td><img class="productImage" src="')
                __M_writer(str(product.photo.image))
                __M_writer('"></td>\n                <td>')
                __M_writer(str(product.name))
                __M_writer('</td>\n                <td>')
                __M_writer(str(product.qty))
                __M_writer('</td>\n                <td>$')
                __M_writer(str(product.collective_cost))
                __M_writer('</td>\n            </tr>\n')
            __M_writer('            <tr>\n                <td></td>\n                <td></td>\n                <td><h3>Total Cost:</h3></td>\n                <td><h3>$')
            __M_writer(str(order.totalCost))
            __M_writer('</h3></td>\n            </tr>\n        </table>\n')
        if cart_item_list:
            __M_writer('        <table id="shopping_cartTable" class="table table-hover">\n            <tr>\n                <th>Picture</th>\n                <th>Item</th>\n                <th>Quantity</th>\n                <th>Collective Cost / day</th>\n            </tr>\n')
            for item in cart_item_list:
                __M_writer('            <tr>\n                <td><img class="productImage" src="')
                __M_writer(str(item.photo.image))
                __M_writer('"></td>\n                <td>')
                __M_writer(str(item.name))
                __M_writer('</td>\n                <td>')
                __M_writer(str(item.qty))
                __M_writer('</td>\n                <td>$')
                __M_writer(str(item.collective_cost))
                __M_writer('</td>\n            </tr>\n')
            __M_writer('            <tr>\n                <td></td>\n                <td></td>\n                <td><h3>Total Cost:</h3></td>\n                <td><h3>$')
            __M_writer(str(rental.totalCost))
            __M_writer('</h3></td>\n            </tr>\n        </table>\n')
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
{"source_encoding": "ascii", "uri": "thankyou.html", "line_map": {"27": 0, "39": 1, "44": 69, "50": 3, "61": 3, "62": 12, "63": 13, "64": 20, "65": 21, "66": 22, "67": 22, "68": 23, "69": 23, "70": 24, "71": 24, "72": 25, "73": 25, "74": 28, "75": 32, "76": 32, "77": 36, "78": 37, "79": 44, "80": 45, "81": 46, "82": 46, "83": 47, "84": 47, "85": 48, "86": 48, "87": 49, "88": 49, "89": 52, "90": 56, "91": 56, "92": 60, "93": 61, "94": 61, "95": 61, "96": 63, "97": 63, "98": 65, "99": 65, "100": 67, "106": 100}, "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/thankyou.html"}
__M_END_METADATA
"""
