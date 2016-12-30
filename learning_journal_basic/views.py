"""."""
from pyramid.view import view_config
import io
import os

THIS_DIR = os.path.dirname(__file__)

ENTRIES = [
    {"id": 0,
        "title": "Week 3",
        "title1": "Day 5",
        "create_date": "Dec 23, 2016",
        "body": "Pomogranets are rotten",
    },
    {"id": 1,
        "title": "Week 3",
        "title1": "Day 4",
        "create_date": "Dec 22, 2016",
        "body": "Mangos are rotten",
    },
    {"id": 2,
        "title": "Week 3",
        "title1": "Day 3",
        "create_date": "Dec 21, 2016",
        "body": "Kiwis are rotten",
    },
    {"id": 3,
        "title": "Week 3",
        "title1": "Day 2",
        "create_date": "Dec 20, 2016",
        "body": "Oranges are rotten",
    },
    {"id": 4,
        "title": "Week 3",
        "title1": "Day 1",
        "create_date": "Dec 19, 2016",
        "body": "Apples are rotten",
    },
]


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
