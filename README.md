# Web Data → Campaign Automation

A Python-based demonstration pipeline that collects data from permitted public websites, cleans and deduplicates the data, enriches it with industry classification, assigns audience segments, stores the results in Supabase, generates mock advertising campaigns, and calculates campaign performance metrics.

> **Demo project:** This project is designed for demonstration and technical evaluation purposes. It does **not** launch real advertising campaigns or spend real advertising money.

---

## 🚀 Project Overview

The system demonstrates an end-to-end workflow:

```text
Permitted Public Websites
          │
          ▼
   Python Web Scraper
          │
          ▼
     Data Cleaning
          │
          ▼
    Deduplication
          │
          ▼
      Enrichment
          │
          ▼
 Audience Segmentation
          │
          ▼
       Supabase
          │
          ▼
 Mock Campaign Generator
          │
          ▼
  Mock Campaign Metrics
```

The project demonstrates practical experience with:

- Python automation
- Web scraping
- Data cleaning
- Data deduplication
- Rule-based data enrichment
- Audience segmentation
- Supabase / PostgreSQL
- Campaign automation concepts
- Campaign analytics
- Unit testing
- Environment configuration
- Modular Python architecture

---

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| HTTP Client | Requests |
| HTML Parsing | BeautifulSoup |
| Database | Supabase / PostgreSQL |
| Configuration | python-dotenv |
| Testing | Pytest |
| Data Processing | Native Python lists/dictionaries |
| Campaign Integration | Mock Advertising Platform |
| Development Environment | VS Code |
| Operating System | Windows 11 |

---

## 📁 Project Structure

```text
web-data-campaign-automation/
│
├── app/
│   ├── __init__.py
│   ├── pipeline.py
│   │
│   ├── scraper/
│   │   ├── __init__.py
│   │   └── website_scraper.py
│   │
│   ├── processing/
│   │   ├── __init__.py
│   │   ├── cleaner.py
│   │   └── deduplicator.py
│   │
│   ├── enrichment/
│   │   ├── __init__.py
│   │   └── enricher.py
│   │
│   ├── segmentation/
│   │   ├── __init__.py
│   │   └── segmenter.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   └── supabase_client.py
│   │
│   ├── campaign/
│   │   ├── __init__.py
│   │   └── mock_platform.py
│   │
│   └── analytics/
│       ├── __init__.py
│       └── metrics.py
│
├── data/
│   └── raw/
│
├── scripts/
│   └── run_pipeline.py
│
├── tests/
│   ├── test_cleaner.py
│   └── test_segmenter.py
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/web-data-campaign-automation.git
cd web-data-campaign-automation
```

Replace `YOUR_USERNAME` with your GitHub username.

---

## 2. Create a virtual environment

On Windows CMD:

```cmd
python -m venv venv
```

Activate it:

```cmd
venv\Scripts\activate
```

You should see:

```text
(venv)
```

at the beginning of your terminal prompt.

---

## 3. Install dependencies

