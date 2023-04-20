from django.shortcuts import render

# Create your views here.
def get_to_dolist(request):
    return render(request, 'todo/todo_list.html')