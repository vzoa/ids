from flask import Blueprint, request

from helpers.resource import wrap_standard_error, wrap_result_set, wrap_result_single
from models import Field

fields_resource = Blueprint(
    'fields_resource',
    __name__,
    url_prefix="/api/v1/fields",
)


@fields_resource.route('/')
def get_all_fields():
    fields = Field.get_all_fields()
    return wrap_result_set(fields)


@fields_resource.route('/', methods=['POST'])
def add_field():
    body = request.json
    required_fields = {'icao', 'name'}

    field = Field.get_by_icao(body.get("icao"))
    if not field:
        if body.keys() < required_fields:
            return wrap_standard_error(message=f"A required field is missing. Required fields are {required_fields}."), 400

        field = Field.create(
            icao=body.get("icao"),
            name=body.get("name")
        )

        field.save()

        return wrap_result_single(field)
    else:
        return wrap_standard_error(message=f"Field with ICAO of '{body.get('icao')}' already exists and cannot be "
                                           f"added. Please utilize update instead."), 400


@fields_resource.route('/', methods=['PUT'])
def update_field():
    body = request.json

    if 'icao' not in body:
        return wrap_standard_error(message=f"You must provide at least and 'icao' field."), 400

    field = Field.get_by_icao(body.get("icao"))

    if not field:
        return wrap_standard_error(message=f"Unable to find field with icao of '{body.get('icao')}'."), 400

    # update if populated
    field.name = body.get('name', field.name)

    # persist
    field.save()

    return wrap_result_single(field)

