import spacy
from spacy.matcher import Matcher

def expand_location(token):
    """ Expands a detected location by including adjacent PROPN or ADJ tokens. """
    location_tokens = [token]
    
    # Check tokens to the right
    next_token = token.nbor(1) if token.i + 1 < len(token.doc) else None
    while next_token and (next_token.pos_ in ["PROPN", "ADJ", "NOUN"]):
        location_tokens.append(next_token)
        next_token = next_token.nbor(1) if next_token.i + 1 < len(next_token.doc) else None
    
    return " ".join([t.text for t in location_tokens])

def preprocess_text(text):
    """ Capitalizes words in key positions (after 'to' and 'from') to improve NER recognition. """
    words = text.split()
    for i, word in enumerate(words):
        if word.lower() in ["to", "from"] and i + 1 < len(words):
            words[i + 1] = words[i + 1].capitalize()  # Force capitalization
    return " ".join(words)


def nlp_app(text):
    nlp = spacy.load("en_core_web_sm")

    
    text = preprocess_text(text)
    doc = nlp(text)

    matcher = Matcher(nlp.vocab)

    pattern_from = [{"LOWER": "from"}, {"POS": "PROPN"}]  # English
    pattern_to = [{"LOWER": "to"}, {"POS": "PROPN"}]  # English

    matcher.add("FROM_LOCATION", [pattern_from])
    matcher.add("TO_DESTINATION", [pattern_to])


    matches = matcher(doc)

    location = None
    destination = None

    for match_id, start, end in matches:
        match_text = doc[start + 1]
        expanded_name = expand_location(match_text)  # Expand multi-word locations
        label = nlp.vocab.strings[match_id]
        if label == "FROM_LOCATION":
            location = expanded_name
        elif label == "TO_DESTINATION":
            destination = expanded_name

    #print(f"Location: {location}")
    #print(f"Destination: {destination}")
    return location, destination

def nlp_location(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    location = None
    # Iterate over named entities recognized by SpaCy
    for ent in doc.ents:
        # If the entity is a proper noun and recognized as a location (GPE)
        if ent.label_ == "GPE" or ent.label_ == "LOC":  # GPE (Geopolitical Entity) LOC location
            location = ent.text
            #location = expand_location(ent)  # Expand multi-word locations
            break  # We just want the first location, so break after finding it
    return location