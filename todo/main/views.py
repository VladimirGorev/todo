from django.shortcuts import render

# Create your views here.

data = {
    'lists': [
        {'name': 'Работа', 'is_done': True, 'date': '01.12.2019'},
        {'name': 'Дом', 'is_done': False},
    ],
    'user_name': 'Admin',
}

count_len_lists = len(data['lists'])
need_blocks = 0 if (6-count_len_lists) <= 0 else 6 - count_len_lists
data["need_blocks"] = need_blocks


def main_view(request):
    context = data
    return render(request, 'index.html', context)
