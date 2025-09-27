from django.shortcuts import render
from django.views.generic import CreateView, View
from .models import PDF
from django.http import HttpResponseRedirect
from .forms import UploadForm

def store_file(file):
    with open("temp/image.png", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

class UploadPDF(View):
    def get(self, request):
        form = UploadForm()
        return render(request, "pdf/upload.html", {"form": form})

    def post(self, request):
        submitted_form = UploadForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            # store_file(request.FILES["file"])
            pdf_model = PDF(file=request.FILES["file"], name=request.POST["name"])
            # as we are using file in our model. On Save the model will take care of file handling for us, saving them on hdd
            pdf_model.save()
            return render(request, "pdf/upload.html", {"form": submitted_form})
        # getting access to files uplaoded

        return HttpResponseRedirect("/upload")
    # model = PDF
    # template_name = "pdf/upload.html"
    # fields = "__all__"


class UploadPDF2(CreateView):
    model = PDF
    template_name = "pdf/upload2.html"