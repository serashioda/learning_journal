"""."""
from pyramid.response import Response
import io
import os

THIS_DIR = os.path.dirname(__file__)


def home_page(request):
    """View for the home page."""
    file_path = os.path.join(THIS_DIR, 'templates', 'index.html')
    file_data = io.open(file_path).read()
    return Response(file_data)


def detail_page(request):
    """View for the detail page."""
    file_path = os.path.join(THIS_DIR, 'templates', 'single.html')
    file_data = io.open(file_path).read()
    return Response(file_data)


def create_page(request):
    """View for the create page."""
    file_path = os.path.join(THIS_DIR, 'templates', 'new_entry.html')
    file_data = io.open(file_path).read()
    return Response(file_data)


def edit_page(request):
    """View for the edit page."""
    file_path = os.path.join(THIS_DIR, 'templates', 'edit_entry.html')
    file_data = io.open(file_path).read()
    return Response(file_data)


def includeme(config):
    """The configurator will attach my views to routes."""
    config.add_view(home_page, route_name='home')
    config.add_view(detail_page, route_name='detail')
    config.add_view(create_page, route_name='create')
    config.add_view(edit_page, route_name='update')