from django.shortcuts import render


def todo_list(request):
    return render(request, 'todolist/todo_list.html', {})
