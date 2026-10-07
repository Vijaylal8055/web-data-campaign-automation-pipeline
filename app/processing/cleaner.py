def clean_record(record: dict) -> dict:
    cleaned = record.copy()

    cleaned["url"] = (
        str(cleaned.get("url", ""))
        .strip()
        .lower()
    )

    cleaned["title"] = (
        str(cleaned.get("title", ""))
        .strip()
    )

    cleaned["description"] = (
        str(cleaned.get("description", ""))
        .strip()
    )

    # Normalize repeated whitespace
    cleaned["title"] = " ".join(
        cleaned["title"].split()
    )

    cleaned["description"] = " ".join(
        cleaned["description"].split()
    )

    return cleaned


def clean_records(records: list[dict]) -> list[dict]:
    return [
        clean_record(record)
        for record in records
    ]
