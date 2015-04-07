# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428439908.368496
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
        cart_product_list = context.get('cart_product_list', UNDEFINED)
        order = context.get('order', UNDEFINED)
        rental = context.get('rental', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        cart_item_list = context.get('cart_item_list', UNDEFINED)
        rental_return = context.get('rental_return', UNDEFINED)
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
        cart_product_list = context.get('cart_product_list', UNDEFINED)
        order = context.get('order', UNDEFINED)
        rental = context.get('rental', UNDEFINED)
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        cart_item_list = context.get('cart_item_list', UNDEFINED)
        rental_return = context.get('rental_return', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\t<div id="thankyou"class="container col-md-12">\n    \t<h1>Thank You</h1>\n    \t<hr>\n\t</div>\n\n    <div class="container col-md-12">\n    <h3>Receipt for Payment</h3>\n')
        if cart_product_list:
            __M_writer('        <table id="shopping_cartTable" class="table table-hover">\n            <tr>\n                <th>Picture</th>\n                <th>Product</th>\n                <th>Quantity</th>\n                <th>Price</th>\n            </tr>\n')
            for product in cart_product_list:
                __M_writer('            <tr>\n                <td><img class="productImage" src="')
                __M_writer(str(STATIC_URL))
                __M_writer('homepage/media/CannonFinished.jpg"></td>\n                <td>')
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
                __M_writer(str(STATIC_URL))
                __M_writer('homepage/media/Glasses.jpg"></td>\n                <td>')
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
{"filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/thankyou.html", "line_map": {"27": 0, "40": 1, "45": 69, "51": 3, "63": 3, "64": 12, "65": 13, "66": 20, "67": 21, "68": 22, "69": 22, "70": 23, "71": 23, "72": 24, "73": 24, "74": 25, "75": 25, "76": 28, "77": 32, "78": 32, "79": 36, "80": 37, "81": 44, "82": 45, "83": 46, "84": 46, "85": 47, "86": 47, "87": 48, "88": 48, "89": 49, "90": 49, "91": 52, "92": 56, "93": 56, "94": 60, "95": 61, "96": 61, "97": 61, "98": 63, "99": 63, "100": 65, "101": 65, "102": 67, "108": 102}, "source_encoding": "ascii", "uri": "thankyou.html"}
__M_END_METADATA
"""
