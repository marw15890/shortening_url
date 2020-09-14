from ..url import Url
from pytest_flask_sqlalchemy.fixtures import db_session


def test_generate_shortcode(db_session):
    request_url = 'https://www.google.com'
    url = db_session.query(Url(url=request_url)).get(1)
    #url = Url(url=request_url)
    shortcode = url.shortcode

    # check length of shortcode
    assert len(shortcode) == 6

    # check if shortcode is made of alphanumeric characters and underscore
    test_shortcode = shortcode.replace('_', '')
    assert test_shortcode.isalnum()


def test_update_stats(db_session):
    request_url = 'https://www.google.com'
    url = db_session.query(Url(url=request_url)).get(1)
    #url = Url(url=request_url)

    # check no redirects and no last redirect
    assert url.redirect_count == 0
    assert not url.last_redirect

    # check one redirect and last redirect
    url.update_stats()
    assert url.redirect_count == 1
    assert url.last_redirect > url.created