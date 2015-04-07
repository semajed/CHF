# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428448343.197212
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/shopping_cart.html'
_template_uri = 'shopping_cart.html'
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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        cart_product_list = context.get('cart_product_list', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        request = context.get('request', UNDEFINED)
        cart_product_list = context.get('cart_product_list', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n   <div id="shopping_cart" class="container col-md-12" >\n      <div id="singleProduct" class="text-muted">\n      \t<table id="shopping_cartTable" class="table table-hover">\n\t      \t\n\t      \t<tr>\n\t      \t\t<th>Picture</th>\n\t      \t\t<th>Product</th>\n\t      \t\t<th>Price</th>\n\t      \t\t<th>Quantity</th>\n\t      \t\t<th>Remove</th>\n      \t\t</tr>\n\n')
        for product in cart_product_list:
            __M_writer('      \t\t<tr>\n      \t\t\t<td><img src="')
            __M_writer(str(product.photo.image))
            __M_writer('"></td>\n            \t<td>')
            __M_writer(str(product.name))
            __M_writer('</td>\n            \t<td>$')
            __M_writer(str(product.currentPrice))
            __M_writer('</td>\n            \t<td>\n              <input id=\'qty\' type="number" value="')
            __M_writer(str(product.qty))
            __M_writer('">\n\n              </td>\n            \t<td><a data-pid="')
            __M_writer(str(product.id))
            __M_writer('" data-qty="')
            __M_writer(str(product.qty))
            __M_writer('" role="button" class="remove_product btn btn-danger glyphicon glyphicon-remove"></a></td>\n          </tr>\n')
        __M_writer('            \n        </table>\n')
        if not cart_product_list:
            __M_writer('        \t<h3 class="none" style:"text-align:center">No Products Selected</h3>\n')
        __M_writer('        <hr>\n')
        if request.user.is_authenticated():
            if cart_product_list:
                __M_writer('          \n          \t<a id="checkoutBtn" href="/homepage/shopping_cart.check_login/" role="button" class="btn btn-success pull-right">Check Out</a>\n')
        else:
            __M_writer('          <div>\n            <span>You are not logged in. Please log in before continuing.</span>\n            <button role="button" class="btn btn-info pull-right show_login_dialog">Login</button>\n          </div>\n          <br>\n          <hr>\n          <div>\n            <span>If you do not yet have an account, please create one here!</span>\n            <a role="button" class="btn btn-primary pull-right" href="/homepage/users.userCreate">Create Account</a>\n          </div>\n')
        __M_writer('      </div>\n      \n    </div>\n\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 22, "65": 25, "66": 25, "67": 25, "68": 25, "69": 28, "70": 30, "71": 31, "72": 33, "73": 34, "74": 35, "75": 36, "76": 39, "77": 40, "78": 51, "84": 78, "27": 0, "36": 1, "46": 3, "54": 3, "55": 16, "56": 17, "57": 18, "58": 18, "59": 19, "60": 19, "61": 20, "62": 20, "63": 22}, "uri": "shopping_cart.html", "source_encoding": "ascii", "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/shopping_cart.html"}
__M_END_METADATA
"""
