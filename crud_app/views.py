from django.shortcuts import render, redirect
from . models import Add
from . forms import AddForm
from django.http import HttpResponse

# Create your views here.


def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('read')
        else:
            return render(request, 'add.html', {'form': form})
    else:
        form = AddForm()
        return render(request, 'add.html', {'form': form})



def read(request):
    all_data = Add.objects.all()
    return render(request, 'read.html', {'all_data': all_data})



def singel_data(request, id):
    try:
        data = Add.objects.get(id=id)
        return render(request, 'singal_data.html', {'data': data})
    except Add.DoesNotExist:
        return redirect('read')
    


def update(request, id):
    try:
        form = Add.objects.get(id=id)

        if request.method == 'POST':
            form = AddForm(request.POST, instance=form)
            if (form.is_valid()):
                form.save()
                return redirect('read')
            else:
                return render(request, 'update.html', {'form': form})
        form = AddForm(instance=form)
        return render(request, 'update.html', {'form': form})
    except:
        return HttpResponse("Data Not Found")



def delete(request, id):
    try:
        data = Add.objects.get(id=id)
        data.delete()
        return redirect('read')
    except Add.DoesNotExist:
        return HttpResponse("Data Not Found")