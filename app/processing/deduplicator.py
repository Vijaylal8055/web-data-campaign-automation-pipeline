def deduplicate(records: list[dict]) -> list[dict]:
    seen_urls = set()
    unique_records = []

    for record in records:

        url = record.get("url", "")

        if url in seen_urls:
            continue

        seen_urls.add(url)
        unique_records.append(record)

    return unique_records
