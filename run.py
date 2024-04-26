# Import necessary modules
from module_1.data_processor import DataProcessor
from module_2.data_collector import DataCollector
from module_3 import generate_summary
from openai import OpenAI

# Set the URL to collect data from
url = 'https://www.foxnews.com/world/us-taxpayer-funded-un-agencys-long-history-enabling-hamas-exposed'

# API key for OpenAI
api_key = "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"

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

def main():
    # Use data collector to fetch data from the URL
    data_collector = DataCollector()
    raw_data = data_collector.collect_data(url)
    
    # Call raw print function
    raw_print(raw_data)
    
    # Use data processor to process the raw data
    data_processor = DataProcessor()
    processed_data = data_processor.process_data(url)
    
    # Call process print function
    process_print(processed_data)
    
    # Generate summary using processed data
    summary = generate_summary(processed_data)
    print(summary)
    
    # Save summary to file
    save_summary(str(summary))



def raw_print(raw_data):
    # Save raw data to the 'raw' folder
    raw_file_path = 'Data/raw/raw_filename.txt'
    with open(raw_file_path, 'w') as raw_file:
        raw_file.write(raw_data)
        
def process_print(processed_data):
    # Save processed data to the 'processed' folder
    processed_file_path = 'Data/processed/processed_filename.txt'
    with open(processed_file_path, 'w') as processed_file:
        processed_file.write(processed_data)
        
def save_summary(summary):
    # Save summary to 'generated' folder
    file_path = 'Data/generated/generated.txt'
    with open(file_path, 'w') as summary_file:
        summary_file.write(summary)

if __name__ == "__main__":
    main()