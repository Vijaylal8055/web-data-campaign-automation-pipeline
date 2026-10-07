from app.processing.cleaner import clean_record


def test_clean_record():

    record = {
        "url": " HTTPS://Example.COM ",
        "title": "  Test   Website  ",
        "description": " Some   description "
    }

    result = clean_record(record)

    assert result["url"] == "https://example.com"

    assert result["title"] == "Test Website"

    assert result["description"] == "Some description"
    