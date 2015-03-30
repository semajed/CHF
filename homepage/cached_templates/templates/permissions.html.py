# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425626299.851653
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/permissions.html'
_template_uri = 'permissions.html'
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
        users = context.get('users', UNDEFINED)
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
        users = context.get('users', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <h1>Permissions Management</h1>\n    <hr>\n    <div class="container col-md-9">\n      <table id="roleTable" class="table table-hover">\n        <tr >\n          <th>Username</th>\n          <th>First Name</th>\n          <th>Last Name</th>\n          <th>Admin</th>\n          <th>Manager</th>\n          <th>User</th>\n          <th>Action</th>\n        </tr>\n')
        for user in users:
            __M_writer('        <tr>\n          <td>')
            __M_writer(str(user.username))
            __M_writer('</td>\n          <td>')
            __M_writer(str(user.first_name))
            __M_writer('</td>\n          <td>')
            __M_writer(str(user.last_name))
            __M_writer('</td>\n')
            if user.is_superuser == False:
                __M_writer('            <td><span class="glyphicon glyphicon-remove"></span></td>\n')
            elif user.is_superuser == True:
                __M_writer('            <td><span class="glyphicon glyphicon-ok"></span></td>\n')
            if user.groups == True:
                __M_writer('            <td><span class="glyphicon glyphicon-ok"></span></td>\n')
            elif user.is_staff == True:
                __M_writer('            <td><span class="glyphicon glyphicon-ok"></span></td>\n')
            elif user.is_staff == False & user.is_superuser == False:
                __M_writer('            <td><span class="glyphicon glyphicon-remove"></span></td>\n')
            __M_writer('          <td><span class="glyphicon glyphicon-ok"></span></td>\n          <td>\n          <a class=\'btn btn-xl btn-primary\' href="/homepage/permissions.edit/')
            __M_writer(str(user.id))
            __M_writer('/">EDIT</a>\n          </td>\n        </tr>\n')
        __M_writer('      </table>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 25, "65": 27, "66": 28, "67": 29, "68": 30, "69": 31, "70": 32, "71": 34, "72": 36, "73": 36, "74": 40, "80": 74, "27": 0, "35": 1, "45": 3, "52": 3, "53": 17, "54": 18, "55": 19, "56": 19, "57": 20, "58": 20, "59": 21, "60": 21, "61": 22, "62": 23, "63": 24}, "source_encoding": "ascii", "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/permissions.html", "uri": "permissions.html"}
__M_END_METADATA
"""
