# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554924150.508464
_enable_loop = True
_template_filename = 'C:/Users/jhoyo/Desktop/dmp/tacohojo/homepage/templates/index.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        formP = context.get('formP', UNDEFINED)
        dList = context.get('dList', UNDEFINED)
        ddList = context.get('ddList', UNDEFINED)
        objectType = context.get('objectType', UNDEFINED)
        pList = context.get('pList', UNDEFINED)
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
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
        def content():
            return render_content(context)
        formP = context.get('formP', UNDEFINED)
        dList = context.get('dList', UNDEFINED)
        ddList = context.get('ddList', UNDEFINED)
        objectType = context.get('objectType', UNDEFINED)
        pList = context.get('pList', UNDEFINED)
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        formD = context.get('formD', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n')
        if objectType is '':
            __M_writer("            <p>I don't think anybody knows it was Russia that wrote Tacohojo, but I don't know, maybe it was. It could be Russia, but it could also be China. It could also be lots of other people. It also could be some wordsmith sitting on their bed that weights 400 pounds. Ok?</p>\r\n")
        __M_writer('        <div class="modal fade" id="modalContactForm" tabindex="-1" role="dialog" aria-labelledby="myModalLabel"aria-hidden="true">\r\n            <div class="modal-dialog" role="document">\r\n                <div class="modal-content">\r\n                    <div class="modal-header text-center">\r\n                    <h4 class="modal-title w-100 font-weight-bold">Write to us</h4>\r\n                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">\r\n                        <span aria-hidden="true">&times;</span>\r\n                    </button>\r\n                    </div>\r\n                    <div class="modal-body mx-3">\r\n                    <div class="md-form mb-5">\r\n                        <label data-error="wrong" data-success="right" for="form34">Your name</label>\r\n                        <input type="text" id="form34" class="form-control validate" value="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( request.user.first_name ))
        __M_writer(' ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( request.user.last_name ))
        __M_writer('">\r\n                    </div>\r\n        \r\n                    <div class="md-form mb-5">\r\n                        <label data-error="wrong" data-success="right" for="form29">Your email</label>\r\n                        <input type="email" id="form29" class="form-control validate" value="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( request.user.email ))
        __M_writer('">\r\n                    </div>\r\n        \r\n                    <div class="md-form mb-5">\r\n                        <label data-error="wrong" data-success="right" for="form32">Subject</label>\r\n                        <input type="text" id="form32" class="form-control validate">\r\n                    </div>\r\n        \r\n                    <div class="md-form">\r\n                        <label data-error="wrong" data-success="right" for="form8">Your message</label>\r\n                        <textarea type="text" id="form8" class="md-textarea form-control" rows="4"></textarea>\r\n                    </div>\r\n        \r\n                    </div>\r\n                    <div class="modal-footer d-flex justify-content-center">\r\n                    <button class="btn btn-primary">Send</button>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n            </div>\r\n        \r\n            <div class="text-center">\r\n                <a href="/homepage/index/" class="btn btn-default btn-rounded mb-4 btn-reqest" data-toggle="modal" data-target="#modalContactForm" style="border: solid;">Request More Features</a>\r\n            </div>\r\n        <div class="grid" style="margin-top: 30px;">\r\n            <form method="post">\r\n                <div class="row" style="width: 95%;">\r\n')
        if request.user.groups.filter(name='Prescribers').exists():
            __M_writer('                    <div class="col"><div hidden> ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( formP ))
            __M_writer(' </div></div>\r\n')
        else:
            __M_writer('                    <div class="col"> ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( formP ))
            __M_writer(' </div>\r\n')
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
{"filename": "C:/Users/jhoyo/Desktop/dmp/tacohojo/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "44": 1, "49": 114, "55": 3, "69": 3, "70": 5, "71": 6, "72": 8, "73": 20, "74": 20, "75": 20, "76": 20, "77": 25, "78": 25, "79": 52, "80": 53, "81": 53, "82": 53, "83": 54, "84": 55, "85": 55, "86": 55, "87": 57, "88": 57, "89": 57, "90": 61, "91": 62, "92": 64, "93": 65, "94": 66, "95": 71, "96": 72, "97": 73, "98": 73, "99": 73, "100": 73, "101": 73, "102": 73, "103": 76, "104": 79, "105": 80, "106": 85, "107": 86, "108": 87, "109": 87, "110": 87, "111": 87, "112": 90, "113": 93, "114": 94, "115": 95, "116": 103, "117": 104, "118": 105, "119": 105, "120": 105, "121": 105, "122": 106, "123": 106, "124": 106, "125": 106, "126": 106, "127": 106, "128": 107, "129": 107, "130": 110, "131": 112, "137": 131}}
__M_END_METADATA
"""
