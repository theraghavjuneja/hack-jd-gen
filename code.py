from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import BeautifulSoupTransformer
import os

# Set user agent
os.environ['USER_AGENT'] = 'myagent'

# Load HTML
loader = AsyncChromiumLoader(["https://www.whereuelevate.com"])
html_documents = loader.load()
print(html_documents)
bs_transformer=BeautifulSoupTransformer()
docs_transformed=bs_transformer.transform_documents(html_documents,tags_to_extract=["span"])
# print(html_documents)
print(docs_transformed)
with open('html_documents.txt', 'w') as f:
    f.write(str(html_documents))

with open('docs_transformed.txt', 'w') as f:
    f.write(str(docs_transformed))
docs_transformed[0].page_content[0:500]
