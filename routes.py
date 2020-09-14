from flask import Blueprint, request, Response, jsonify

from .db import db
from .url import Url
routes = Blueprint('routes', __name__)


@routes.route('/<shortcode>', methods=['GET'])
def get_shortcode(shortcode):
    '''
    Redirects to the original URL and updates the stats
    '''
    url = Url.query.filter_by(shortcode=shortcode).first()
    if not url:
        return 'Shortcode not found', 404
    url.update_stats()
    db.session.commit()
    return Response(headers={'Location': url.url}, status=302)


@routes.route('/<shortcode>/stats', methods=['GET'])
def stats(shortcode):
    '''
    Returns shortcode stats
    '''
    url = Url.query.filter_by(shortcode=shortcode).first()
    if not url:
        return 'Shortcode not found', 404

    return jsonify(created=url.created, lastRedirect=url.last_redirect, redirectCount=url.redirect_count), 200


@routes.route('/shorten', methods=['POST'])
def shorten():
    '''
    Shortens the URL and saves it to database
    '''
    request_url = request.form.get('url')
    request_shortcode = request.form.get('shortcode')
    if not request_url:
        return 'URL not present', 400

    if request_shortcode:
        url = Url.query.filter_by(shortcode=request_shortcode).first()
        if url:
            return 'Shortcode already in use', 409
        else:
            return 'The provided shortcode is invalid', 412

    url = Url(url=request_url)
    db.session.add(url)
    db.session.commit()

    return jsonify(shortcode=url.shortcode), 201
