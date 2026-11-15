# Fashion Atlas

A portable, evidence-first fashion research skill: **reference → taste → wardrobe gap → catalog → complete outfit → buy/skip decision**.

Fashion Atlas builds on [googlarz/fashion-skill](https://github.com/googlarz/fashion-skill), with attribution and substantial changes. It is an independent adaptation, not an endorsed successor. Upstream inspected at `da3224bba51dfb7e14e30f1e147865d5476cd4a6` (2026-05-18); this initial version does not claim to outperform it in live shopping.

## What changes
- Separate aesthetic preference, ownership, fit, budget and availability. “No” is not automatically “I dislike it.”
- Extract silhouette, panel construction, texture and outfit proportions from actual reference images, not brand keywords alone.
- Search broadly with multilingual descriptors; compare real reference and product images before generating try-ons.
- Show full pants, footwear and useful belt-on/belt-off variants. Never fabricate details that a real product lacks.
- Treat branch stock, garment measurements, international/local prices and travel time as independent evidence.
- Keep private profile/photos separate from the public skill and use synthetic examples.
- Turn corrections into dated, reversible evidence, not universal rules.

## Use
1. Read `skills/fashion-atlas/SKILL.md` in your agent, or copy its folder into your agent's supported skill directory.
2. Copy `templates/` into a **private location outside this repository**. Fill only relevant fields; unknown is valid.
3. Give the agent authorized reference photos and the task. Start with 3–6 contrasting references and known-owned items.
4. Require a reference-vs-candidate contact sheet, match explanation and verification gaps before a shortlist.

No API, paid service, model download, scheduled job or browser login is required. Browse/image generation/calendar capabilities depend on the host; if unavailable, report the limit. No integration is installed automatically.

## Modes
Wardrobe intake/import; reference taste analysis; outfit planning; pre-purchase review; in-store dry run; capsule/trip route; optional price/new-arrival monitoring; seasonal rotation; resale drafting. See [modes](skills/fashion-atlas/references/modes.md).

## Validation
`python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v`

These validate data and decision invariants on synthetic fixtures. They do not prove visual understanding, fit accuracy, live availability or improved personal taste. Optional retrieval engines: [FashionCLIP](https://github.com/patrickjohncyh/fashion-clip), [Marqo FashionCLIP](https://github.com/marqo-ai/marqo-FashionCLIP). No engine is bundled or benchmarked here.

## Privacy / licenses
No user photos, measurements, receipts, account data, private itineraries or credentials belong in this repo. Use links to third-party product imagery rather than republishing without permission. Skill/docs: CC BY 4.0; original small Python validation code: MIT. See [NOTICE](NOTICE.md).
