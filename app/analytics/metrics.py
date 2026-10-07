def calculate_metrics(
    impressions: int,
    clicks: int,
    conversions: int,
    spend: float
) -> dict:

    ctr = (
        clicks / impressions * 100
        if impressions > 0
        else 0
    )

    cpc = (
        spend / clicks
        if clicks > 0
        else 0
    )

    conversion_rate = (
        conversions / clicks * 100
        if clicks > 0
        else 0
    )

    return {
        "ctr": round(ctr, 2),
        "cpc": round(cpc, 2),
        "conversion_rate": round(
            conversion_rate,
            2
        )
    }
