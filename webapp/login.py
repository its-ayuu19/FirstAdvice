from django.contrib.auth.views import LoginView

from webapp.models import Patient


class CustomLoginView(LoginView):
    template_name = 'sign-in.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        # logic to determine the URL to redirect to after successful login
         return 'dashboard'
