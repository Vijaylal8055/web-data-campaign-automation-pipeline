from app.pipeline import run_pipeline


if __name__ == "__main__":

    urls = [
        "https://example.com",
        "https://example.org"
    ]

    run_pipeline(urls)
    