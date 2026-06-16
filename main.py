from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import MarkdownHeaderTextSplitter

# Semantic chunking with overlap
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
    separators=["\n\n", "\n", " ", ""]
)

# Header-aware chunking for structured documents
headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]
markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on
)
def create_rag_prompt(query, retrieved_documents):
    context = "\n\n".join([doc['text'] for doc in retrieved_documents])
    
    prompt_template = f"""You are a helpful assistant that answers questions based on the provided context.

Context:
{context}

Question: {query}

Instructions:
1. Answer the question using only information from the provided context
2. If the context doesn't contain relevant information, say "I don't have enough information to answer this question"
3. Cite specific parts of the context when possible
4. Provide a concise, accurate answer

Answer:"""
    
    return prompt_template
