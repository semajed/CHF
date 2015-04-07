# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428447447.280153
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/account.html'
_template_uri = 'account.html'
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
        address = context.get('address', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n{% loadstaticfiles %}\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        address = context.get('address', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <h1>Hello, ')
        __M_writer(str(user.get_full_name()))
        __M_writer('</h1>\n    <hr>  \n    <div class="row">\n     <div class="panel-body">\n        <div class="row">\n          <div class="col-md-3 col-lg-3 " align="center"> \n            <br>\n                <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/profilepictures/jimmydean.jpg" width="200px" class="img-circle">\n            <br>\n            <br>\n            <a class="btn btn-success" href="/homepage/users.edit/')
        __M_writer(str(user.id))
        __M_writer('/" role="button">Edit Profile</a>\n          </div>\n\n        <div>\n        <h4>Personal Information</h4>\n        </div>\n        <br>\n        <div class="col-md-9">\n          <div class=" col-md-9 col-lg-9 "> \n                  <table class="table">\n                    <tbody>\n                      <tr>\n                        <td>Username:</td>\n                        <td>')
        __M_writer(str(user.username))
        __M_writer('</td>\n                      </tr>\n                      <tr>\n                        <td>Name:</td>\n                        <td>')
        __M_writer(str(user.get_full_name()))
        __M_writer('</td>\n                      </tr>\n                      <tr>\n                        <td>Email</td>\n                        <td><a href="mailto:info@support.com">')
        __M_writer(str(user.email))
        __M_writer('</a></td>\n                      </tr>\n                      <tr>\n                        <td>Phone Number:</td>\n                        <td>')
        __M_writer(str(user.phoneNumber))
        __M_writer('</td>\n                      </tr>\n                        <tr>\n                        <td>Address 1:</td>\n                        <td>')
        __M_writer(str(address.street1))
        __M_writer('</td>\n                      </tr>\n                      </tr>\n                      <tr>\n                        <td>Address 2:</td>\n                        <td>')
        __M_writer(str(address.street2))
        __M_writer('</td>\n                      </tr>\n                      <tr>\n                        <td>City:</td>\n                        <td>')
        __M_writer(str(address.city))
        __M_writer('</td>\n                      </tr>\n                      <tr>\n                        <td>State:</td>\n                        <td>')
        __M_writer(str(address.state))
        __M_writer('</td>\n                      </tr>\n                      <tr>\n                        <td>ZIP:</td>\n                        <td>')
        __M_writer(str(address.ZIP))
        __M_writer('</td>\n                      </tr>\n                  </tbody>\n                </table>\n                <hr>\n                <h4>Biographical Sketch:</h4><br><span>')
        __M_writer(str(user.biographicalSketch))
        __M_writer('</span>\n            </div><!-- /.col-lg-9 -->\n            \n          </div><!-- /.col-md-9 -->\n\n        </div><!-- /.row2 -->\n\n      </div><!-- /.panel -->\n    </div><!-- /.row -->\n \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "account.html", "line_map": {"64": 29, "65": 33, "66": 33, "67": 37, "68": 37, "69": 41, "70": 41, "71": 45, "72": 45, "73": 50, "74": 50, "75": 54, "76": 54, "77": 58, "78": 58, "79": 62, "80": 62, "81": 67, "82": 67, "88": 82, "27": 0, "37": 1, "47": 5, "56": 5, "57": 6, "58": 6, "59": 13, "60": 13, "61": 16, "62": 16, "63": 29}, "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/account.html"}
__M_END_METADATA
"""
