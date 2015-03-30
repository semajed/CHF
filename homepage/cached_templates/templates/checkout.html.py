# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427564118.25611
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
        item_list2 = context.get('item_list2', UNDEFINED)
        product_list2 = context.get('product_list2', UNDEFINED)
        form = context.get('form', UNDEFINED)
        qty = context.get('qty', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        item_list2 = context.get('item_list2', UNDEFINED)
        product_list2 = context.get('product_list2', UNDEFINED)
        form = context.get('form', UNDEFINED)
        qty = context.get('qty', UNDEFINED)
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <h1>Checkout</h1>\n    <hr>\n    \n    <div class="container col-md-12">\n    <h3>Review Your Purchase</h3>\n')
        if product_list2:
            __M_writer('        <table id="shopping_cartTable" class="table table-hover">\n            <tr>\n                <th>Picture</th>\n                <th>Product</th>\n                <th>Price</th>\n                <th>Quantity</th>\n            </tr>\n')
            for product in product_list2:
                __M_writer('            <tr>\n                <td><img class="productImage" src="')
                __M_writer(str(STATIC_URL))
                __M_writer('homepage/media/CannonFinished.jpg"></td>\n                <td>')
                __M_writer(str(product.name))
                __M_writer('</td>\n                <td>$')
                __M_writer(str(product.currentPrice))
                __M_writer('</td>\n                <td><input id=\'qty\' type="number" value="')
                __M_writer(str(qty))
                __M_writer('"></td>\n            </tr>\n')
            __M_writer('        </table>\n')
        if item_list2:
            __M_writer('        <table id="shopping_cartTable" class="table table-hover">\n            <tr>\n                <th>Picture</th>\n                <th>Item</th>\n                <th>Price / day</th>\n                <th>Quantity</th>\n                <th>Condition</th>\n            </tr>\n')
            for item in item_list2:
                __M_writer('            <tr>\n                <td><img class="productImage" src="')
                __M_writer(str(STATIC_URL))
                __M_writer('homepage/media/Glasses.jpg"></td>\n                <td>')
                __M_writer(str(item.name))
                __M_writer('</td>\n                <td>$')
                __M_writer(str(item.STP))
                __M_writer('</td>\n                <td><input id=\'qty\' type="number" value="')
                __M_writer(str(qty))
                __M_writer('"></td>\n                <td>')
                __M_writer(str(item.condition))
                __M_writer('</td>\n            </tr>\n')
            __M_writer('        </table>\n')
        __M_writer('    </div>\n\n\n    <div class=\'container col-md-4\'>\n        \n        <form method="POST">\n            <div class="checkout">\n                <h3>Shipping/Payment Information</h3>\n                ')
        __M_writer(str(form))
        __M_writer('\n            </div>\n\n            <input class=\'btn btn-success\' type=\'submit\' value="Checkout">\n        </form>\n    </div>\n    <div>\n        \n    </div>\n\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/checkout.html", "uri": "checkout.html", "line_map": {"64": 17, "65": 18, "66": 19, "67": 19, "68": 20, "69": 20, "70": 21, "71": 21, "72": 22, "73": 22, "74": 25, "75": 27, "76": 28, "77": 36, "78": 37, "79": 38, "80": 38, "81": 39, "82": 39, "83": 40, "84": 40, "85": 41, "86": 41, "87": 42, "88": 42, "89": 45, "90": 47, "27": 0, "92": 55, "98": 92, "91": 55, "39": 1, "44": 69, "50": 3, "61": 3, "62": 9, "63": 10}}
__M_END_METADATA
"""
