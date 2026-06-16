import numpy as np
from sentence_transformers import SentenceTransformer

# Initialize embedding model
model = SentenceTransformer('BAAI/bge-large-en-v1.5')

# Generate embeddings for document chunks
documents = ["First document text...", "Second document text..."]
embeddings = model.encode(documents, normalize_embeddings=True)

# Store embeddings efficiently
import pickle
with open('embeddings.pkl', 'wb') as f:
    pickle.dump({'documents': documents, 'embeddings': embeddings}, f)
