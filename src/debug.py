import os

# Absolute path to your supposed file
data_path = r"C:\Users\kimnd\OneDrive\Desktop\wordcloud-nlp\data\reviews.txt"

print("File exists?", os.path.exists(data_path))

with open(data_path, "r", encoding="utf-8") as f:
    text = f.read()

print("Length of text:", len(text))
print("First 100 characters:", text[:100])
