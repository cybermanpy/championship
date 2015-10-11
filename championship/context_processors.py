from random import sample
from images.models import Image

listImage = Image.objects.values('imagesource')

def randomImages(request):
    return {'link': sample(listImage, 3)}	
