# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427932848.902506
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
        order = context.get('order', UNDEFINED)
        item_list2 = context.get('item_list2', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        qty = context.get('qty', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        rental = context.get('rental', UNDEFINED)
        product_list2 = context.get('product_list2', UNDEFINED)
        form1 = context.get('form1', UNDEFINED)
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
        order = context.get('order', UNDEFINED)
        item_list2 = context.get('item_list2', UNDEFINED)
        def content():
            return render_content(context)
        qty = context.get('qty', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        rental = context.get('rental', UNDEFINED)
        product_list2 = context.get('product_list2', UNDEFINED)
        form1 = context.get('form1', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <h1>Checkout</h1>\n    <hr>\n    \n    <div class="container col-md-12">\n    <h3>Review Your Purchase</h3>\n')
        if product_list2:
            __M_writer('        <table id="shopping_cartTable" class="table table-hover">\n            <tr>\n                <th>Picture</th>\n                <th>Product</th>\n                <th>Quantity</th>\n                <th>Price</th>\n            </tr>\n')
            for product in product_list2:
                __M_writer('            <tr>\n                <td><img class="productImage" src="')
                __M_writer(str(STATIC_URL))
                __M_writer('homepage/media/CannonFinished.jpg"></td>\n                <td>')
                __M_writer(str(product.name))
                __M_writer('</td>\n                <td><input id=\'qty\' type="number" value="')
                __M_writer(str(qty))
                __M_writer('"></td>\n                <td>$')
                __M_writer(str(product.currentPrice))
                __M_writer('</td>\n            </tr>\n')
            __M_writer('            <tr>\n                <td></td>\n                <td></td>\n                <td><h3>Total Cost:</h3></td>\n                <td><h3>$')
            __M_writer(str(order.totalCost))
            __M_writer('</h3></td>\n            </tr>\n        </table>\n')
        if item_list2:
            __M_writer('        <table id="shopping_cartTable" class="table table-hover">\n            <tr>\n                <th>Picture</th>\n                <th>Item</th>\n                <th>Quantity</th>\n                <th>Condition</th>\n                <th>Price</th>\n            </tr>\n')
            for item in item_list2:
                __M_writer('            <tr>\n                <td><img class="productImage" src="')
                __M_writer(str(STATIC_URL))
                __M_writer('homepage/media/Glasses.jpg"></td>\n                <td>')
                __M_writer(str(item.name))
                __M_writer('</td>\n                <td><input id=\'qty\' type="number" value="')
                __M_writer(str(qty))
                __M_writer('"></td>\n                <td>')
                __M_writer(str(item.condition))
                __M_writer('</td>\n                <td>$')
                __M_writer(str(item.STP))
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
        if product_list2 or item_list2:
            __M_writer('    <div class=\'container col-md-4\'>\n        <form method="POST">\n            <div class="checkout">\n                <h3>Shipping/Payment Information</h3>\n                ')
            __M_writer(str(form))
            __M_writer('\n            </div>\n            <input class=\'btn btn-success\' type=\'submit\' value="Checkout">\n        </form>\n    </div>\n')
        __M_writer('    <div>\n        \n    </div>\n\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"27": 0, "43": 1, "48": 90, "54": 3, "69": 3, "70": 9, "71": 10, "72": 17, "73": 18, "74": 19, "75": 19, "76": 20, "77": 20, "78": 21, "79": 21, "80": 22, "81": 22, "82": 25, "83": 29, "84": 29, "85": 33, "86": 34, "87": 42, "88": 43, "89": 44, "90": 44, "91": 45, "92": 45, "93": 46, "94": 46, "95": 47, "96": 47, "97": 48, "98": 48, "99": 51, "100": 56, "101": 56, "102": 60, "103": 62, "104": 63, "105": 65, "106": 65, "107": 70, "108": 71, "109": 72, "110": 76, "111": 76, "112": 82, "118": 112}, "uri": "checkout.html", "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/checkout.html"}
__M_END_METADATA
"""
