from django.urls import path

from .views import auth_views, todo_views

urlpatterns = [
    path("login/", auth_views.google_login, name="login"),
    path("callback/", auth_views.google_callback, name="google-callback"),
    path("login_failed/", auth_views.login_failed_view, name="login_failed_view"),
    path("home/", auth_views.home, name="home"),
    path("todos/", todo_views.list_todos, name="list_todos"),
    path("add/", todo_views.add_todo, name="add_todo"),
    path("<int:todo_id>/delete/", todo_views.delete_todo, name="delete_todo"),
    path(
        "<int:todo_id>/complete/",
        todo_views.mark_todo_completed,
        name="mark_todo_completed",
    ),
]
