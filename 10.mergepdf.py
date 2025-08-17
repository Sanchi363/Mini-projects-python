# Using pypdf module.
import pypdf as p
merger=p.PdfWriter()
pdf=["Clutter/SJF.pdf","Clutter/SJF with given arrival time.pdf"]
for i in pdf:
    merger.append(i)
merger.write("Merged.pdf")
merger.close()