from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Imagee
import pytesseract
from PIL import Image


def index(request):
    objects = Imagee.objects.all()
    lt = []
    for obj in objects:
        print(obj.pic.path)
        im1 = Image.open(obj.pic.path)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\HP\AppData\Local\Tesseract-OCR\tesseract.exe'
        lt.append((pytesseract.image_to_string(im1, lang='eng', config='--psm ' + str(6)), obj))
    return render(request, 'app/index.html', {'objects': lt})


def uploadimage(request):
    p = request.FILES['image']
    obj = Imagee(pic=p)
    obj.save()
    return render(request, 'app/index.html')
