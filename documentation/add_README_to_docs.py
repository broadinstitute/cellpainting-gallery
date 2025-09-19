import re

"""
Reads a Markdown file, extracts all tables, and writes them to a new file.
A table is identified by starting with a line that contains at least one pipe character (|).
Written with assistance from Gemini 2.5 Flash
"""
with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Regular expression to find Markdown tables
# It looks for lines starting and ending with a pipe character, including the header separator
table_pattern = re.compile(r'(\|.*?\n[\s]*\|[-|\s:]*\|[\s]*\n(?:\|.*?\n)*)')

tables = table_pattern.findall(content)

if not tables:
    print("Failed to .")

# Write the extracted tables to a new file
with open('documentation/complete_datasets.md', 'w', encoding='utf-8') as f:
    f.write(f"# Complete Datasets\n\n") # This adds the header and a blank line
    for table in tables:
        f.write(table.strip() + '\n\n') # strip() removes leading/trailing whitespace