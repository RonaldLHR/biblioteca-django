from django.urls import path
import core.views

urlpatterns = [
    path('livros/', core.views.livro_list_create, name='livros-list-create'),
    path('livros/<int:pk>/', core.views.livro_detail, name='livro-detail'),
]




'''
urlpatterns = [
    path('admin/', admin.site.urls),
]
'''