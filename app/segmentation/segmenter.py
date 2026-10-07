def assign_segment(industry: str) -> str:

    segments = {
        "Technology": "B2B Technology",
        "Finance": "Financial Services",
        "Healthcare": "Healthcare Services",
        "Education": "Education Services",
        "Other": "General Business"
    }

    return segments.get(
        industry,
        "General Business"
    )
