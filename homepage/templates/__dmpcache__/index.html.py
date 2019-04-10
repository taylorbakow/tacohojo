# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554868449.2021296
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
        def content():
            return render_content(context._locals(__M_locals))
        formD = context.get('formD', UNDEFINED)
        objectType = context.get('objectType', UNDEFINED)
        pList = context.get('pList', UNDEFINED)
        group = context.get('group', UNDEFINED)
        ddList = context.get('ddList', UNDEFINED)
        formP = context.get('formP', UNDEFINED)
        self = context.get('self', UNDEFINED)
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
        def content():
            return render_content(context)
        formD = context.get('formD', UNDEFINED)
        objectType = context.get('objectType', UNDEFINED)
        pList = context.get('pList', UNDEFINED)
        group = context.get('group', UNDEFINED)
        ddList = context.get('ddList', UNDEFINED)
        formP = context.get('formP', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n')
        if objectType is '':
            __M_writer("            <p>I don't think anybody knows it was Russia that wrote Lorem Ipsum, but I don't know, maybe it was. It could be Russia, but it could also be China. It could also be lots of other people. It also could be some wordsmith sitting on their bed that weights 400 pounds. Ok?</p>\r\n")
        __M_writer('        <div class="grid" style="margin-top: 30px;">\r\n            <form method="post">\r\n                <div class="row" style="width: 95%;">\r\n')
        if group.name == 'Health Officials':
            __M_writer('                    <div class="col"> ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( formP ))
            __M_writer(' </div>\r\n')
        elif group.name == 'Data Clerks':
            __M_writer('                    <div class="col"> ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( formP ))
            __M_writer(' </div>\r\n')
        elif group.name == 'Prescribers':
            __M_writer('                    <div class="col"><div hidden> ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( formP ))
            __M_writer(' </div></div>\r\n')
        __M_writer('                    <div class="col"> ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( formD ))
        __M_writer(' </div>\r\n                    <div class="col" style="margin-left: -90px;"><input style="width: 140px;" class="button is-dark" type="submit" value="Search"></div>\r\n                </div>\r\n            </form>\r\n')
        if objectType is not '':
            __M_writer('                <h1 class="title">Search Results:</h1>\r\n')
        __M_writer('            <div class="row">\r\n')
        if objectType == 'Prescriber' or objectType == 'Both':
            __M_writer('                    <div class="col">\r\n                        <table class="table table-hover" id="dev-table">\r\n                            <tr>\r\n                                <th>Full Name</th>\r\n                            </tr>\r\n')
            for p in pList:
                __M_writer("                            <tr>\r\n                                <td><a href='/homepage/details.prescriberdetail/")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( p.id ))
                __M_writer("'>")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(p.Fname))
                __M_writer(' ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(p.Lname))
                __M_writer('</a></td>\r\n                            </tr>\r\n')
            __M_writer('                        </table>\r\n                    </div>  \r\n')
        if objectType == 'Drug' or objectType == 'Both':
            __M_writer('                    <div class="col">\r\n                        <table class="table table-hover" id="dev-table">\r\n                            <tr>\r\n                                <th>Drug Name</th>\r\n                            </tr>\r\n')
            for d in dList:
                __M_writer("                            <tr>\r\n                                <td><a href='/homepage/details.drugdetail/")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( d.id ))
                __M_writer("'>")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(d.DrugName))
                __M_writer('</a></td>\r\n                            </tr>\r\n')
            __M_writer('                        </table>\r\n                    </div>\r\n')
        __M_writer('            </div>\r\n')
        if objectType == 'Both':
            __M_writer('                <br/>\r\n                <h1 class="title">Prescriber Stats:</h1>\r\n                <table class="table table-hover" id="dev-table">\r\n                    <tr>\r\n                        <th>Drug Name</th>\r\n                        <th>Prescriber</th>\r\n                        <th>Quantity</th>\r\n                    </tr>\r\n')
            for dd in ddList:
                __M_writer("                    <tr>\r\n                        <td><a href='/homepage/details.drugdetail/")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( dd.DrugID.id ))
                __M_writer("'>")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(dd.DrugID.DrugName))
                __M_writer("</a></td>\r\n                        <td><a href='/homepage/details.prescriberdetail/")
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
{"filename": "C:/Users/Taylo/github/tacohojo/tacohojo/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "44": 1, "49": 75, "55": 3, "69": 3, "70": 5, "71": 6, "72": 8, "73": 11, "74": 12, "75": 12, "76": 12, "77": 13, "78": 14, "79": 14, "80": 14, "81": 15, "82": 16, "83": 16, "84": 16, "85": 18, "86": 18, "87": 18, "88": 22, "89": 23, "90": 25, "91": 26, "92": 27, "93": 32, "94": 33, "95": 34, "96": 34, "97": 34, "98": 34, "99": 34, "100": 34, "101": 37, "102": 40, "103": 41, "104": 46, "105": 47, "106": 48, "107": 48, "108": 48, "109": 48, "110": 51, "111": 54, "112": 55, "113": 56, "114": 64, "115": 65, "116": 66, "117": 66, "118": 66, "119": 66, "120": 67, "121": 67, "122": 67, "123": 67, "124": 67, "125": 67, "126": 68, "127": 68, "128": 71, "129": 73, "135": 129}}
__M_END_METADATA
"""
