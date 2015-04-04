# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428018630.015962
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/rentals.html'
_template_uri = 'rentals.html'
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
        thirty_to_sixty = context.get('thirty_to_sixty', UNDEFINED)
        lates = context.get('lates', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        rentals = context.get('rentals', UNDEFINED)
        sixty_to_ninety = context.get('sixty_to_ninety', UNDEFINED)
        ninety_plus = context.get('ninety_plus', UNDEFINED)
        today_to_thirty = context.get('today_to_thirty', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        thirty_to_sixty = context.get('thirty_to_sixty', UNDEFINED)
        lates = context.get('lates', UNDEFINED)
        def content():
            return render_content(context)
        rentals = context.get('rentals', UNDEFINED)
        sixty_to_ninety = context.get('sixty_to_ninety', UNDEFINED)
        ninety_plus = context.get('ninety_plus', UNDEFINED)
        today_to_thirty = context.get('today_to_thirty', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <h1>Rentals Management\n  <a role="button" class=\'btn btn-xl btn-danger pull-right filter_button\' href="/homepage/rentals.late/">View all over-due rentals</a>\n  <a role="button"class=\'btn btn-xl btn-info pull-right filter_button\' href="/homepage/rentals/">View all rentals</a>\n  <span id="filter_text"class="pull-right">Filter Rentals:</span>\n  </h1>\n  <hr>\n')
        if lates == True:
            __M_writer('  <a role="button" class=\'btn btn-xl btn-success filter_button\' href="/homepage/rentals.send_email/">Email Late Notices</a>\n')
        __M_writer('\n')
        if rentals:
            __M_writer('    <div class="container col-md-12">\n      <table id="roleTable" class="table table-hover">\n        <tr >\n          <th>Name</th>\n          <th>Rental Date</th>\n          <th>Due Date</th>\n          <th>Handling Agent</th>\n          <th>Edit Rental</th>\n          <th>Return Rental</th>\n        </tr>\n')
            for rental in rentals:
                __M_writer('        <tr>\n          <td>')
                __M_writer(str(rental.memberName))
                __M_writer('</td>\n          <td>')
                __M_writer(str(rental.rentalTime.strftime('%m/%d/%Y')))
                __M_writer('</td>\n          <td>')
                __M_writer(str(rental.dueDate.strftime('%m/%d/%Y')))
                __M_writer('</td>\n          <td>')
                __M_writer(str(rental.handlingAgent))
                __M_writer('</td>\n          <td>\n          <a class=\'btn btn-xl btn-primary\' href="/homepage/rentals.edit/')
                __M_writer(str(rental.id))
                __M_writer('/">EDIT</a>\n          </td>\n          <td>\n          <a class=\'btn btn-xl btn-warning\' href="/homepage/rentals.rental_return/')
                __M_writer(str(rental.id))
                __M_writer('/">RETURN</a>\n          </td>\n        </tr>\n')
            __M_writer('      </table>\n    </div>\n')
        __M_writer('\n')
        if today_to_thirty:
            __M_writer('    <div class="container col-md-12">\n    <h2>Today to 30 Days</h2>\n      <table id="roleTable" class="table table-hover">\n        <tr >\n          <th>Name</th>\n          <th>Rental Date</th>\n          <th>Due Date</th>\n          <th>Handling Agent</th>\n          <th>Edit Rental</th>\n          <th>Return Rental</th>\n        </tr>\n')
            for rental in today_to_thirty:
                __M_writer('        <tr>\n          <td>')
                __M_writer(str(rental.memberName))
                __M_writer('</td>\n          <td>')
                __M_writer(str(rental.rentalTime.strftime('%m/%d/%Y')))
                __M_writer('</td>\n          <td>')
                __M_writer(str(rental.dueDate.strftime('%m/%d/%Y')))
                __M_writer('</td>\n          <td>')
                __M_writer(str(rental.handlingAgent))
                __M_writer('</td>\n          <td>\n          <a class=\'btn btn-xl btn-primary\' href="/homepage/rentals.edit/')
                __M_writer(str(rental.id))
                __M_writer('/">EDIT</a>\n          </td>\n          <td>\n          <a class=\'btn btn-xl btn-warning\' href="/homepage/rentals.rental_return/')
                __M_writer(str(rental.id))
                __M_writer('/">RETURN</a>\n          </td>\n        </tr>\n')
            __M_writer('      </table>\n    </div>\n')
        __M_writer('\n')
        if thirty_to_sixty:
            __M_writer('    <div class="container col-md-12">\n    <h2>Between 30 and 60 Days</h2>\n      <table id="roleTable" class="table table-hover">\n        <tr >\n          <th>Name</th>\n          <th>Rental Date</th>\n          <th>Due Date</th>\n          <th>Handling Agent</th>\n          <th>Edit Rental</th>\n          <th>Return Rental</th>\n        </tr>\n')
            for rental in thirty_to_sixty:
                __M_writer('        <tr>\n          <td>')
                __M_writer(str(rental.memberName))
                __M_writer('</td>\n          <td>')
                __M_writer(str(rental.rentalTime.strftime('%m/%d/%Y')))
                __M_writer('</td>\n          <td>')
                __M_writer(str(rental.dueDate.strftime('%m/%d/%Y')))
                __M_writer('</td>\n          <td>')
                __M_writer(str(rental.handlingAgent))
                __M_writer('</td>\n          <td>\n          <a class=\'btn btn-xl btn-primary\' href="/homepage/rentals.edit/')
                __M_writer(str(rental.id))
                __M_writer('/">EDIT</a>\n          </td>\n          <td>\n          <a class=\'btn btn-xl btn-warning\' href="/homepage/rentals.rental_return/')
                __M_writer(str(rental.id))
                __M_writer('/">RETURN</a>\n          </td>\n        </tr>\n')
            __M_writer('      </table>\n    </div>\n')
        __M_writer('\n')
        if sixty_to_ninety:
            __M_writer('    <div class="container col-md-12">\n    <h2>Between 30 and 60 Days</h2>\n      <table id="roleTable" class="table table-hover">\n        <tr >\n          <th>Name</th>\n          <th>Rental Date</th>\n          <th>Due Date</th>\n          <th>Handling Agent</th>\n          <th>Edit Rental</th>\n          <th>Return Rental</th>\n        </tr>\n')
            for rental in sixty_to_ninety:
                __M_writer('        <tr>\n          <td>')
                __M_writer(str(rental.memberName))
                __M_writer('</td>\n          <td>')
                __M_writer(str(rental.rentalTime.strftime('%m/%d/%Y')))
                __M_writer('</td>\n          <td>')
                __M_writer(str(rental.dueDate.strftime('%m/%d/%Y')))
                __M_writer('</td>\n          <td>')
                __M_writer(str(rental.handlingAgent))
                __M_writer('</td>\n          <td>\n          <a class=\'btn btn-xl btn-primary\' href="/homepage/rentals.edit/')
                __M_writer(str(rental.id))
                __M_writer('/">EDIT</a>\n          </td>\n          <td>\n          <a class=\'btn btn-xl btn-warning\' href="/homepage/rentals.rental_return/')
                __M_writer(str(rental.id))
                __M_writer('/">RETURN</a>\n          </td>\n        </tr>\n')
            __M_writer('      </table>\n    </div>\n')
        __M_writer('\n')
        if ninety_plus:
            __M_writer('    <div class="container col-md-12">\n    <h2>90+ Days</h2>\n      <table id="roleTable" class="table table-hover">\n        <tr >\n          <th>Name</th>\n          <th>Rental Date</th>\n          <th>Due Date</th>\n          <th>Handling Agent</th>\n          <th>Edit Rental</th>\n          <th>Return Rental</th>\n        </tr>\n')
            for rental in ninety_plus:
                __M_writer('        <tr>\n          <td>')
                __M_writer(str(rental.memberName))
                __M_writer('</td>\n          <td>')
                __M_writer(str(rental.rentalTime.strftime('%m/%d/%Y')))
                __M_writer('</td>\n          <td>')
                __M_writer(str(rental.dueDate.strftime('%m/%d/%Y')))
                __M_writer('</td>\n          <td>')
                __M_writer(str(rental.handlingAgent))
                __M_writer('</td>\n          <td>\n          <a class=\'btn btn-xl btn-primary\' href="/homepage/rentals.edit/')
                __M_writer(str(rental.id))
                __M_writer('/">EDIT</a>\n          </td>\n          <td>\n          <a class=\'btn btn-xl btn-warning\' href="/homepage/rentals.rental_return/')
                __M_writer(str(rental.id))
                __M_writer('/">RETURN</a>\n          </td>\n        </tr>\n')
            __M_writer('      </table>\n    </div>\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/rentals.html", "uri": "rentals.html", "source_encoding": "ascii", "line_map": {"27": 0, "40": 1, "45": 163, "51": 3, "63": 3, "64": 10, "65": 11, "66": 13, "67": 14, "68": 15, "69": 25, "70": 26, "71": 27, "72": 27, "73": 28, "74": 28, "75": 29, "76": 29, "77": 30, "78": 30, "79": 32, "80": 32, "81": 35, "82": 35, "83": 39, "84": 42, "85": 43, "86": 44, "87": 55, "88": 56, "89": 57, "90": 57, "91": 58, "92": 58, "93": 59, "94": 59, "95": 60, "96": 60, "97": 62, "98": 62, "99": 65, "100": 65, "101": 69, "102": 72, "103": 73, "104": 74, "105": 85, "106": 86, "107": 87, "108": 87, "109": 88, "110": 88, "111": 89, "112": 89, "113": 90, "114": 90, "115": 92, "116": 92, "117": 95, "118": 95, "119": 99, "120": 102, "121": 103, "122": 104, "123": 115, "124": 116, "125": 117, "126": 117, "127": 118, "128": 118, "129": 119, "130": 119, "131": 120, "132": 120, "133": 122, "134": 122, "135": 125, "136": 125, "137": 129, "138": 132, "139": 133, "140": 134, "141": 145, "142": 146, "143": 147, "144": 147, "145": 148, "146": 148, "147": 149, "148": 149, "149": 150, "150": 150, "151": 152, "152": 152, "153": 155, "154": 155, "155": 159, "156": 162, "162": 156}}
__M_END_METADATA
"""
