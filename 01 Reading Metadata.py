from PyPDF2 import PdfReader

reader = PdfReader("sample.pdf")

meta = reader.metadata

print(len(reader.pages))

print(f"""
Author  : {meta.author}
Creator : {meta.creator}
Producer: {meta.producer}
Subject : {meta.subject}
Title   : {meta.title}
""")
