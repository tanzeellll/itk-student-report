import pdfkit

pdfkit.config.default_options[:ignore_load_errors] = True

with open('index.html') as f:
    pdfkit.from_file(f, 'out.pdf')
