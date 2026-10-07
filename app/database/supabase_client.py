import os

from dotenv import load_dotenv
from supabase import create_client


load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


if not SUPABASE_URL:
    raise ValueError(
        "SUPABASE_URL is missing from .env"
    )

if not SUPABASE_KEY:
    raise ValueError(
        "SUPABASE_KEY is missing from .env"
    )


supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)


def save_scraped_data(records):

    if not records:
        return None

    return (
        supabase
        .table("scraped_pages")
        .upsert(
            records,
            on_conflict="url"
        )
        .execute()
    )


def save_campaign(campaign):

    return (
        supabase
        .table("campaigns")
        .insert(campaign)
        .execute()
    )


def save_metrics(metrics):

    return (
        supabase
        .table("campaign_metrics")
        .insert(metrics)
        .execute()
    )
