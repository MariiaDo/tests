from http import HTTPStatus

import pytest

from api_collections.notes_api import NotesApi
from api_collections.schemas.json_schemas import NotesSchema
#from utilities.allure_logger import log_response


# get all notes positive
@pytest.mark.positive
def test_get_all_notes():
    resp = NotesApi().get_all_notes()
    #log_response(resp)
    assert resp.status_code == HTTPStatus.OK, f'Request fail! ({resp.text})'
    data = resp.json()
    NotesApi._validate_json(data, NotesSchema.all_notes)


# get note by id positive
@pytest.mark.positive
def test_get_note_by_id(get_new_note_id):
    _id = get_new_note_id
    resp = NotesApi().get_note_by_id(note_id=_id)
    #log_response(resp)
    assert resp.status_code == HTTPStatus.OK, f'Request fail! ({resp.text})'
    data = resp.json()
    NotesApi._validate_json(data, NotesSchema.get_note_by_id)


# get note by id negative
def test_get_note_by_id_negative(get_new_note_id):
    _id = str(get_new_note_id)[0:-1]
    resp = NotesApi().get_note_by_id(note_id=_id)
    #log_response(resp)
    assert resp.status_code == HTTPStatus.BAD_REQUEST, f'Request fail! ({resp.text})'


# Create a new note positive
@pytest.mark.positive
def test_post_new_note(get_fake_note_payload):
    payload = get_fake_note_payload
    resp = NotesApi().post_new_note(note_data=payload)
    #log_response(resp)
    assert resp.status_code == HTTPStatus.OK, f'Request fail! ({resp.text})'
    data = resp.json()
    NotesApi._validate_json(data, NotesSchema.post_new_note)


# Create a new note negative
def test_post_new_note_negative(get_fake_note_payload):
    payload = get_fake_note_payload
    del payload["description"]
    resp = NotesApi().post_new_note(note_data=payload)
    #log_response(resp)
    assert resp.status_code == HTTPStatus.BAD_REQUEST, f'Request fail! ({resp.text})'


# Update an existing note positive
@pytest.mark.positive
def test_put_notes_by_id(put_fake_note_payload):
    payload = put_fake_note_payload
    resp = NotesApi().put_notes_by_id(note_id=payload.get('id'), note_data=payload)
    #log_response(resp)
    assert resp.status_code == HTTPStatus.OK, f'Request fail! ({resp.text})'
    data = resp.json()
    NotesApi._validate_json(data, NotesSchema.put_notes_by_id)


# Update an existing note negative
def test_put_notes_by_id_negative(put_fake_note_payload):
    payload = put_fake_note_payload
    del payload["completed"]
    resp = NotesApi().put_notes_by_id(note_id=payload.get('id'), note_data=payload)
    #log_response(resp)
    assert resp.status_code == HTTPStatus.BAD_REQUEST, f'Request fail! ({resp.text})'


# Update the completed status of a note positive
@pytest.mark.positive
def test_patch_completed_by_id(patch_fake_completed_payload):
    payload = patch_fake_completed_payload
    resp = NotesApi().patch_completed_by_id(note_id=payload.get('id'), note_data=payload)
    #log_response(resp)
    assert resp.status_code == HTTPStatus.OK, f'Request fail! ({resp.text})'
    data = resp.json()
    NotesApi._validate_json(data, NotesSchema.patch_completed_by_id)


# Delete a note by id positive
@pytest.mark.positive
def test_delete_note_by_id(get_new_note_id):
    resp = NotesApi().delete_note_by_id(note_id=get_new_note_id)
    #log_response(resp)
    assert resp.status_code == HTTPStatus.OK, f'Request fail! ({resp.text})'
    data = resp.json()
    NotesApi._validate_json(data, NotesSchema.delete_note_by_id)


# Delete a note by id negative
def test_delete_note_by_id_negative(get_new_note_id):
    _id = str(get_new_note_id)[0:-1]
    resp = NotesApi().delete_note_by_id(note_id=_id)
    #log_response(resp)
    assert resp.status_code == HTTPStatus.BAD_REQUEST, f'Request fail! ({resp.text})'
