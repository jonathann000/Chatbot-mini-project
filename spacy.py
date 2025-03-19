import spacy
nlp = spacy.load("sv_core_news_sm")

def extract_location(text):
    doc = nlp(text)
    locations = [ent.text for ent in doc.ents if ent.label_ == "GPE"]  # GPE (Geopolitical entity) includes cities, countries, etc.
    return locations

test_text = "Jag bor i Göteborg och jag älskar att äta sushi."
print(extract_location(test_text))  # Output: ['Göteborg']