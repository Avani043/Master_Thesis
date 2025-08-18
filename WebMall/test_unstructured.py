from unstructured.partition.html import partition_html

html_text = """
<html>
  <body>
    <h1>Welcome to WebMall</h1>
    <p>Here you can find laptops, phones, and accessories.</p>
    <a href="https://shop.com/laptops">Shop Laptops</a>
  </body>
</html>
"""

elements = partition_html(text=html_text)

for el in elements:
    print(el)