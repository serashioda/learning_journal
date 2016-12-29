"""."""
from pyramid.view import view_config
import io
import os

THIS_DIR = os.path.dirname(__file__)

ENTRIES = [
    {"id": 0,
        "title": "Week 1",
        "title1": "Day 1",
        "create_date": "Dec 22, 2016",
        "body": "Apples are rotten",
    },
    {"id": 1,
        "title": "Week 1",
        "title1": "Day 2",
        "create_date": "Dec 23, 2016",
        "body": "Oranges are rotten",
    },
    {"id": 2,
        "title": "Week 1",
        "title1": "Day 3",
        "create_date": "Dec 24, 2016",
        "body": "Kiwis are rotten",
    },
]


# def get_entry(id):
#     """Get the entry from the dictionary by id"""
#     for entry in ENTRIES:
#         if entry["id"] == id:
#             return entry
#     return None


@view_config(route_name='list', renderer='templates/list.jinja2')
def list_page(request):
    """View for the home page."""
    return {"entries": ENTRIES}


@view_config(route_name='detail', renderer='templates/detail.jinja2')
def detail_page(request):
    """View for the detail page."""
    entry_id = int(request.matchdict["id"])
    entry = ENTRIES[entry_id]
    return {"entry": entry}


@view_config(route_name='create', renderer='templates/create.jinja2')
def create_page(request):
    """View for creating new entry."""
    return {}


@view_config(route_name='edit', renderer='templates/edit.jinja2')
def edit_page(request):
    """View for the edit page."""
    entry_id = int(request.matchdict["id"])
    entry = ENTRIES[entry_id]
    return {"entry": entry}


# def includeme(config):
#     """The configurator will attach my views to routes."""
#     config.add_view(home_page, route_name='home')
#     config.add_view(detail_page, route_name='detail')
#     config.add_view(create_page, route_name='create')
#     config.add_view(edit_page, route_name='update')
