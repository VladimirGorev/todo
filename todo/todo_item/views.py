from django.shortcuts import render
from main.models import ListModel
from todo_item.models import ItemModel






def item_view(request):
    lists = ItemModel.objects.filter(user=request.user, user_id=1)
    count_len_lists = len(lists)
    need_blocks = 0 if (6 - count_len_lists) <= 0 else 6 - count_len_lists
    context = dict(lists=lists, user_name=request.user.username, need_blocks=need_blocks, case='dfgfdg')
    return render(request, 'list.html', context)
