import pytesseract
from PIL import Image
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract_text(request):
    if request.method == 'POST' and request.FILES['image']:
        uploaded_image = request.FILES['image']
        language = request.POST.get('language', 'eng')
        fs = FileSystemStorage()
        filename = fs.save(uploaded_image.name, uploaded_image)
        img_path = fs.path(filename)
        
        img = Image.open(img_path)
        extracted_text = pytesseract.image_to_string(img, lang=language)
        
        return render(request, 'ocr/result.html', {'text': extracted_text})
    return render(request, 'ocr/upload.html')
