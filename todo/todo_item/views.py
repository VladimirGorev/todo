from django.shortcuts import render
from main.models import ListModel
from todo_item.models import ItemModel






def item_view(request):
    lists = ItemModel.objects.filter(list_model_id=request.user.id)
    case=ListModel.objects.get(id=lists[0].list_model_id).name  #(берем первый элемент из отфильтрованного списка)
    # моделей итемов по id юзера,у него запрашивает номер модели лист,и вызываем им модели имя этой модели)
    count_len_lists = len(lists)
    need_blocks = 0 if (6 - count_len_lists) <= 0 else 6 - count_len_lists
    context = dict(lists=lists, user_name=request.user.username, need_blocks=need_blocks, case=case)
    return render(request, 'list.html', context)
