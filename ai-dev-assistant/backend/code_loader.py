import os

# Code Loader (Read Entire Project)
# Purpose:
# ✔ reads all project files
# ✔ sends them to AI

def load_code_files(folder):

    code_chunks = []

    for root, dirs, files in os.walk(folder):

        for file in files:

            if file.endswith(".py"):

                path = os.path.join(root, file)

                with open(path, "r", encoding="utf-8") as f:

                    content = f.read()

                code_chunks.append({
                    "file": file,
                    "content": content
                })

    return code_chunks