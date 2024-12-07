from .forms import GuestbookEntryForm
from .models import GuestbookEntry
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

def index(request):
    entries = GuestbookEntry.objects.filter(status='active').order_by('-created_at')
    return render(request, 'index.html', {'entries': entriesk})


def add_entry(request):
    if request.method == 'POST':
        form = GuestbookEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GuestbookEntryForm()

    return render(request, 'form.html', {'form': form})

def edit_entry(request, pk):
    entry = get_object_or_404(GuestbookEntry, pk=pk)
    if request.method == 'POST':
        form = GuestbookEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GuestbookEntryForm(instance=entry)

    return render(request, 'edit.html', {'form': form})

def delete_entry(request, pk):
    entry = get_object_or_404(GuestbookEntry, pk=pk)

    if request.method == 'POST':
        if request.POST.get('email') == entry.email:
            entry.delete()
            messages.success(request, 'Запись успешно удалена.')
            return redirect('index')
        else:
            messages.error(request, 'Email не совпадает с тем, что был указан в записи.')

    return render(request, 'delete.html', {'entry': entry})