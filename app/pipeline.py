import os

from dotenv import load_dotenv

from app.scraper.website_scraper import WebsiteScraper
from app.processing.cleaner import clean_records
from app.processing.deduplicator import deduplicate
from app.enrichment.enricher import enrich_record
from app.segmentation.segmenter import assign_segment

from app.database.supabase_client import (
    save_scraped_data,
    save_campaign,
    save_metrics
)

from app.campaign.mock_platform import (
    MockCampaignPlatform
)

from app.analytics.metrics import (
    calculate_metrics
)


load_dotenv()


def run_pipeline(urls: list[str]):

    print("\n" + "=" * 60)
    print("WEB DATA → CAMPAIGN AUTOMATION PIPELINE")
    print("=" * 60)

    # ==================================================
    # 1. SCRAPING
    # ==================================================

    print("\n[1/7] Starting website scraping...")

    user_agent = os.getenv(
        "SCRAPER_USER_AGENT",
        "Mozilla/5.0"
    )

    scraper = WebsiteScraper(user_agent)

    records = []

    for url in urls:

        try:

            record = scraper.scrape(url)

            records.append(record)

        except Exception as error:

            print(
                f"[ERROR] Failed to scrape "
                f"{url}: {error}"
            )

    if not records:

        print("[ERROR] No data collected.")

        return

    print(
        f"[SCRAPER] Collected "
        f"{len(records)} records."
    )

    # ==================================================
    # 2. CLEANING
    # ==================================================

    print("\n[2/7] Cleaning data...")

    records = clean_records(records)

    print(
        f"[DATA] Records after cleaning: "
        f"{len(records)}"
    )

    # ==================================================
    # 3. DEDUPLICATION
    # ==================================================

    print("\n[3/7] Removing duplicates...")

    records = deduplicate(records)

    print(
        f"[DATA] Records after deduplication: "
        f"{len(records)}"
    )

    # ==================================================
    # 4. ENRICHMENT + SEGMENTATION
    # ==================================================

    print("\n[4/7] Enriching and segmenting data...")

    enriched_records = []

    for record in records:

        enriched = enrich_record(record)

        enriched["segment"] = assign_segment(
            enriched["industry"]
        )

        enriched_records.append(enriched)

    records = enriched_records

    print("\n[DATA] Processed records:")

    for record in records:

        print(
            f"  URL       : {record['url']}"
        )

        print(
            f"  Title     : {record['title']}"
        )

        print(
            f"  Industry  : {record['industry']}"
        )

        print(
            f"  Segment   : {record['segment']}"
        )

        print("-" * 60)

    # ==================================================
    # 5. SAVE TO SUPABASE
    # ==================================================

    print("\n[5/7] Saving data to Supabase...")

    save_scraped_data(records)

    print(
        "[DATABASE] Scraped data saved successfully."
    )

    # ==================================================
    # 6. CREATE CAMPAIGNS
    # ==================================================

    print("\n[6/7] Creating campaigns...")

    platform = MockCampaignPlatform()

    segments = set()

    for record in records:
        segments.add(record["segment"])

    campaigns = []

    for segment in sorted(segments):

        campaign = platform.create_campaign(
            segment
        )

        save_campaign(campaign)

        campaigns.append(campaign)

        print(
            f"[CAMPAIGN] Created: "
            f"{campaign['name']}"
        )

    # ==================================================
    # 7. COLLECT METRICS
    # ==================================================

    print("\n[7/7] Collecting campaign metrics...")

    for campaign in campaigns:

        raw_metrics = platform.get_metrics(
            campaign["external_campaign_id"]
        )

        calculated_metrics = calculate_metrics(
            impressions=raw_metrics["impressions"],
            clicks=raw_metrics["clicks"],
            conversions=raw_metrics["conversions"],
            spend=raw_metrics["spend"]
        )

        final_metrics = {
            **raw_metrics,
            **calculated_metrics
        }

        save_metrics(final_metrics)

        print(
            f"[METRICS] {campaign['name']}"
        )

        print(
            f"  Impressions      : "
            f"{raw_metrics['impressions']}"
        )

        print(
            f"  Clicks           : "
            f"{raw_metrics['clicks']}"
        )

        print(
            f"  Conversions      : "
            f"{raw_metrics['conversions']}"
        )

        print(
            f"  Spend            : "
            f"${raw_metrics['spend']}"
        )

        print(
            f"  CTR              : "
            f"{calculated_metrics['ctr']}%"
        )

        print(
            f"  CPC              : "
            f"${calculated_metrics['cpc']}"
        )

        print(
            f"  Conversion Rate  : "
            f"{calculated_metrics['conversion_rate']}%"
        )

    print("\n" + "=" * 60)
    print("PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 60)
    