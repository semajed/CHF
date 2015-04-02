# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428006823.102587
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/accountSecurity.forgot.html'
_template_uri = 'accountSecurity.forgot.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n<!DOCTYPE html>\n<html>  \n\n<head>\n    <title>Reset Password</title>\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\n    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\n    <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.3.1/js/bootstrap-datepicker.js">\n    </script>\n</head>\n\n\n<body>\n\n    <div class="container">\n        <form method=\'POST\'>\n        <h2>Account Security Information:</h2>\n        <div><span class="label label-danger">Important:</span>   You will need to log back in after changing your password.</div>\n        <hr>\n        <div>\n            \n        </div>\n            <div class="container" id="addressForm">\n                <table>\n                    ')
        __M_writer(str(form))
        __M_writer('\n                </table>\n            </div>\n            <button class=\'btn btn-xl btn-primary\' type="submit">Submit</button>\n        </form>\n\n    </div>\n\n</body>\n\n\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/accountSecurity.forgot.html", "line_map": {"16": 0, "33": 1, "48": 42, "40": 1, "41": 28, "42": 28}, "uri": "accountSecurity.forgot.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
