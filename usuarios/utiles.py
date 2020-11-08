from io import BytesIO
from django.template.loader import get_template
from django.http import HttpResponse
#clase para generar pdf a partir de hhtml
from xhtml2pdf import pisa

def genera_pdf(template_src, context_dic={}):
    template=get_template(template_src)
    html1=template.render(context_dic)
    result=BytesIO()
    pdf=pisa.pisaDocument(BytesIO(html1.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')


    return None
