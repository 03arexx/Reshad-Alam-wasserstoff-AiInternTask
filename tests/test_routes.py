from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wasserstoff Gen-AI Chatbot API"}

def test_upload_documents():
    # Note: Requires a sample PDF file for testing
    response = client.post("/api/upload", files={})
    assert response.status_code == 422  # Expect failure due to no files

def test_list_documents():
    response = client.get("/api/documents")
    assert response.status_code == 200
    assert "documents" in response.json()