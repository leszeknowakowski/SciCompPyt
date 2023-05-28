import os

path = "D:\OneDrive - Uniwersytet Jagielloński\Studia\doktorat\\2 rok\SciCompPy\lesson5\homework"

size=[]
def    find_pdf_size(top):
    for root, dirs, files in os.walk(top):  # walking top-down (default)
        for name in files:
           if name.lower().endswith(".pdf"):
               pdf_size = os.path.getsize(os.path.join(root, name))
               size.append(pdf_size)
               print("{} consumes {} bytes".format(name, pdf_size))
    print("all pdf files in directory {} consume {} bytes".format(top, (sum(size))))


find_pdf_size(path)