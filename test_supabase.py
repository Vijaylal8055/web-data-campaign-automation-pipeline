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
