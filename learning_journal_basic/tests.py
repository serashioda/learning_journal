"""."""
import pytest
from pyramid import testing


@pytest.fixture()
def req():
    """."""
    the_request = testing.DummyRequest()
    return the_request


@pytest.fixture
def testapp():
    """Create an app instance for testing."""
    from webtest import TestApp
    from learning_journal_basic import main
    app = main({})
    return TestApp(app)


def test_home_page_renders_file_data(req):
    """My home page view returns some data."""
    from .views import home_page##
    response = home_page(req)
    assert "entries" in response


def test_home_page_has_iterable(req):
    """."""
    from .views import list
    response = list(req)
    assert hasattr(response["entries"], "__iter__")


def test_home_page_has_list(testapp):
    """Test that index/home page has list of entries, and button/links to all sub-pages."""
    response = testapp.get("/", status=200)
    inner_html = response.html
    assert "Today I learned in Python 401d5 ... " in inner_html.find("body").text


def test_detail_page_has_detail(testapp):
    """Test that single page exits/links to single entry."""
    response = testapp.get("/journal/3", status=200)
    inner_html = response.html
    assert "Today on Week 1 Day 3, I learned in Python 401d5 ... " in inner_html.find("body").text


def test_create_page_has_data(testapp):
    """Test that detail page exists/links properly."""
    response = testapp.get("/journal/new-entry", status=200)
    inner_html = response.html
    assert "New Entry" in inner_html.find("main").text


def test_edit_page_has_data(testapp):
    """Test edit page exist/links properly"""
    response = testapp.get("/journal/3/edit-entry")
    inner_html = response.html
    assert "Title:" in inner_html.find("article").text


# from webtest import TestApp

# From learning_journal_basic import main

# testapp = TestApp(min({}))

# response = testapp.get("/", status=200)

# from pprint import pprint

# pprint(dir(response))

# html = response.html

# html.find_all("li")

# len(html.find_all("li"))
# >> 5

# html.find("ul").child

# <<ul = html.find('ul')
# <<ul



"""."""
import pytest
from pyramid import testing


@pytest.fixture()
def req():
    """."""
    the_request = testing.DummyRequest()
    return the_request


def test_home_page_renders_file_data(req):
    """My home page view returns some data."""
    from .views import home_page
    response = home_page(req)
    assert "bag_list" in response


@pytest.fixture()


@pytest.fixture()
def testapp():
    from webtest import TestApp
    from learning_journal_basic import main
    app = main({})
    from webtest import TestApp
    return TestApp(app)

def test_home_page_has_list(testapp):
    response = testapp.get("/", status=200)
    inner_html = response.html


# from webtest import TestApp

# From learning_journal_basic import main

# testapp = TestApp(min({}))

# response = testapp.get("/", status=200)

# from pprint import pprint

# pprint(dir(response))

# html = response.html

# html.find_all("li")

# len(html.find_all("li"))
# >> 5

# html.find("ul").child

# <<ul = html.find('ul')
# <<ul



import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from .views import my_view
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info['project'], 'learning_journal_basic')


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from learning_journal_basic import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_root(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'Pyramid' in res.body)
