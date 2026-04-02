from supabase import create_client, Client

project_url = "https://agyepafauyuyfpjqname.supabase.co"
api_key = "sb_publishable_Oeu19J0SNtnJ3qg2-W3S4g_asAmryd0"

supabase: Client = create_client(project_url, api_key)

# Create embeddings
embedding = [0.99, 0.78, 0.60, -0.17, -0.76]

# document-1 embedding: [0.21, 0.14, -0.06, 0.75, 0.51]
# document-2 embedding: [0.19, 0.11, -0.01, 0.80, 0.55]

document = {
    "id" : 3,
    "title" : "HTML, CSS & Javascript",
    "content" : "HTML, css & JS are used for frontend tech stack",
    "category" : "frontend",
    "embedding" : embedding
}

supabase.table("documents").insert(document).execute()


