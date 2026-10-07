from app.segmentation.segmenter import assign_segment


def test_technology_segment():

    assert assign_segment(
        "Technology"
    ) == "B2B Technology"


def test_finance_segment():

    assert assign_segment(
        "Finance"
    ) == "Financial Services"


def test_healthcare_segment():

    assert assign_segment(
        "Healthcare"
    ) == "Healthcare Services"
    