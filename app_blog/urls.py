from django.urls import path

from . import views

urlpatterns = [
    path('', views.auth, name='url_name_index'),
    path('login', views.loginUser, name='url_name_login'),
    path('signup', views.signupUser, name='url_name_signup'),
    # path('author_detail/<int:arg_author_id>', views.authorDetail, name='url_name_author_detail'),
    path('author_admin_panel/<int:arg_user_id>', views.authorPanel, name='url_name_author_panel'), 
    path('register_as_author/<int:arg_user_id>', views.registerAsAuthor, name='url_name_register_as_author'),
    path('update_blog', views.blogAdd, name='url_name_update_blog'), 
    path('delete_blog/<int:arg_blog_id>', views.blogDelete, name='url_name_delete_blog'),
    path('add_blog', views.blogAdd, name='url_name_add_blog'),
    path('redirect_index', views.indexRedirect, name='url_name_index_redirect'),
    path('logout_user', views.logoutUser, name='url_name_logout'),
]