```cmd
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Current dependencies:

```text
requests
beautifulsoup4
supabase
python-dotenv
pytest
lxml
```

---

# 🔐 Environment Configuration

Create a `.env` file in the project root:

```env
SUPABASE_URL=https://YOUR_PROJECT_ID.supabase.co
SUPABASE_KEY=YOUR_SUPABASE_KEY
SCRAPER_USER_AGENT=Mozilla/5.0
```

Replace the placeholders with your Supabase project credentials.

### Important

Never commit `.env` to GitHub.

The repository includes `.env.example` as a template:

```env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-supabase-key
SCRAPER_USER_AGENT=Mozilla/5.0
```

The `.gitignore` file excludes:

```text
.env
venv/
__pycache__/
*.pyc
.pytest_cache/
.vscode/
.idea/
data/raw/*
```

---

# 🗄️ Supabase Setup

Create a Supabase project and open:

```text
Supabase Dashboard
        ↓
SQL Editor
        ↓
New Query
```

Run the following SQL.

## Create `scraped_pages`

```sql
CREATE TABLE scraped_pages (
    id BIGSERIAL PRIMARY KEY,
    url TEXT UNIQUE NOT NULL,
    title TEXT,
    description TEXT,
    industry TEXT,
    segment TEXT,
    scraped_at TIMESTAMPTZ DEFAULT NOW()
);
```

## Create `campaigns`

```sql
CREATE TABLE campaigns (
    id BIGSERIAL PRIMARY KEY,
    external_campaign_id TEXT,
    name TEXT NOT NULL,
    platform TEXT,
    objective TEXT,
    segment TEXT,
    headline TEXT,
    description TEXT,
    cta TEXT,
    status TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

## Create `campaign_metrics`

```sql
CREATE TABLE campaign_metrics (
    id BIGSERIAL PRIMARY KEY,
    external_campaign_id TEXT,
    impressions INTEGER DEFAULT 0,
    clicks INTEGER DEFAULT 0,
    conversions INTEGER DEFAULT 0,
    spend NUMERIC DEFAULT 0,
    ctr NUMERIC,
    cpc NUMERIC,
    conversion_rate NUMERIC,
    recorded_at TIMESTAMPTZ DEFAULT NOW()
);
```

---

# 🔒 Demo RLS Policies

For this demonstration, the following policies allow the application to insert and read data.

```sql
CREATE POLICY "Allow insert scraped pages"
ON public.scraped_pages
FOR INSERT
TO anon
WITH CHECK (true);

CREATE POLICY "Allow read scraped pages"
ON public.scraped_pages
FOR SELECT
TO anon
USING (true);

CREATE POLICY "Allow insert campaigns"
ON public.campaigns
FOR INSERT
TO anon
WITH CHECK (true);

CREATE POLICY "Allow read campaigns"
ON public.campaigns
FOR SELECT
TO anon
USING (true);

CREATE POLICY "Allow insert campaign metrics"
ON public.campaign_metrics
FOR INSERT
TO anon
WITH CHECK (true);

CREATE POLICY "Allow read campaign metrics"
ON public.campaign_metrics
FOR SELECT
TO anon
USING (true);
```

> **Production note:** These policies are intentionally broad for this demo. A production implementation should use authentication, least-privilege access, appropriate RLS policies, and protected server-side credentials.

---

# 🧪 Verify Supabase Connection

Before running the complete pipeline, verify that Python can communicate with Supabase.

Create `test_supabase.py`:

```python
from app.database.supabase_client import supabase


response = (
    supabase
    .table("scraped_pages")
    .select("*")
    .limit(1)
    .execute()
)

print("Supabase connection successful!")
print(response.data)
```

Run:

```cmd
python test_supabase.py
```

Expected result:

```text
Supabase connection successful!
[]
```

An existing list of records is also valid.

---

# 🧪 Run Tests

Run the test suite:

```cmd
pytest -q
```

Expected result:

```text
4 passed
```

The tests currently cover:

- Data cleaning
- Technology segmentation
- Financial Services segmentation
- Healthcare Services segmentation

---

# ▶️ Run the Pipeline

From the project root:

```cmd
python -m scripts.run_pipeline
```

### Important

Use:

```cmd
python -m scripts.run_pipeline
```

instead of:

```cmd
python scripts\run_pipeline.py
```

The module execution form correctly resolves the `app` package.

---

# 📊 Example Pipeline Output

A successful run looks like:

```text
============================================================
WEB DATA → CAMPAIGN AUTOMATION PIPELINE
============================================================

[1/7] Starting website scraping...
[SCRAPER] Scraping: https://example.com
[SCRAPER] Scraping: https://example.org
[SCRAPER] Collected 2 records.

[2/7] Cleaning data...
[DATA] Records after cleaning: 2

[3/7] Removing duplicates...
[DATA] Records after deduplication: 2

[4/7] Enriching and segmenting data...

[DATA] Processed records:
  URL       : https://example.com
  Title     : Example Domain
  Industry  : Technology
  Segment   : B2B Technology
------------------------------------------------------------
  URL       : https://example.org
  Title     : Example Domain
  Industry  : Technology
  Segment   : B2B Technology
------------------------------------------------------------

[5/7] Saving data to Supabase...
[DATABASE] Scraped data saved successfully.

[6/7] Creating campaigns...
[CAMPAIGN] Created: B2B Technology Campaign

[7/7] Collecting campaign metrics...
[METRICS] B2B Technology Campaign
  Impressions      : 10000
  Clicks           : 450
  Conversions      : 35
  Spend            : $180.0
  CTR              : 4.5%
  CPC              : $0.4
  Conversion Rate  : 7.78%

============================================================
PIPELINE COMPLETED SUCCESSFULLY
============================================================
```

---

# 🔄 Pipeline Components

## 1. Website Scraper

Location:

```text
app/scraper/website_scraper.py
```

Uses:

- `requests`
- `BeautifulSoup`

The scraper retrieves the HTML of the configured public URLs and extracts:

- URL
- Page title
- Meta description

Example:

```python
record = scraper.scrape(url)
```

---

## 2. Data Cleaning

Location:

```text
app/processing/cleaner.py
```

The cleaner:

- Normalizes URLs
- Removes unnecessary whitespace
- Normalizes title text
- Normalizes descriptions

Example:

```text
"  Test   Website  "
```

becomes:

```text
"Test Website"
```

---

## 3. Deduplication

Location:

```text
app/processing/deduplicator.py
```

Duplicate URLs are removed using a Python `set`.

This prevents the same page from being processed multiple times during a pipeline run.

---

## 4. Enrichment

Location:

```text
app/enrichment/enricher.py
```

The demo uses keyword-based classification.

Supported industries include:

```text
Technology
Finance
Healthcare
Education
Other
```

For example:

```text
software
cloud
AI
SaaS
cybersecurity
```

can result in:

```text
Technology
```

---

## 5. Audience Segmentation

Location:

```text
app/segmentation/segmenter.py
```

Industry classifications are mapped into audience segments:

| Industry | Segment |
|---|---|
| Technology | B2B Technology |
| Finance | Financial Services |
| Healthcare | Healthcare Services |
| Education | Education Services |
| Other | General Business |

---

# 🗄️ Database Layer

Location:

```text
app/database/supabase_client.py
```

The application stores processed data in three Supabase tables.

### `scraped_pages`

Stores website-level information:

```text
url
title
description
industry
segment
scraped_at
```

### `campaigns`

Stores generated campaign information:

```text
external_campaign_id
name
platform
objective
segment
headline
description
cta
status
created_at
```

### `campaign_metrics`

Stores campaign performance information:

```text
external_campaign_id
impressions
clicks
conversions
spend
ctr
cpc
conversion_rate
recorded_at
```

---

# 📢 Mock Campaign Platform

Location:

```text
app/campaign/mock_platform.py
```

The project intentionally uses a mock advertising platform.

It generates campaign information such as:

```text
Campaign Name
Platform
Objective
Audience Segment
Headline
Description
CTA
Status
```

Example:

```text
B2B Technology Campaign
```

The mock platform does **not**:

- connect to Google Ads
- connect to Meta Ads
- launch advertisements
- spend real money
- interact with real customer accounts

This keeps the demonstration safe and self-contained.

---

# 📈 Campaign Analytics

Location:

```text
app/analytics/metrics.py
```

The application calculates:

### Click-through rate

```text
CTR = clicks / impressions × 100
```

For the demo:

```text
450 / 10000 × 100 = 4.5%
```

### Cost per click

```text
CPC = spend / clicks
```

For the demo:

```text
180 / 450 = $0.40
```

### Conversion rate

```text
Conversion Rate = conversions / clicks × 100
```

For the demo:

```text
35 / 450 × 100 = 7.78%
```

---

# 📊 Demo Metrics

| Metric | Value |
|---|---:|
| Impressions | 10,000 |
| Clicks | 450 |
| Conversions | 35 |
| Spend | $180.00 |
| CTR | 4.50% |
| CPC | $0.40 |
| Conversion Rate | 7.78% |

These values are generated by the mock campaign platform and are **not real advertising performance data**.

---

# 🧩 Main Pipeline

The orchestration logic is located at:

```text
app/pipeline.py
```

The seven main stages are:

```text
1. Scrape
2. Clean
3. Deduplicate
4. Enrich + Segment
5. Save to Supabase
6. Create Mock Campaign
7. Calculate and Save Metrics
```

---

# 🔧 Configuration

The demonstration URLs are configured in:

```text
scripts/run_pipeline.py
```

Current demo URLs:

```python
urls = [
    "https://example.com",
    "https://example.org"
]
```

These are technical placeholder websites used only to demonstrate the pipeline.

For a real permitted-data demonstration, replace them with public websites that you are authorized to scrape.

---

# 🛡️ Responsible Scraping

This project is intended to demonstrate responsible public-web data collection.

Use only websites and data that you are permitted to access and collect.

### Do not:

- bypass authentication
- bypass CAPTCHAs
- bypass anti-bot protections
- circumvent rate limits
- scrape private areas
- collect unnecessary personal information
- attempt to evade website access controls

### Recommended practices:

- Respect applicable website terms and policies.
- Use reasonable request rates.
- Use request timeouts.
- Collect only the information required for the demonstration.
- Avoid sensitive personal information.
- Keep credentials out of source control.

---

# 🐛 Troubleshooting

## `ModuleNotFoundError: No module named 'app'`

Run the pipeline from the project root:

```cmd
python -m scripts.run_pipeline
```

Do not run:

```cmd
python scripts\run_pipeline.py
```

---

## Supabase RLS error

If you receive:

```text
new row violates row-level security policy
```

verify that the demonstration RLS policies have been created in the Supabase SQL Editor.

---

## Supabase credentials error

Check:

```text
.env
```

and make sure these variables are present:

```env
SUPABASE_URL=...
SUPABASE_KEY=...
```

Then run:

```cmd
python test_supabase.py
```

---

## Pandas DLL/Application Control error

Pandas is not required by this implementation.

The project uses native Python data structures:

```python
list
dict
set
```

This keeps the demo lightweight and avoids the Windows DLL restriction encountered during development.

---

# 🔒 Security

Never commit credentials.

Before pushing to GitHub, verify:

```text
.env
```

is listed in:

```text
.gitignore
```

Check the repository before pushing:

```cmd
git status
```

The `.env` file should not appear as a file ready to be committed.

---

# 🚀 Future Improvements

Although this repository is intentionally a demonstration, the architecture can be extended with:

- Configurable website sources
- More advanced HTML/content extraction
- robots.txt and policy-aware crawling
- Request rate limiting
- Retry/backoff handling
- Structured logging
- Better industry classification
- LLM-based enrichment
- Embedding-based audience segmentation
- Scheduled pipeline execution
- Data quality monitoring
- Dashboarding
- Authentication and stricter Supabase RLS
- Real advertising-platform APIs behind appropriate authorization
- Campaign A/B testing
- Automated performance optimization
- Production observability

---

# 📌 Current Demo Status

The complete pipeline has been successfully tested locally.

```text
Website Scraping       ✅
Data Cleaning          ✅
Deduplication          ✅
Enrichment             ✅
Segmentation           ✅
Supabase Integration   ✅
Campaign Generation    ✅
Campaign Metrics       ✅
Automated Tests        ✅
```

Test result:

```text
4 passed
```

Pipeline result:

```text
PIPELINE COMPLETED SUCCESSFULLY
```

---

# 👨‍💻 Author

**Vijaylal Bussa**

AI/Data Engineer | Generative AI & Agentic AI Specialist

- LinkedIn: https://linkedin.com/in/vijaylal-bussa
- GitHub: https://github.com/Vijaylal8055

---

## 📄 License

This project is intended as a technical demonstration and learning project.

Add an appropriate open-source license if the repository will be publicly distributed.
