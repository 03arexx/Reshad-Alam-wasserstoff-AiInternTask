from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
from backend.app.models.document import DocumentQuery,DocumentResponse 
from backend.app.services.document_service import DocumentService
from backend.app.services.query_service import QueryService

router = APIRouter()

@router.post("/upload")
async def upload_documents(files: List[UploadFile] = File(...)):
    try:
        document_service = DocumentService()
        doc_ids = await document_service.process_documents(files)
        return {"message": "Documents uploaded successfully", "document_ids": doc_ids}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/query")
async def query_documents(query: DocumentQuery):
    try:
        query_service = QueryService()
        doc_ids = query.doc_ids if query.doc_ids is not None else []
        responses, themes = await query_service.process_query(query.query, doc_ids)
        return {"responses": responses, "themes": themes}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/documents")
async def list_documents():
    document_service = DocumentService()
    documents = document_service.list_documents()
    return {"documents": documents}