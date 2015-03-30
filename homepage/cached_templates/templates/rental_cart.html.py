# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427314538.950132
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/rental_cart.html'
_template_uri = 'rental_cart.html'
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
        itemList2 = context.get('itemList2', UNDEFINED)
        qty = context.get('qty', UNDEFINED)
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
        itemList2 = context.get('itemList2', UNDEFINED)
        qty = context.get('qty', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n   <div id="shopping_cart" class="container col-md-12" >\n      <div id="singleProduct" class="text-muted">\n      \t<table id="shopping_cartTable" class="table table-hover">\n\t      \t\n\t      \t<tr>\n\t      \t\t<th>Picture</th>\n\t      \t\t<th>Item</th>\n\t      \t\t<th>Price / day</th>\n\t      \t\t<th>Quantity</th>\n\t      \t\t<th>Remove</th>\n      \t\t</tr>\n')
        for item in itemList2:
            __M_writer('      \t\t<tr>\n      \t\t\t<td>[IMAGE]</td>\n            \t<td>')
            __M_writer(str(item.name))
            __M_writer('</td>\n            \t<td>$')
            __M_writer(str(item.STP))
            __M_writer('</td>\n            \t<td><input id=\'qty\' type="number" value="')
            __M_writer(str(qty))
            __M_writer('"></td>\n            \t<td><a data-pid="')
            __M_writer(str(item.id))
            __M_writer('" data-qty="')
            __M_writer(str(qty))
            __M_writer('" role="button" class="remove_product btn btn-danger glyphicon glyphicon-remove"></a></td>\n            </tr>\n')
        __M_writer('            \n        </table>\n')
        if not itemList2:
            __M_writer('        \t<h3 class="none" style:"text-align:center">No Items Selected</h3>\n')
        __M_writer('        <hr>\n')
        if request.user.is_authenticated():
            if itemList2:
                __M_writer('          \n            <a id="checkoutBtn" href="/homepage/rental_cart.check_login/')
                __M_writer(str(qty))
                __M_writer('" role="button" class="btn btn-success pull-right">Check Out</a>\n')
        else:
            __M_writer('          <div>\n            <span>You are not logged in. Please log in before continuing.</span>\n            <button role="button" class="btn btn-info pull-right show_login_dialog">Login</button>\n          </div>\n          <br>\n          <hr>\n          <div>\n            <span>If you do not yet have an account, please create one here!</span>\n            <a role="button" class="btn btn-primary pull-right" href="/homepage/users.userCreate">Create Account</a>\n          </div>\n')
        __M_writer('      </div>\n      \n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "rental_cart.html", "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/rental_cart.html", "line_map": {"64": 20, "65": 21, "66": 21, "67": 21, "68": 21, "69": 24, "70": 26, "71": 27, "72": 29, "73": 30, "74": 31, "75": 32, "76": 33, "77": 33, "78": 35, "79": 36, "80": 47, "86": 80, "27": 0, "37": 1, "47": 3, "56": 3, "57": 15, "58": 16, "59": 18, "60": 18, "61": 19, "62": 19, "63": 20}, "source_encoding": "ascii"}
__M_END_METADATA
"""
