import dataclasses


def test_get_data(monkeypatch):

    print('aaa')
    print(__name__)
    print('hello')
    from . import index
    from .index import handler
    from user_table import UserTable

    def mock_return(table_name):
        return 'aaa'

    def scan_user_data():
        return 'dummy data dayo'

    monkeypatch.setattr(index, "get_table_data", mock_return)
    monkeypatch.setattr(UserTable, "scan_user_data", scan_user_data)
    handler('', '')
