# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554917572.9725487
_enable_loop = True
_template_filename = 'C:/Users/jhoyo/Desktop/dmp/tacohojo/homepage/templates/about.html'
_template_uri = 'about.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'content']


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
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('About Page')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('    \r\n   <div style="text-align: center;">\r\n      <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/banner.png" alt="python" style="width: 20%;" /> \r\n   </div>\r\n   <p style="text-align: center;">\r\n         We provide this web-accessible database to allow government officials, healthcare providers, and prescribers to view and analyze the volume of drugs being prescribed.<br /><br />\r\n   </p>\r\n   <div class="policy_terms" style="padding: 50px;">\r\n      <h2>What Data is in the Database?</h2>\r\n      <ul>\r\n         <li>Drug prescribers*: Name, Gender, Credentials, Location, Specialty.</li>\r\n         <li>Drugs: Name, Type (i.e. IsOpiate).</li>\r\n         <li>Quantities of each drugs that is prescribed by each Doctor.</li>\r\n         <li>Opioid overdose death rate for each state</li>\r\n      </ul>\r\n      <p>We the data above, we created analytics and prediction models that indicates the doctors who are over prescribing opioids or the drugs that are highly related to opioids.</p>\r\n      <br />\r\n      <p style="font-size: 10px;">*Drug prescribers: Health providers such as doctors, physician assistants, nurse practitioners, and others who prescribe.</p>\r\n      <br />\r\n      <h2>Privacy Policy</h2>\r\n      <h3>Our Commitment to Privacy</h3>\r\n      <p>Your privacy is as important to us as it is to you. We know you hate SPAM and so do we. That is why we will never sell or share your information with anyone without your express permission. We respect your rights and will do everything in our power to protect your personal information. In the interest of full disclosure, we provide this notice explaining our online information collection practices. This privacy notice discloses the privacy practices for Tacohojo Company (herein known as we, us and our company) and applies solely to information collected by this web site.</p>\r\n      <br />\r\n      <h3>Information Collection, Use, and Sharing</h3>\r\n      <p>We are the sole owners of the information collected on this site. We only have access to information that you voluntarily give us via email or other direct contact from you. We will not sell or rent this information to anyone. We will use your information to respond to you, regarding the reason you contacted us. We will not share your information with any third party outside of our organization, other than as necessary to fulfill your request, e.g. to ship an order.</p>\r\n      <br />\r\n      <h3>Disclosure</h3>\r\n      <p>This site uses Google web analytics service. Google may record mouse clicks, mouse movements, scrolling activity as well as text you type in this website. This site does not use Google to collect any personally identifiable information entered in this website. Google does track your browsing habits across web sites which do not use Google services.</p>\r\n      <br />\r\n      <h3>Security</h3>\r\n      <p>\r\n         We take precautions to protect your information. When you submit sensitive information via the website, your information is protected both online and offline.<br /><br />\r\n         Wherever we collect sensitive information (such as credit card data), that information is encrypted and transmitted to us in a secure way. You can verify this by looking for a closed lock icon at the bottom of your web browser, or looking for “https” at the beginning of the address of the web page.<br /><br />\r\n         While we use encryption to protect sensitive information transmitted online, we also protect your information offline. Only employees who need the information to perform a specific job (for example, billing or customer service) are granted access to personally identifiable information. The computers/servers in which we store personally identifiable information are kept in a secure environment.\r\n      </p>\r\n      <br />\r\n      <h3>Contact Form</h3>\r\n      <p>In order for us to contact you, a user must first complete the contact form. When completing the form, a user is required to give certain information (such as name and email address). This information is used to contact you about the products/services on our site in which you have expressed interest. At your option, you may also provide demographic information (such as gender or age) about yourself, but it is not required.</p>\r\n      <br />\r\n      <h3>Links</h3>\r\n      <p>This web site contains links to other sites. Please be aware that we are not responsible for the content or privacy practices of such other sites. We encourage our users to be aware when they leave our site and to read the privacy statements of any other site that collects personally identifiable information.</p>\r\n      <br />\r\n      <h3>Email Policy</h3>\r\n      <p>\r\n         Tacohojo Company has a strict no-spam policy.<br /><br />\r\n         Tacohojo Company will never sell or trade your email address to a third party.<br /><br />\r\n         Tacohojo Company does not send unsolicited commercial email messages. Tacohojo Company does send commercial email to those who have a pre-existing business relationship with us. A pre-existing business relationship means that the email recipient has made a purchase, requested information, responded to a survey or questionnaire, or had offline contact with Tacohojo Company. Email recipients may contact us at any time to opt-out of future mailings.<br /><br />\r\n         Tacohojo Company does not engage in deceptive email practices such as misleading subject lines or falsifying email addresses.<br /><br />         \r\n         Tacohojo Company does not encourage deceptive practices in email marketing to its clients.\r\n      </p>\r\n      <br />\r\n      <h2>Terms of Service</h2>\r\n      <p>Tacohojo Company is a California-based company that operates and maintains a website at the URL www.theloremipsumco.com” (the “Website”) and provides certain Content Marketing, Digital Market, Social Media Marketing and SEO services described in more detail on our website. By using the Service, you agree to be bound by these Terms of Service (this “Agreement”). If you object to anything in this Agreement or Tacohojo Company Privacy Policy, do not use the Service. This Agreement is subject to change by Tacohojo Company at any time, effective upon posting on the Website, and your use of the Service after such posting will constitute acceptance by you of such changes. This Agreement includes Tacohojo Company Privacy Policy and any notices regarding the Website.</p>\r\n      <br />\r\n      <h3>Description of the Service</h3>\r\n      <p>\r\n         Tacohojo Company provides users with access to content marketing, digital marketing, social media marketing and SEO Services, including but not limited to, search engine optimization marketing services, original content development services, and organic link building services tools. Unless explicitly stated otherwise, any new features that augment or enhance the current Service shall be subject to this Agreement. You are responsible for obtaining access to the Service, and that access may involve third-party fees (such as Internet service provider or airtime charges). In addition, you must provide and are responsible for all equipment necessary to access the Service, including a computer and modem or other access device.<br /><br />\r\n         By accessing the Website, you consent to have this Agreement provided to you in electronic form. Please print a copy of this document for your records. To retain an electronic copy of this Agreement, you may save it to into any word processing program. You have a right to a paper copy of this Agreement. If you would like a paper copy, please contact us. If you request a paper copy of the Agreement, your account will be suspended until you return a signed copy of the paper agreement to Tacohojo Company.\r\n      </p>\r\n      <br />\r\n      <h3>Proprietary Rights</h3>\r\n      <p>Tacohojo Company owns and retains all proprietary rights in the Service. The Website contains the copyrighted material, trademarks, and other proprietary information of Tacohojo Company, and its licensors. Except for information that is in the public domain or for which you have been given written permission, you agree not to reproduce, duplicate, copy, sell, trade, resell, modify, publish, transmit, distribute, perform, display, create derivative works, or exploit for any commercial purposes, any portion of the Service, use of the Service, or access to the Service or computer code that powers the Service (hereafter sometimes “Software”). You may not post, distribute, reproduce or create derivative works in any way any copyrighted material, trademarks, or other proprietary information without obtaining the prior written consent of the owner of such proprietary rights. As between You and Tacohojo Company, You own all right, title and interest in your logos and trademarks, so long as they are not derived from Tacohojo Company proprietary information. You agree to and hereby do grant Tacohojo Company the limited, nonexclusive right and license to reproduce, distribute, display and use any of your content and intellectual property as necessary to perform its obligations under this Agreement. You also grant Tacohojo Company a license to use your name and logo in Tacohojo Company marketing materials and customer lists, including on the Tacohojo Company website.</p>\r\n      <br />\r\n   </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/jhoyo/Desktop/dmp/tacohojo/homepage/templates/about.html", "uri": "about.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "45": 3, "50": 69, "56": 3, "62": 3, "68": 5, "76": 5, "77": 7, "78": 7, "84": 78}}
__M_END_METADATA
"""
