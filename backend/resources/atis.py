import uuid
from datetime import datetime

from flask import Blueprint, request
from peewee import DoesNotExist

from helpers.resource import wrap_standard_error, wrap_result_set, wrap_result_single
from models.atis import Atis
from models.field import Field

atis_resource = Blueprint(
    'atis_resource',
    __name__,
    url_prefix="/api/v1/atis",
)


@atis_resource.route('/')
def get_active_atis():
    atis = Atis.get_active_atis()
    return wrap_result_set(atis)


@atis_resource.route('/vatis', methods=['POST'])
def accept_atis_from_vatis():
    body = request.json

    try:
        field = Field.get_by_id(body.get("Facility"))
    except DoesNotExist:
        return wrap_standard_error(f"Provided field {body.get('Facility')} isn't a supported field."), 400

    # enforce that we are getting the right version
    if body.get("Version") != "4.0.0":
        return wrap_standard_error(f"Endpoint only supports 4.0.0 updates. {body.get('Version')} provided."), 400

    # example: 04/17/2022 15:39:59
    try:
        timestamp = datetime.strptime(body.get("Timestamp"), '%m/%d/%Y %H:%M:%S')
    except ValueError:
        return wrap_standard_error(f"Provided timestamp '{body.get('Timestamp')}' isn't a supported format."), 400

    # expire any previous ATIS for this field
    update_query = Atis.update(active=False).where(Atis.field == field and Atis.active is True)
    update_query.execute()

    # create the new ATIS
    atis = Atis.create(
        id=str(uuid.uuid4()),
        field=field,
        code=body.get("AtisLetter"),
        conditions=body.get("AirportConditions"),
        notams=body.get("Notams"),
        timestamp=timestamp,
        created=datetime.now(),
        active=True
    )
    atis.save()

    return wrap_result_single(atis)
