from django.shortcuts import render, redirect
from .forms import MusicianForm

# Create your views here.
def add_musician(request):
    if request.method=='POST':
     musician_form=MusicianForm(request.POST)
     if musician_form.is_valid():
        musician_form.save()
        return redirect('add_musician')
    else:
        musician_form=MusicianForm()
    return render(request, 'musician.html', {'form':musician_form})
