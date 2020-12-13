from django.shortcuts import render
from main.models import ListModel


def main_view(request):
    lists = ListModel.objects.filter(user=request.user)
    count_len_lists = len(lists)
    need_blocks = 0 if (6 - count_len_lists) <= 0 else 6 - count_len_lists
    context = {'lists': lists, 'user_name': request.user.username, }
    context["need_blocks"] = need_blocks
    return render(request, 'index.html', context)
