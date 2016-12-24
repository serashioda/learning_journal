"""."""
from pyramid.view import view_config
import os

THIS_DIR = os.path.dirname(__file__)

ENTRIES = [
    {"id": 0, "title": "Week 1 Day 1", "creation_date": "Dec 22, 2016", "body": "<p>Apples are rotten</p>"},
    {"id": 1, "title": "Week 1 Day 2", "creation_date": "Dec 23, 2016", "body": "<p>Oranges are rotten</p>"},
    {"id": 2, "title": "Week 1 Day 3", "creation_date": "Dec 24, 2016", "body": "<p>Kiwis are rotten</p>"},
]


def get_entry(id):
    """Get the entry from the dictionary by id"""
    for entry in ENTRIES:
        if entry["id"] == id:
            return entry
    return None


@view_config(route_name='list', renderer='templates/list.jinja2')
def index_page(request):
    """View for the home page."""
    return {
        "ENTRIES": ENTRIES,
    }


@view_config(route_name='detail', renderer='templates/detail.jinja2')
def detail_page(request):
    """View for the detail page."""
    entry_id = int(request.matchdict.get('id'))
    entry = get_entry(entry_id)
    return {'entry': entry}


@view_config(route_name='create', renderer='templates/create.jinja2')
def create_page(request):
    """."""
    return {}


@view_config(route_name='edit', renderer='templates/edit.jinja2')
def edit_page(request):
    """View for the edit page."""
    entry_id = int(request.matchdict.get('id'))
    entry = get_entry(entry_id)
    return {'entry': entry}
