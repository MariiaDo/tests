import json

from api_collections._base_api import BaseApi


class NotesApi(BaseApi):
    def __init__(self, base_url='https://practice.expandtesting.com/notes/api'):
        super().__init__(base_url)
        self.__url = '/notes'
        self.__headers = {
            'Content-Type': 'application/json',
            'x-auth-token': "fddcccba7a294bb3bfe0e2de8e3d467aa9126ad1c0554e719b8ffa72fdf62b16"
        }

    def get_all_notes(self):
        return self._get(url=self.__url, headers=self.__headers)

    def get_note_by_id(self, note_id: str):
        return self._get(url=f'{self.__url}/{note_id}', headers=self.__headers)

    def post_new_note(self, note_data: dict):
        return self._post(self.__url, data=json.dumps(note_data), headers=self.__headers)

    def put_notes_by_id(self, note_id, note_data: dict):
        return self._put(url=f'{self.__url}/{note_id}', data=json.dumps(note_data), headers=self.__headers)

    def patch_completed_by_id(self, note_id, note_data: dict):
        return self._patch(url=f'{self.__url}/{note_id}', data=json.dumps(note_data), headers=self.__headers)

    def delete_note_by_id(self, note_id: str):
        return self._delete(url=f'{self.__url}/{note_id}', headers=self.__headers)