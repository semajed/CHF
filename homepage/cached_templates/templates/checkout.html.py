# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428438173.013217
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        rental_return = context.get('rental_return', UNDEFINED)
        cart_item_list = context.get('cart_item_list', UNDEFINED)
        form1 = context.get('form1', UNDEFINED)
        cart_product_list = context.get('cart_product_list', UNDEFINED)
        rental = context.get('rental', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        order = context.get('order', UNDEFINED)
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        rental_return = context.get('rental_return', UNDEFINED)
        cart_item_list = context.get('cart_item_list', UNDEFINED)
        form1 = context.get('form1', UNDEFINED)
        cart_product_list = context.get('cart_product_list', UNDEFINED)
        rental = context.get('rental', UNDEFINED)
        def content():
            return render_content(context)
        order = context.get('order', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <h1>Checkout</h1>\n    <hr>\n    \n    <div class="container col-md-12">\n    <h3>Review Your Purchase</h3>\n')
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
            __M_writer('        <table id="shopping_cartTable" class="table table-hover">\n            <tr>\n                <th>Picture</th>\n                <th>Item</th>\n                <th>Quantity</th>\n                <th>Condition</th>\n                <th>Price</th>\n            </tr>\n')
            for item in cart_item_list:
                __M_writer('            <tr>\n                <td><img class="productImage" src="')
                __M_writer(str(STATIC_URL))
                __M_writer('homepage/media/Glasses.jpg"></td>\n                <td>')
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
{"filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/checkout.html", "line_map": {"27": 0, "42": 1, "47": 90, "53": 3, "67": 3, "68": 9, "69": 10, "70": 17, "71": 18, "72": 19, "73": 19, "74": 20, "75": 20, "76": 21, "77": 21, "78": 22, "79": 22, "80": 25, "81": 29, "82": 29, "83": 33, "84": 34, "85": 42, "86": 43, "87": 44, "88": 44, "89": 45, "90": 45, "91": 46, "92": 46, "93": 47, "94": 47, "95": 48, "96": 48, "97": 51, "98": 56, "99": 56, "100": 60, "101": 62, "102": 63, "103": 65, "104": 65, "105": 70, "106": 71, "107": 72, "108": 76, "109": 76, "110": 82, "116": 110}, "uri": "checkout.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
