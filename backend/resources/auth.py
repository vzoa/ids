from flask import Blueprint, request

from helpers.resource import wrap_standard_error

auth_resource = Blueprint(
    'auth_resource',
    __name__,
    url_prefix="/api/v1/auth",
)


@auth_resource.route('/init', methods=['POST'])
def init_sso_session():
    """
    Initializes a new VATSIM SSO session.

    This endpoint will initialize a new VATSIM SSO session and redirect the user to the VATSIM SSO login page.

    :return:
    """
    return wrap_standard_error("Not implemented"), 500


@auth_resource.route('/return')
def handle_return_from_vatsim():
    """
    Function to handle the return from VATSIM SSO.

    Upon returning from VATSIM SSO, the user will be redirected to this endpoint with a code in the query string.

    The user will be logged in if the code is valid, otherwise they will be redirected to the login page with an error.
    """

    return wrap_standard_error("Not implemented"), 500
