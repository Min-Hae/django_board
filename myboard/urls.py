from django.urls.conf import path
from myboard.views import view2

urlpatterns =[
    path('list/', view2.listFunc),
    path('insert/', view2.InsertFunc),
    path('content/', view2.ContentFunc),
    path('insertok/', view2.InsertokFunc),
    path('update/', view2.UpdateFunc),
    path('updateok/', view2.UpdateokFunc),
    path('delete/', view2.DeleteFunc),
    path('deleteok/', view2.DeleteokFunc),
    path('search/', view2.SearchFunc),
    path('reply/', view2.ReplyFunc),
    path('replyok/', view2.ReplyokFunc),
    ]