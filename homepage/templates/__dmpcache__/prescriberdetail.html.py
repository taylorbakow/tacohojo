# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554956599.1329615
_enable_loop = True
_template_filename = 'C:/Users/Think/tacohojo/homepage/templates/prescriberdetail.html'
_template_uri = 'prescriberdetail.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_center']


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
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        round = context.get('round', UNDEFINED)
        drugs = context.get('drugs', UNDEFINED)
        request = context.get('request', UNDEFINED)
        prescriber = context.get('prescriber', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        round = context.get('round', UNDEFINED)
        drugs = context.get('drugs', UNDEFINED)
        request = context.get('request', UNDEFINED)
        prescriber = context.get('prescriber', UNDEFINED)
        def site_center():
            return render_site_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <table class="table">\r\n        <thead>\r\n            <th></th>\r\n            <th>Prescriber Name</th>\r\n            <th>State</th>\r\n            <th>Presciber Type</th>\r\n            <th>Specialty</th>\r\n            <th>Gender</th>\r\n            <th>Total Prescriptions</th>\r\n            <th>Total Opioid Prescriptions</th>\r\n            <th>% of prescriptions opioids</th>\r\n            <th></th>\r\n        </thead>\r\n        <tbody>\r\n            <tr>\r\n                <td></td>\r\n')
        if request.user.groups.filter(name='Prescribers').exists():
            __M_writer('                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.PrescriberID.id ))
            __M_writer(', ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.PrescriberID.Credentials ))
            __M_writer('</td>\r\n')
        else:
            __M_writer('                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.PrescriberID.Fname ))
            __M_writer(' ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.PrescriberID.Lname ))
            __M_writer(', ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.PrescriberID.Credentials ))
            __M_writer('</td>\r\n')
        __M_writer('                <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.PrescriberID.StateAbbrev ))
        __M_writer('</td>\r\n                <td>\r\n')
        if (prescriber.PrescriberID.OpioidPrescriber) == True:
            __M_writer('                    Opiod\r\n')
        else: 
            __M_writer('                    Non-Opioid\r\n')
        __M_writer('                </td>\r\n                <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.PrescriberID.Specialty ))
        __M_writer('</td>\r\n                <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.PrescriberID.Gender ))
        __M_writer('</td>\r\n                <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.PrescriberID.TotalPrescription ))
        __M_writer('</td>\r\n                <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.PrescriberID.AcetaminophinCodeine + prescriber.PrescriberID.Fentanyl + prescriber.PrescriberID.HydrocodoneAcetaminophen + prescriber.PrescriberID.OxycodoneAcetaminophen + prescriber.PrescriberID.Oxycontin))
        __M_writer('</td>\r\n                <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( round(((prescriber.PrescriberID.AcetaminophinCodeine + prescriber.PrescriberID.Fentanyl + prescriber.PrescriberID.HydrocodoneAcetaminophen + prescriber.PrescriberID.OxycodoneAcetaminophen + prescriber.PrescriberID.Oxycontin)/prescriber.PrescriberID.TotalPrescription)*100,2)))
        __M_writer('%</td>\r\n                <td></td>\r\n            </tr>\r\n        </tbody> \r\n    </table>\r\n    <table class="table">\r\n        <thead>\r\n            <th></th>\r\n            <th>Drugs Prescribed by this Doctor</th>\r\n            <th>Is Opioid?</th>\r\n            <th># of Prescriptions</th>\r\n            <th>Avg Quantity for all Prescribers</th>\r\n            <th></th>\r\n        </thead>\r\n        <tbody>\r\n')
        for p in drugs:
            __M_writer('            <tr>\r\n                <td></td>\r\n                <td><a href="/homepage/details.drugdetail/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( p.DrugID.id  ))
            __M_writer('"> ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( p.DrugID.DrugName ))
            __M_writer('</a></td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( p.DrugID.IsOpioid ))
            __M_writer('</td>\r\n')
            if (p.QtyPrescribed) > (p.DrugID.AvgPerscribed):
                __M_writer('                <td style="color:red">')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( p.QtyPrescribed ))
                __M_writer('</td>\r\n')
            else:
                __M_writer('                <td>')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( p.QtyPrescribed ))
                __M_writer('</td>\r\n')
            __M_writer('                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( p.DrugID.AvgPerscribed ))
            __M_writer('</td>\r\n                <td></td>\r\n            </tr>\r\n')
        __M_writer('        </tbody> \r\n    </table>\r\n\r\n    <div class=\'tableauPlaceholder\' id=\'viz1554955728502\' style=\'position: relative\'>\r\n        <noscript><a href=\'#\'><img alt=\' \' src=\'https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;In&#47;Intex_Opioids_Charts_OnlyWORKSHEET&#47;NumberofEachOpiodPrescribed&#47;1_rss.png\' style=\'border: none\' /></a>\r\n        </noscript>\r\n        <object class=\'tableauViz\'  style=\'display:none;\'><param name=\'host_url\' value=\'https%3A%2F%2Fpublic.tableau.com%2F\' /> <param name=\'embed_code_version\' value=\'3\' /> \r\n            <param name=\'site_root\' value=\'\' />\r\n            <param name=\'name\' value=\'Intex_Opioids_Charts_OnlyWORKSHEET&#47;NumberofEachOpiodPrescribed\' />\r\n            <param name=\'tabs\' value=\'no\' />\r\n            <param name=\'toolbar\' value=\'yes\' />\r\n            <param name=\'static_image\' value=\'https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;In&#47;Intex_Opioids_Charts_OnlyWORKSHEET&#47;NumberofEachOpiodPrescribed&#47;1.png\' /> \r\n            <param name=\'animate_transition\' value=\'yes\' />\r\n            <param name=\'display_static_image\' value=\'yes\' />\r\n            <param name=\'display_spinner\' value=\'yes\' />\r\n            <param name=\'display_overlay\' value=\'yes\' />\r\n            <param name=\'display_count\' value=\'yes\' />\r\n            <param name=\'filter\' value=\'publish=yes\' />\r\n        </object>\r\n    </div>         \r\n\r\n    <script type=\'text/javascript\' src=\'http://public.tableau.com/javascripts/api/tableau-2.0.0.min.js\'>\r\n    </script>\r\n\r\n    \r\n    <script type=\'text/javascript\'>                    \r\n        \r\n        var workbook, activeSheet;\r\n\r\n\r\n\r\n        var divElement = document.getElementById(\'viz1554955728502\');                    \r\n        var vizElement = divElement.getElementsByTagName(\'object\')[0];                    \r\n        vizElement.style.width=\'100%\';vizElement.style.height=\'400px\';\r\n        var scriptElement = document.createElement(\'script\');                    \r\n        scriptElement.src = \'https://public.tableau.com/javascripts/api/viz_v1.js\';                    \r\n        vizElement.parentNode.insertBefore(scriptElement, vizElement);        \r\n\r\n        function initViz() {\r\n            var containerDiv = document.getElementById("vizContainer"),\r\n            url = "https://public.tableau.com/shared/ZDT2YN39H?:display_count=yes";\r\n\r\n            workbook = viz.getWorkbook();\r\n            activeSheet = workbook.getActiveSheet();\r\n           \r\n            var options = {\r\n                width: 600,\r\n                height: 600,\r\n                hideTabs: true,\r\n                hideToolbar: true,\r\n                onFirstInteractive: function () {\r\n                    workbook = viz.getWorkbook();\r\n                    activeSheet = workbook.getActiveSheet();\r\n                }\r\n            };\r\n\r\n             var viz = new tableau.Viz(containerDiv, url, options);\r\n        }\r\n\r\n\r\n        \r\n\r\n        function filterSingleValue() {\r\n            activeSheet.applyFilterAsync(\r\n            "Id",\r\n            "')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.PrescriberID.id ))
        __M_writer('",\r\n            tableau.FilterUpdateType.ADD);\r\n        }        \r\n    </script>\r\n    \r\n\r\n        <div onload="initViz()">\r\n\r\n            <input type="button" value="current Dr." onclick="filterSingleValue();">\r\n        \r\n        <div id="vizContainer">\r\n\r\n         \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Think/tacohojo/homepage/templates/prescriberdetail.html", "uri": "prescriberdetail.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "51": 3, "62": 3, "63": 20, "64": 21, "65": 21, "66": 21, "67": 21, "68": 21, "69": 22, "70": 23, "71": 23, "72": 23, "73": 23, "74": 23, "75": 23, "76": 23, "77": 25, "78": 25, "79": 25, "80": 27, "81": 28, "82": 29, "83": 30, "84": 32, "85": 33, "86": 33, "87": 34, "88": 34, "89": 35, "90": 35, "91": 36, "92": 36, "93": 37, "94": 37, "95": 52, "96": 53, "97": 55, "98": 55, "99": 55, "100": 55, "101": 56, "102": 56, "103": 57, "104": 58, "105": 58, "106": 58, "107": 59, "108": 60, "109": 60, "110": 60, "111": 62, "112": 62, "113": 62, "114": 66, "115": 131, "116": 131, "122": 116}}
__M_END_METADATA
"""
