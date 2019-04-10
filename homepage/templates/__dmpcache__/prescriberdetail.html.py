# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554865327.1868706
_enable_loop = True
_template_filename = 'C:/Users/jhoyo/Desktop/dmp/tacohojo/homepage/templates/prescriberdetail.html'
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
        group = context.get('group', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        prescriber = context.get('prescriber', UNDEFINED)
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
        group = context.get('group', UNDEFINED)
        def site_center():
            return render_site_center(context)
        prescriber = context.get('prescriber', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <table class="table">\r\n        <thead>\r\n            <th></th>\r\n            <th>Prescriber Name</th>\r\n            <th>State</th>\r\n            <th>Presciber Type</th>\r\n            <th>Specialty</th>\r\n            <th>Total Prescriptions</th>\r\n            <th>Total Opioid Prescriptions</th>\r\n            <th></th>\r\n        </thead>\r\n        <tbody>\r\n            <tr>\r\n                <td></td>\r\n')
        if group.name == 'Health Officials':
            __M_writer('                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.PrescriberID.Fname ))
            __M_writer(' ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.PrescriberID.Lname ))
            __M_writer(', ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.PrescriberID.Credentials ))
            __M_writer('</td>\r\n')
        elif group.name == 'Data Clerks':
            __M_writer('                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.PrescriberID.Fname ))
            __M_writer(' ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.PrescriberID.Lname ))
            __M_writer(', ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.PrescriberID.Credentials ))
            __M_writer('</td>\r\n')
        elif group.name == 'Prescribers':
            __M_writer('                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.PrescriberID.id ))
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
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.PrescriberID.TotalPrescription ))
        __M_writer('</td>\r\n                <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.PrescriberID.AcetaminophinCodeine + prescriber.PrescriberID.Fentanyl + prescriber.PrescriberID.HydrocodoneAcetaminophen + prescriber.PrescriberID.OxycodoneAcetaminophen + prescriber.PrescriberID.Oxycontin))
        __M_writer('</td>\r\n                <td></td>\r\n            </tr>\r\n        </tbody> \r\n    </table>\r\n    <div class=\'tableauPlaceholder\' id=\'viz1554849453936\' style=\'position: relative\'>\r\n        <noscript><a href=\'#\'><img alt=\' \' src=\'https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;In&#47;Intex_Opioids&#47;Howmanyofeachdrugs&#47;1_rss.png\' style=\'border: none\' /></a>\r\n        </noscript>\r\n        <object class=\'tableauViz\'  style=\'display:none;\'>\r\n            <param name=\'host_url\' value=\'https%3A%2F%2Fpublic.tableau.com%2F\' /> \r\n            <param name=\'embed_code_version\' value=\'3\' /> \r\n            <param name=\'site_root\' value=\'\' />\r\n            <param name=\'name\' value=\'Intex_Opioids&#47;Howmanyofeachdrugs\' />\r\n            <param name=\'tabs\' value=\'yes\' /><param name=\'toolbar\' value=\'yes\' />\r\n            <param name=\'static_image\' value=\'https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;In&#47;Intex_Opioids&#47;Howmanyofeachdrugs&#47;1.png\' /> \r\n            <param name=\'animate_transition\' value=\'yes\' /><param name=\'display_static_image\' value=\'yes\' />\r\n            <param name=\'display_spinner\' value=\'yes\' /><param name=\'display_overlay\' value=\'yes\' />\r\n            <param name=\'display_count\' value=\'yes\' /><param name=\'filter\' value=\'publish=yes\' />\r\n        </object>\r\n    </div>  \r\n\r\n    <script type=\'text/javascript\' src=\'http://public.tableau.com/javascripts/api/tableau-2.0.0.min.js\'>\r\n    </script>\r\n\r\n    <script type=\'text/javascript\'>                   \r\n        \r\n        var workbook, activeSheet;\r\n\r\n            var divElement = document.getElementById(\'viz1554849453936\');                    \r\n            var vizElement = divElement.getElementsByTagName(\'object\')[0];                    \r\n            vizElement.style.width=\'100%\';\r\n            vizElement.style.height=(divElement.offsetWidth*0.75)+\'px\';                    \r\n            var scriptElement = document.createElement(\'script\');                    \r\n            scriptElement.src = \'https://public.tableau.com/javascripts/api/viz_v1.js\';                    \r\n            vizElement.parentNode.insertBefore(scriptElement, vizElement);\r\n\r\n        function initViz() {\r\n            var containerDiv = document.getElementById("vizContainer"),\r\n            url = "https://public.tableau.com/views/Intex_Opioids/Howmanyofeachdrugs?:embed=y&:display_count=yes&publish=yes";\r\n\r\n            var options = {\r\n                width: placeholderDiv.offsetWidth,\r\n                height: placeholderDiv.offsetHeight,\r\n                hideTabs: true,\r\n                hideToolbar: true,\r\n                onFirstInteractive: function () {\r\n                    workbook = viz.getWorkbook();\r\n                    activeSheet = workbook.getActiveSheet();\r\n                }\r\n            };\r\n\r\n            var viz = new tableau.Viz(containerDiv, url);\r\n        }\r\n\r\n        activeSheet.applyFilterAsync(\r\n            "Id",\r\n            ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.PrescriberID.id ))
        __M_writer(',\r\n            tableau.FilterUpdateType.REPLACE);\r\n\r\n        \r\n\r\n        //function filterSingleValue() {\r\n            \r\n        //}\r\n    </script>\r\n    <div onload="initViz()">\r\n\r\n        <!--<input type="button" value=')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.PrescriberID.id ))
        __M_writer(' onclick="filterSingleValue();">-->\r\n        <div id="vizContainer">\r\n\r\n        </div>\r\n    </div>  \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/jhoyo/Desktop/dmp/tacohojo/homepage/templates/prescriberdetail.html", "uri": "prescriberdetail.html", "source_encoding": "utf-8", "line_map": {"29": 0, "39": 1, "49": 3, "58": 3, "59": 18, "60": 19, "61": 19, "62": 19, "63": 19, "64": 19, "65": 19, "66": 19, "67": 20, "68": 21, "69": 21, "70": 21, "71": 21, "72": 21, "73": 21, "74": 21, "75": 22, "76": 23, "77": 23, "78": 23, "79": 23, "80": 23, "81": 25, "82": 25, "83": 25, "84": 27, "85": 28, "86": 29, "87": 30, "88": 32, "89": 33, "90": 33, "91": 34, "92": 34, "93": 35, "94": 35, "95": 91, "96": 91, "97": 102, "98": 102, "104": 98}}
__M_END_METADATA
"""
