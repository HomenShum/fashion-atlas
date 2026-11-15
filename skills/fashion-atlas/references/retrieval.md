# Retrieval and ensemble protocol

## Reusable search profile
For each reference store: category, source image URL, inspected views, frame descriptors, construction descriptors, texture, palette, desired outfit role, must-have cues, avoid cues and unknowns. Example structural terms: articulated knees, curved panel seams, sculpted flare, cropped boxy jacket, compact fitted tee, barrel twill, lantern nylon, stacked dance sweatpants. Translate terms, not assumed brand equivalence.

Separate three lanes: exact/near visual analogues; complementary outfit anchors; practical replacements. Do not label a plain anchor as a statement substitute. Color-only and category-only retrieval are weak baselines.

## Broadening intelligently
Search official designer catalogs and regional-language categories; inspect collections beyond search-engine snippets; inspect similar item silhouettes and stockist designers; use reverse image tools only if available and permitted. Expand to another region when local match/price/stock is weak, but retain travel feasibility. Track examined vs unexamined catalogs rather than claim exhaustive coverage.

Optional FashionCLIP/Marqo embeddings can retrieve candidates, but require separately audited installation, model license, resource budget and privacy review. Do not send private images to a third-party endpoint just because a model exists. No embedding model is installed here. Rerank by evidence, ownership, proportions and outfit compatibility; cosine similarity is not a purchase decision.

## Independent researchers
Give workers the same references, constraints and correction log. Ask each to return exact sources, inspected images, disagreements and unknowns. Record actual model/tool and whether it ran; unavailable requested models are not silently replaced. Deduplicate products; independently verify strongest claims. Ensemble agreement is not evidence if all repeat the same source. Keep a revision log explaining what changed and why.
