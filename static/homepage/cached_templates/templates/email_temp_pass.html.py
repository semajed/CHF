# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428003653.314967
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/email_temp_pass.html'
_template_uri = 'email_temp_pass.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n\t<div id="thankyou"class="container col-md-12">\n    \t<h1>Reset Your Password</h1>\n    \t<hr>\n        <h2>Dear ')
        __M_writer(str(user.get_full_name()))
        __M_writer(',</h2>\n        <p>This link will lead you to a page for you to enter your given security code.\n        Enter the security code to get to the page to change your password.</p>\n        <h3>Link to change password:</h3>\n        <div><a href="http://localhost:8000/homepage/accountSecurity.check_security_code/')
        __M_writer(str(user.id))
        __M_writer('/">Change Password</a></div>\n        <h3>Security Code:</h3>\n        <div>')
        __M_writer(str(user.forgot_password_code))
        __M_writer('</div>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/email_temp_pass.html", "line_map": {"16": 0, "34": 1, "53": 47, "47": 12, "41": 1, "42": 6, "43": 6, "28": 15, "45": 10, "46": 12, "44": 10}, "uri": "email_temp_pass.html"}
__M_END_METADATA
"""
