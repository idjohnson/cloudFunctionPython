import json


def test_main(app, client):
    res = client.get('/')
    assert res.status_code == 200
    expected = "Hello hello World!"
    assert expected == res.get_data(as_text=True)