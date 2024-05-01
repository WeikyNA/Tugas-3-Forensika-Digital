# Get the first page of the PDF
    page = pdf_reader.pages[0]

# Extract the hidden text (white-colored text)
    hidden_text = page.extract_text().strip()

# Decode and decrypt the hidden text using base64
    decrypted_message = base64.b64decode(hidden_text.encode()).decode()

return decrypted_message
