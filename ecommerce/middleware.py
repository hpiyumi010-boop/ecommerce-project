from django.utils.deprecation import MiddlewareMixin

class DisableCSRFOriginCheck(MiddlewareMixin):
    """Disable CSRF origin check for development in Codespaces"""
    def process_request(self, request):
        # Mark this request to skip CSRF origin verification
        setattr(request, '_dont_enforce_csrf_checks', True)
