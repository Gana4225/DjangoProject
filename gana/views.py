from django.shortcuts import render, HttpResponse
from .models import student
from django.template.loader import render_to_string
from weasyprint import HTML
def base(request):
    error_message = None
    if request.method == "POST":
        pk = request.POST["rn"]
        tt2 = pk.upper()
        data = student.objects.filter(rn=tt2)
        print(type(data))
        if data:
            request.session['rn'] = tt2
            return render(request, "index.html", {'data': data})
        else:
            error_message = "Roll No Does Not Exist"
    return render(request, "index.html", {'error_message': error_message})

def tt(request):
    return render(request, "base.html")

def generate_pdf(request):
    tt2 = request.session.get('rn', None)
    # Get data from the database (adjust as needed for your use case)
    data = student.objects.filter(rn=tt2)

    # Render the template with the data
    html_string = render_to_string('pdf_template.html', {'data': data})

    # Generate the PDF
    pdf = HTML(string=html_string).write_pdf()

    # Return the PDF as a response
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="result.pdf"'
    return response


def profile(request):
    return render(request, "profile.html")