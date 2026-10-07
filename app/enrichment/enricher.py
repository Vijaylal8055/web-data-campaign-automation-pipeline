def classify_industry(
    title: str,
    description: str
) -> str:

    text = f"{title} {description}".lower()

    industry_keywords = {

        "Technology": [
            "software",
            "technology",
            "cloud",
            "ai",
            "artificial intelligence",
            "saas",
            "data",
            "cybersecurity"
        ],

        "Finance": [
            "finance",
            "bank",
            "investment",
            "financial",
            "insurance",
            "fintech"
        ],

        "Healthcare": [
            "health",
            "medical",
            "hospital",
            "healthcare",
            "pharma"
        ],

        "Education": [
            "education",
            "university",
            "learning",
            "course",
            "training",
            "school"
        ]
    }

    for industry, keywords in industry_keywords.items():

        for keyword in keywords:

            if keyword in text:
                return industry

    return "Other"


def enrich_record(record: dict) -> dict:

    industry = classify_industry(
        record.get("title", ""),
        record.get("description", "")
    )

    return {
        **record,
        "industry": industry
    }
