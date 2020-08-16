from transformers import pipeline
from pprint import pprint

if __name__ == "__main__":
    ner = pipeline("ner", model="bert-base-multilingual-cased", grouped_entities=True)
    # tokenizer = BertTokenizer.from_pretrained("bert-base-multilingual-cased")
    text = "Kamarnya bau, air hangatnya gak nyala, acnya berisik, pembuangan kamar mandinya buntu. Plusnya drket tempat makan, busway"
    results = ner(text)
    pprint(results)
