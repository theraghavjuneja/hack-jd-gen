from langchain_community.document_loaders import AsyncChromiumLoader
from langchain.document_transformers import BeautifulSoupTransformer
loader = AsyncChromiumLoader(["https://www.wsj.com"])
html = loader.load()