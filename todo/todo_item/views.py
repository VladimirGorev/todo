from django.shortcuts import render

# Create your views here.
data = {
    'case': 'Сделать ДЗ',
    'lists': [
        {'name': 'Редактируем шрифт', 'is_done': True, 'date': '01.12.2019'},
        {'name': 'Возможно была какая то конфронтация стилей, из верстки стиль не зачеркивался( Создал новый', 'is_done': False},

    ],
    'user_name': 'User',
}


def item_view(request):
    context = data
    return render(request, 'list.html', context)
