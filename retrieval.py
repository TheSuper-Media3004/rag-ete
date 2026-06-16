import qdrant_client
from qdrant_client.models import Distance, VectorParams, PointStruct

# Initialize vector store
client = qdrant_client.QdrantClient(location=":memory:")
client.create_collection(
    collection_name="documents",
    vectors_config=VectorParams(size=768, distance=Distance.COSINE)
)

# Store vectors with metadata
points = [
    PointStruct(
        id=idx,
        vector=embedding.tolist(),
        payload={"text": text, "source": source, "chunk_id": idx}
    )
    for idx, (text, embedding) in enumerate(zip(texts, embeddings))
]
client.upsert(collection_name="documents", points=points)

# Retrieve relevant chunks
from qdrant_client.models import Filter, FieldCondition, MatchValue

def retrieve_relevant_chunks(query, top_k=5, filters=None):
    query_embedding = model.encode([query])[0]
    search_result = client.search(
        collection_name="documents",
        query_vector=query_embedding.tolist(),
        query_filter=filters,
        limit=top_k
    )
    return [hit.payload for hit in search_result]
