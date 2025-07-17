import json
import os

def match_examples(job_role):
    data_path = os.path.join(os.path.dirname(__file__), '../data/curated_examples.json')
    with open(data_path, 'r', encoding='utf-8') as f:
        examples = json.load(f)
    return examples.get(job_role, []) 