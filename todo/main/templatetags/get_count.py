
from django.utils.safestring import mark_safe
from django import template
from django.template.defaulttags import register



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


@register.filter
def get_div(arg):
    context = arg * our_div
    return ( mark_safe(context))


