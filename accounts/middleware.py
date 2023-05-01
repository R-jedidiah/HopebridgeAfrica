from django.utils.deprecation import MiddlewareMixin

class LogoutOnSessionExpiryMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Code to log out the user if the session has expired
        pass
