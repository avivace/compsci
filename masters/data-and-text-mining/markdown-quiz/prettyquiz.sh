echo "Running scraper"
python3 scrape.py
echo "Running the template compiler"
python3 compile.py
echo "Running pandoc"
pandoc template.md -o template.pdf
