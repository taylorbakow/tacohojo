# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554840029.111697
_enable_loop = True
_template_filename = 'C:/Users/Taylo/github/tacohojo/tacohojo/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
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
        dList = context.get('dList', UNDEFINED)
        formP = context.get('formP', UNDEFINED)
        formD = context.get('formD', UNDEFINED)
        objectType = context.get('objectType', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        pList = context.get('pList', UNDEFINED)
        ddList = context.get('ddList', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        dList = context.get('dList', UNDEFINED)
        formP = context.get('formP', UNDEFINED)
        formD = context.get('formD', UNDEFINED)
        objectType = context.get('objectType', UNDEFINED)
        def content():
            return render_content(context)
        self = context.get('self', UNDEFINED)
        pList = context.get('pList', UNDEFINED)
        ddList = context.get('ddList', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <p>CONTENT GOES HERE</p>\r\n        <div class="grid">\r\n            <form method="post">\r\n                <div class="row">\r\n                    <div class="col"> ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( formP ))
        __M_writer(' </div>\r\n                    <div class="col"> ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( formD ))
        __M_writer(' </div>\r\n                    <div class="col" style="margin-top: 33px;"><input style="width: 140px;" class="button is-dark" type="submit" value="Search"></div>\r\n                </div>\r\n            </form>\r\n')
        if objectType is not '':
            __M_writer('                <h1 class="title">Search Results:</h1>\r\n')
        __M_writer('            <div class="row">\r\n')
        if objectType == 'Prescriber' or objectType == 'Both':
            __M_writer('                    <div class="col">\r\n                        <table>\r\n                            <tr>\r\n                                <th>First Name</th>\r\n                                <th>Last Name</th>\r\n                            </tr>\r\n')
            for p in pList:
                __M_writer("                            <tr>\r\n                                <td><a href='/homepage/details/")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( p.id ))
                __M_writer("'>")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(p.Fname))
                __M_writer("</a></td>\r\n                                <td><a href='/homepage/details/")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( p.id ))
                __M_writer("'>")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(p.Lname))
                __M_writer('</a></td>\r\n                            </tr>\r\n')
            __M_writer('                        </table>\r\n                    </div>  \r\n')
        if objectType == 'Drug' or objectType == 'Both':
            __M_writer('                    <div class="col">\r\n                        <table>\r\n                            <tr>\r\n                                <th>Drug Name</th>\r\n                            </tr>\r\n')
            for d in dList:
                __M_writer("                            <tr>\r\n                                <td><a href='/homepage/details.drugdetail/")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( d.id ))
                __M_writer("'>")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(d.DrugName))
                __M_writer('</a></td>\r\n                            </tr>\r\n')
            __M_writer('                        </table>\r\n                    </div>\r\n')
        __M_writer('            </div>\r\n')
        if objectType == 'Both':
            __M_writer('                <br/>\r\n                <h1 class="title">Prescriber Stats:</h1>\r\n                <table>\r\n                    <tr>\r\n                        <th>Drug Name</th>\r\n                        <th>Prescriber</th>\r\n                        <th>Quantity</th>\r\n                    </tr>\r\n')
            for dd in ddList:
                __M_writer("                    <tr>\r\n                        <td><a href='/homepage/details.drugdetail/")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( dd.DrugID.id ))
                __M_writer("'>")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(dd.DrugID.DrugName))
                __M_writer("</a></td>\r\n                        <td><a href='/homepage/details/")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( dd.PrescriberID.id ))
                __M_writer("'>")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(dd.PrescriberID.Fname))
                __M_writer(' ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(dd.PrescriberID.Lname))
                __M_writer('</a></td>\r\n                        <td>')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(dd.QtyPrescribed))
                __M_writer('</td>         \r\n                    </tr>\r\n')
            __M_writer('                </table>\r\n')
        __M_writer('        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Taylo/github/tacohojo/tacohojo/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "43": 1, "48": 69, "54": 3, "67": 3, "68": 9, "69": 9, "70": 10, "71": 10, "72": 14, "73": 15, "74": 17, "75": 18, "76": 19, "77": 25, "78": 26, "79": 27, "80": 27, "81": 27, "82": 27, "83": 28, "84": 28, "85": 28, "86": 28, "87": 31, "88": 34, "89": 35, "90": 40, "91": 41, "92": 42, "93": 42, "94": 42, "95": 42, "96": 45, "97": 48, "98": 49, "99": 50, "100": 58, "101": 59, "102": 60, "103": 60, "104": 60, "105": 60, "106": 61, "107": 61, "108": 61, "109": 61, "110": 61, "111": 61, "112": 62, "113": 62, "114": 65, "115": 67, "121": 115}}
__M_END_METADATA
"""
