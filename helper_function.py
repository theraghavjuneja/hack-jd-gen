from IPython.display import Markdown
import textwrap

def to_markdown(text):
    """
    Converts the input text into Markdown format suitable for display in IPython environments.

    Parameters:
    - text (str): The input text to be converted to Markdown.

    Returns:
    - Markdown: A Markdown-formatted text wrapped in blockquotes ('> ') with bullet points ('*').

    Example:
    If 'text' is:
    '• Item 1\n• Item 2\n• Item 3'

    Output will be:
    Markdown('''
    > * Item 1
    > * Item 2
    > * Item 3
    ''')

    Explanation:
    - Replaces '•' with ' *' to format bullet points correctly.
    - Uses textwrap.indent with '> ' to create blockquotes in Markdown.
    - Returns a Markdown object that can be displayed in IPython environments using display().

    """
    text = text.replace('•', ' *')  # Replace bullet points with Markdown format '*'
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


