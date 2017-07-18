from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "landscapes/index.html")

def landscapes(request, num):
    context = {
        "id": int(num),
        "image": ""
    }
    if context['id'] < 11 and context['id'] >0:
        context['image'] = 'snow.jpg'
        return render(request, 'landscapes/landscapes.html', context)
    elif context['id'] > 10 and context['id'] < 21:
        context['image'] = 'desert.jpg'
        return render(request, 'landscapes/landscapes.html', context)
    elif context['id'] > 20 and context['id'] < 31:
        context['image'] = 'forest.jpg'
        return render(request, 'landscapes/landscapes.html', context)
    elif context['id'] > 30 and context['id'] < 41:
        context['image'] = 'vineyard.jpg'
        return render(request, 'landscapes/landscapes.html', context)
    elif context['id'] > 40 and context['id'] < 51:
        context['image'] = 'tropical.jpg'
        return render(request, 'landscapes/landscapes.html', context)
