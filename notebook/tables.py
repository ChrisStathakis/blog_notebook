import django_tables2 as tables
from .models import Tags


class TagsTable(tables.Table):
    action = tables.TemplateColumn('''
                                    <a class="btn btn-primary" href="{{ record.get_edit_url }}">Επεξεργασια</a>             
                                    ''')

    class Meta:
        model = Tags
        template_name = 'django_tables2/bootstrap.html'
        fields = ['title', 'action']