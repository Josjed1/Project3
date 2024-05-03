from xml.etree import ElementTree as ET

def txt_to_html(txt_file, html_file):

  # Read text file content
  with open(txt_file, 'r', encoding='utf-8') as f:
    content = f.readlines()

  # Extract header and paragraph, since you will be having multiple articles the logic will
  # change for the code given below. 
  
  header = content[0].strip()
  paragraph = "".join(content[1:]).strip()

  # Create root element for HTML, try to remember the structure of a HTML file
  root = ET.Element("html")

  # Create head and body elements, try to understand how subElements works
  head = ET.SubElement(root, "head")
  title = ET.SubElement(head, "title")
  title.text = "My News Aggregation Site"
  body = ET.SubElement(root, "body")

  # Create header and paragraph elements in body
  h1 = ET.SubElement(body, "h1")
  h1.text = header
  p = ET.SubElement(body, "p")
  p.text = paragraph

  # Write HTML tree to file
  with open(html_file, 'ab') as f:
    tree = ET.ElementTree(root)
    tree.write(f, encoding='utf-8')
 
  print(f"Converted text file '{txt_file}' to HTML file '{html_file}'.")

