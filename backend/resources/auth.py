from flask import Blueprint, request

from helpers.resource import wrap_standard_error

auth_resource = Blueprint(
    'auth_resource',
    __name__,
    url_prefix="/api/v1/auth",
)


@auth_resource.route('/init', methods=['POST'])
def init_sso_session():
    return wrap_standard_error("Not implemented"), 500


@auth_resource.route('/return')
def handle_return_from_vatsim():
    body = request.json

    return wrap_standard_error("Not implemented"), 500
