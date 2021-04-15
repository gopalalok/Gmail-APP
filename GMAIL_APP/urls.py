from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from users.view.compose import ComposeView
from users.view.home import HomeView
from users.view.sent import SentView
from users.view.inbox import InboxView
from users.view.spam import SpamView
from users.view.search import SearchView
from users.views import SignUpView, ActivateAccount
from users.middlewares.auth import auth_middleware

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', user_views.profile, name='profile'),
    path('login/',auth_middleware(auth_views.LoginView.as_view(template_name='users/login.html')), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    path('', include('blog.urls')),
    path('compose', ComposeView.as_view(), name='compose'),
    path('inbox/', InboxView.as_view(), name='inbox'),
    path('sent/', SentView.as_view(), name='sent'),
    path('view_mail/<int:id>', user_views.view_mail, name='view_mail'),
    path('spam/', SpamView.as_view(), name='spam'),
    path('search/', SearchView.as_view(), name = 'search'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)