from firecrawl import FirecrawlApp
from decouple import config
from time import perf_counter

app = FirecrawlApp(api_key=config("FIRECRAWL_API_KEY"))

start_time = perf_counter()
batch_scrape_result = app.batch_scrape_urls(['https://firecrawl.dev', 'https://mendable.ai'], formats=['links'], only_main_content=True)
end_time = perf_counter()
# Create a new file to store the batch scrape results
with open('data/batch_scrape_records.py', 'w') as f:
    f.write('batch_scrape_records = [\n')
    
    # Process each result in the batch scrape
    for i, result in enumerate(batch_scrape_result.data, 1):
        # Extract the markdown content from the result
        markdown_content = result.links
        
        # Create a record with similar structure to pinecone_records
        record = {
            '_id': f'batch_rec{i}',
            'chunk_text': markdown_content,
            'category': 'web_content'  # Default category for batch scraped content
        }
        
        # Write the record to the file with proper formatting
        f.write(f'{str(record)},\n')
    f.write(']\n')

print(f"Time taken: {end_time - start_time} seconds")
print(batch_scrape_result)



# (async) You can then use the job ID to check the status of the batch scrape:
# batch_scrape_status = app.check_batch_scrape_status("ad7e5581-5baa-4cfd-a67c-bda851976d41")
# print(batch_scrape_status.data)