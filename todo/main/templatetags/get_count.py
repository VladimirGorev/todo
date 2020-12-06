
from django.utils.safestring import mark_safe
from django import template
from main.views import need_blocks


register = template.Library()

our_div = """
                    <div class="table-data__table-row">
                    <div class="table-row_table_cell-1">   
                    </div>
                    <div class="buttons">
                        <div class="table-data-two_table-icon">
                        </div>
                        <a class="delete_button" href="#">
                            <div class="table-row_table_icon">     
                            </div>
                        </a>
                    </div>
                </div>
        """


@register.simple_tag
def get_div():
    context = need_blocks*our_div
    return (mark_safe(context))

@register.filter
def create_range(value, start_index=0):
    return range(start_index, value+start_index)
# {% for i in 0|create_range %} this text add in our template for create cycle range
# {% endfor %}
