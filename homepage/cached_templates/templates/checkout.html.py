# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428447818.582754
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/checkout.html'
_template_uri = 'checkout.html'
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
        form = context.get('form', UNDEFINED)
        rental_return = context.get('rental_return', UNDEFINED)
        cart_product_list = context.get('cart_product_list', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        order = context.get('order', UNDEFINED)
        cart_item_list = context.get('cart_item_list', UNDEFINED)
        form1 = context.get('form1', UNDEFINED)
        rental = context.get('rental', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<title>Checkout</title>\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        rental_return = context.get('rental_return', UNDEFINED)
        cart_product_list = context.get('cart_product_list', UNDEFINED)
        def content():
            return render_content(context)
        order = context.get('order', UNDEFINED)
        cart_item_list = context.get('cart_item_list', UNDEFINED)
        form1 = context.get('form1', UNDEFINED)
        rental = context.get('rental', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <h1>Checkout</h1>\n    <hr>\n    \n    <div class="container col-md-12">\n    <h3>Review Your Purchase</h3>\n')
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
            __M_writer('        <table id="shopping_cartTable" class="table table-hover">\n            <tr>\n                <th>Picture</th>\n                <th>Item</th>\n                <th>Quantity</th>\n                <th>Condition</th>\n                <th>Price</th>\n            </tr>\n')
            for item in cart_item_list:
                __M_writer('            <tr>\n                <td><img class="productImage" src="')
                __M_writer(str(item.photo.image))
                __M_writer('"></td>\n                <td>')
                __M_writer(str(item.name))
                __M_writer('</td>\n                <td>')
                __M_writer(str(item.qty))
                __M_writer('</td>\n                <td>')
                __M_writer(str(item.condition))
                __M_writer('</td>\n                <td>$')
                __M_writer(str(item.collective_cost))
                __M_writer('</td>\n            </tr>\n')
            __M_writer('            <tr>\n                <td></td>\n                <td></td>\n                <td></td>\n                <td><h3>Total Cost:</h3></td>\n                <td><h3>$')
            __M_writer(str(rental.totalCost))
            __M_writer('</h3></td>\n            </tr>\n        </table>\n')
        __M_writer('    </div>\n\n')
        if rental_return:
            __M_writer('        <div class="col-md-4">\n            <form method=\'POST\'>\n                ')
            __M_writer(str(form1))
            __M_writer('\n                <input class=\'btn btn-success\' type=\'submit\' value="Make Payment">\n            </form>\n        </div>\n')
        __M_writer('\n')
        if cart_product_list or cart_item_list:
            __M_writer('    <div class=\'container col-md-4\'>\n        <form method="POST">\n            <div class="checkout">\n                <h3>Shipping/Payment Information</h3>\n                ')
            __M_writer(str(form))
            __M_writer('\n            </div>\n            <input class=\'btn btn-success\' type=\'submit\' value="Checkout">\n        </form>\n    </div>\n')
        __M_writer('    <div>\n        \n    </div>\n\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "checkout.html", "line_map": {"27": 0, "41": 1, "46": 90, "52": 3, "65": 3, "66": 9, "67": 10, "68": 17, "69": 18, "70": 19, "71": 19, "72": 20, "73": 20, "74": 21, "75": 21, "76": 22, "77": 22, "78": 25, "79": 29, "80": 29, "81": 33, "82": 34, "83": 42, "84": 43, "85": 44, "86": 44, "87": 45, "88": 45, "89": 46, "90": 46, "91": 47, "92": 47, "93": 48, "94": 48, "95": 51, "96": 56, "97": 56, "98": 60, "99": 62, "100": 63, "101": 65, "102": 65, "103": 70, "104": 71, "105": 72, "106": 76, "107": 76, "108": 82, "114": 108}, "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/checkout.html"}
__M_END_METADATA
"""
