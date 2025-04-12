import json

dataset = []
current_id = None
current_sentiment = None
current_words = []
current_lang_markers = []

with open('dataset/Spanglish_dev.conll', 'r', encoding='utf-8') as f:
    for line in f:
        stripped_line = line.strip()
        if not stripped_line:
            continue  # Skip empty lines
        
        if stripped_line.startswith('meta') and len(stripped_line.split('\t')) ==3:
            # Save previous entry if exists
            if current_id is not None:
                dataset.append({
                    "id": current_id,
                    "sentence": ' '.join(current_words),
                    "language": ' '.join(current_lang_markers),
                    "sentiment_label": current_sentiment
                })
                current_words = []
                current_lang_markers = []
            
            # Parse meta information
            parts = stripped_line.split('\t')
            current_id = int(parts[1])
            current_sentiment = parts[2]
        else:
            # Extract word from line
            word,lang = stripped_line.split('\t')
            current_words.append(word)
            current_lang_markers.append(lang)
    
    # Add the last entry after loop ends
    if current_id is not None:
        dataset.append({
            "id": current_id,
            "sentence": ' '.join(current_words),
            "gold_label": current_sentiment
        })

# Save to JSON file
with open('spanglish_dataset.json', 'w', encoding='utf-8') as json_file:
    json.dump(dataset, json_file, ensure_ascii=False, indent=2)

print("Conversion successful! JSON file saved.")