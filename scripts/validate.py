#!/usr/bin/env python3
"""Dependency-free public-fixture validation; not a visual fashion benchmark."""
import json
from pathlib import Path

TASTES = {'liked', 'disliked', 'neutral', 'unknown'}
OWNERSHIP = {'owned', 'needed', 'redundant', 'unknown'}

def validate_match(item):
    assert item['taste'] in TASTES, 'invalid taste'
    assert item['ownership'] in OWNERSHIP, 'invalid ownership'
    assert item['decision'] in {'buy', 'try', 'only_if', 'skip'}, 'invalid decision'
    assert item['price']['amount'] >= 0, 'negative price'
    assert len(item['price']['currency']) == 3, 'currency must be explicit'
    assert item['stock']['branch'] in {'unknown', 'in_stock', 'out_of_stock'}, 'invalid branch stock'
    assert item['source_url'].startswith('https://'), 'source must be https'
    if item['reason'] == 'already_owned':
        assert item['ownership'] == 'owned', 'ownership feedback must remain separate'
    if item.get('pickup_confirmed'):
        assert item['stock']['branch'] == 'in_stock' and item.get('branch_confirmation_source'), 'pickup needs branch evidence'
    if item.get('image_kind') == 'ai':
        assert item.get('approximation_label') and not item.get('fit_proven'), 'AI cannot prove fit'
    return True

def main():
    root=Path(__file__).resolve().parents[1]
    rows=[json.loads(x) for x in (root/'examples/catalog_matches.jsonl').read_text().splitlines() if x]
    for row in rows:
        validate_match(row)
        assert row['synthetic'] is True
        assert row['source_url'].startswith('https://example.com/')
    skill=(root/'skills/fashion-atlas/SKILL.md').read_text()
    assert skill.startswith('---\nname: fashion-atlas\n')
    print(f'PASS: {len(rows)} synthetic fixtures and skill frontmatter; no live visual benchmark claimed.')
if __name__=='__main__': main()
