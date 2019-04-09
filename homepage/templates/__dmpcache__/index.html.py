# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554837876.0070417
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
        self = context.get('self', UNDEFINED)
        pList = context.get('pList', UNDEFINED)
        ddList = context.get('ddList', UNDEFINED)
        objectType = context.get('objectType', UNDEFINED)
        formP = context.get('formP', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        formD = context.get('formD', UNDEFINED)
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
        self = context.get('self', UNDEFINED)
        pList = context.get('pList', UNDEFINED)
        ddList = context.get('ddList', UNDEFINED)
        objectType = context.get('objectType', UNDEFINED)
        formP = context.get('formP', UNDEFINED)
        def content():
            return render_content(context)
        formD = context.get('formD', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <p>CONTENT GOES HERE</p>\r\n        <div class="grid">\r\n            <form method="post">\r\n                <div class="row">\r\n                    <div class="col"> ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( formP ))
        __M_writer(' </div>\r\n                    <div class="col"> ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( formD ))
        __M_writer(' </div>\r\n                    <div class="col" style="margin-top: 35px;"> <input type="submit" value="Search"></div>\r\n                </div>\r\n            </form>\r\n            <div class="row">\r\n')
        if objectType == 'Prescriber':
            __M_writer('                    <ul>\r\n')
            for p in pList:
                __M_writer("                        <li><a href='/homepage/details/")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( p.id ))
                __M_writer("'>")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(p.Fname))
                __M_writer('  ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(p.Lname))
                __M_writer('</a</li>\r\n')
            __M_writer('                    </ul>\r\n')
        if objectType == 'Drug':
            __M_writer('                    <ul>\r\n')
            for d in dList:
                __M_writer("                        <li><a href='/homepage/details.drugdetail/")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( d.id ))
                __M_writer("'>")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(d.DrugName))
                __M_writer('</a></li>\r\n')
            __M_writer('                    </ul>\r\n')
        __M_writer('            </div>\r\n')
        if objectType == 'Both':
            __M_writer('                <ul>\r\n')
            for p in pList:
                __M_writer("                    <li><a href='/homepage/details.drugdetail/")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( p.id ))
                __M_writer("'>")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(p.Fname))
                __M_writer('  ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(p.Lname))
                __M_writer('</a></li>\r\n')
            __M_writer('                </ul>\r\n                <ul>\r\n')
            for d in dList:
                __M_writer("                    <li><a href='/homepage/details.drugdetail/")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( d.id ))
                __M_writer("'>")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(d.DrugName))
                __M_writer('</a></li>\r\n')
            __M_writer('                </ul>\r\n                <table>\r\n                    <tr>\r\n                        <th>Drug Name</th>\r\n                        <th>Prescriber</th>\r\n                        <th>Quantity</th>\r\n                    </tr>\r\n')
            for dd in ddList:
                __M_writer("                    <tr>\r\n                        <td><a href='/homepage/details.drugdetail/")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( dd.DrugID ))
                __M_writer("'>")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(dd.DrugID.DrugName))
                __M_writer("</a></td>\r\n                        <td><a href='/homepage/details.drugdetail/")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( dd.PrescriberID ))
                __M_writer("'></a>")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(dd.PrescriberID.Fname))
                __M_writer(' ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(dd.PrescriberID.Lname))
                __M_writer('</td>\r\n                        <td>')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(dd.QtyPrescribed))
                __M_writer('</td>         \r\n                    </tr>\r\n')
            __M_writer('                </table>\r\n')
        __M_writer('        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Taylo/github/tacohojo/tacohojo/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "43": 1, "48": 58, "54": 3, "67": 3, "68": 9, "69": 9, "70": 10, "71": 10, "72": 15, "73": 16, "74": 17, "75": 18, "76": 18, "77": 18, "78": 18, "79": 18, "80": 18, "81": 18, "82": 20, "83": 22, "84": 23, "85": 24, "86": 25, "87": 25, "88": 25, "89": 25, "90": 25, "91": 27, "92": 29, "93": 30, "94": 31, "95": 32, "96": 33, "97": 33, "98": 33, "99": 33, "100": 33, "101": 33, "102": 33, "103": 35, "104": 37, "105": 38, "106": 38, "107": 38, "108": 38, "109": 38, "110": 40, "111": 47, "112": 48, "113": 49, "114": 49, "115": 49, "116": 49, "117": 50, "118": 50, "119": 50, "120": 50, "121": 50, "122": 50, "123": 51, "124": 51, "125": 54, "126": 56, "132": 126}}
__M_END_METADATA
"""
