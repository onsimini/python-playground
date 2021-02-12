from my_app.app import create_app

def test_index():
    tester = create_app().test_client()
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200
    assert response.data == b"Hello, World!"
