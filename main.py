# Copy pages and metadata from the input PDF to the output PDF
for page in pdf_reader.pages:
    pdf_writer.add_page(page)

# Update metadata
    pdf_writer.add_metadata(new_metadata)

# Write the updated metadata to the output PDF file
with open(output_pdf, 'wb') as output_file:
    pdf_writer.write(output_file)
