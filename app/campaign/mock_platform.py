import uuid


class MockCampaignPlatform:

    def create_campaign(
        self,
        segment: str
    ) -> dict:

        campaign_id = str(uuid.uuid4())

        campaign_templates = {

            "B2B Technology": {
                "headline": "Grow Your Technology Business",
                "description": (
                    "Discover smarter technology solutions "
                    "designed to improve business performance."
                ),
                "cta": "Learn More"
            },

            "Financial Services": {
                "headline": "Smarter Financial Solutions",
                "description": (
                    "Explore modern financial solutions "
                    "for your business."
                ),
                "cta": "Get Started"
            },

            "Healthcare Services": {
                "headline": "Better Healthcare Solutions",
                "description": (
                    "Discover innovative healthcare "
                    "services and solutions."
                ),
                "cta": "Learn More"
            },

            "Education Services": {
                "headline": "Build Your Future With Better Learning",
                "description": (
                    "Explore education and learning "
                    "opportunities designed for your goals."
                ),
                "cta": "Explore Now"
            },

            "General Business": {
                "headline": "Grow Your Business",
                "description": (
                    "Discover solutions designed to "
                    "help your business grow."
                ),
                "cta": "Learn More"
            }
        }

        template = campaign_templates.get(
            segment,
            campaign_templates["General Business"]
        )

        return {
            "external_campaign_id": campaign_id,
            "name": f"{segment} Campaign",
            "platform": "Mock Advertising Platform",
            "objective": "LEADS",
            "segment": segment,
            "headline": template["headline"],
            "description": template["description"],
            "cta": template["cta"],
            "status": "CREATED"
        }

    def get_metrics(
        self,
        campaign_id: str
    ) -> dict:

        return {
            "external_campaign_id": campaign_id,
            "impressions": 10000,
            "clicks": 450,
            "conversions": 35,
            "spend": 180.00
        }
    