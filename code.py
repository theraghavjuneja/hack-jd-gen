from langchain_community.document_loaders import AsyncChromiumLoader
import os

# Set user agent
os.environ['USER_AGENT'] = 'myagent'

# Load HTML
loader = AsyncChromiumLoader(["https://www.whereuelevate.com"])
html_documents = loader.load()

# Print the first document to inspect its structure
if html_documents:
    print(html_documents[0])  # Print the first document object
    # Optionally, print the attributes of the first document
    print(dir(html_documents[0]))

# Exit the script after printing
exit()
