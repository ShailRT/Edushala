from .models import Navbar 

def navbar(request):
    col_nav = Navbar.objects.filter(page_type='college')[:9]
    cr_nav = Navbar.objects.filter(page_type='course')[:9]
    ab_nav = Navbar.objects.filter(page_type='abroad')[:9]
    return {'col_nav': col_nav, 'cr_nav': cr_nav, 'ab_nav': ab_nav}