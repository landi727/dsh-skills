# HTML Delivery Contract

## Portable file structure

Use this default shape, simplifying it for a narrow request:

| Path | Purpose |
| --- | --- |
| index.html | Complete composed example with sample text; main entry |
| modules/<module-id>.html | Each module as an independently openable HTML document |
| styles/tokens.css | Scoped style-family tokens derived from the reference |
| styles/modules.css | Namespaced reusable module styles |
| assets/ | Local images, textures, edge artwork and permitted font files |
| template-manifest.json | Style provenance, module/field IDs, extension and assembly rules |

Keep all meaningful content directly in HTML. Make each standalone module's marked section copyable into the composed example. Use the same shared CSS in both views and verify they stay consistent. Do not introduce a runtime module loader, fetch-based HTML includes or iframe composition. Default to no JavaScript; add it only for an actual requested behavior.

Use relative paths adjusted for each document's depth. Avoid external fonts, CDNs, remote image links and hosted preview URLs. Ensure pages can open through file:// without a build step or web server. Include only assets that can be delivered legitimately. Record an explicit fallback for unavailable fonts.

Scope tokens and component classes to the template family. Keep module styles independent of their demo position. Avoid nth-child styling as a content-placement contract, global heading resets, and duplicate IDs when modules are repeated. Use stable data-module and data-field attributes for reusable blocks and editable slots. Preserve supplied contentRef values when present; do not require a new content schema or add database code.

Keep images and captions as separate fields. Use reference-derived image aspect ratios and object positioning. Choose a template's responsive behavior deliberately: preserve its desktop/source composition and provide a readable narrow preview, or a clearly fitted fixed-width export view. Keep responsive reflow out of a fixed-width export unless explicitly desired.

## Height and layer mechanics

Use normal document flow for headings, paragraphs, images that affect height, and following sections. Avoid fixed body heights, text clipping, line clamping and absolute-positioned body copy. Support wrapping of long titles and unbroken strings.

| Region | Behavior |
| --- | --- |
| Top cap | Keep edge shape and artwork at fixed proportions; reserve title padding |
| Body surface | Grow with content; fill with solid color, suitable repeating texture or vector edge |
| Side edges | Extend vertically with repeat-safe artwork or structural CSS/vector strokes |
| Bottom cap | Follow content in flow or anchor to container bottom with reserved padding |
| Decoration | Preserve size; anchor to a relevant corner/region and reserve a text-safe zone |
| Main image | Keep aspect ratio; specify crop or fit independently of body height |
| Connector | Keep local to a module boundary or define compatible neighbor types |

Choose the simplest faithful implementation per frame: a CSS border for plain frames, cap/body/cap for torn paper, or border-image with suitable repeat semantics for textured edges. Do not stretch an entire paper bitmap vertically. Do not tile conspicuous creases, labels or torn corners through the body. Inspect cap/body joins at both short and long heights.

For overlapped images, reserve sufficient layout space so subsequent text and sections move correctly. Avoid arrows with page-global coordinates. Build joins with explicit padding, overlap or compatible boundary variants so removing a module does not strand a connector.

Keep fixed brand protection zones clear. A taller body should move the ending down through document flow, preserving its internal logo geometry. Long cover titles should wrap within their allocated region or trigger a stated capacity limit, never silently shrink protected brand elements.

## Manifest content

Write valid JSON with a real serializer. Keep it small and descriptive; it documents the delivered HTML rather than operating as an unrequested runtime engine.

Include:

- Template family ID, reference filenames or user-provided identifiers, source width and display assumptions.
- Frozen brand/style rules and known approximations.
- Per-module ID, HTML path, reference region, editable field selectors and local assets.
- Fixed/flexible parts, height strategy, decoration anchors and text capacity guidance.
- Compatible predecessor/successor roles and optional boundary variants.
- Which sample modules may be repeated, removed or reordered safely.

Do not imply an integration was tested merely because the manifest exists.

## Practical verification

Use a browser tool or Playwright available in the environment. Inspect screenshots as well as DOM geometry. Keep tests focused on the promised modules and local-file behavior.

1. Open index.html and every standalone module through file://; confirm styles, images and fonts load. Scan HTML and CSS resource references for missing files and external dependencies; parse JSON with a JSON parser.
2. Inspect each module at the intended source width and the composed page at a representative phone width. Check text visibility, asset crops, protected zones and unintended horizontal overflow. Compare the original reference to both views.
3. For each distinct flexible-frame implementation, render short, representative and approximately triple-length sample copy. Verify height growth, bottom-cap movement, image proportions, text-safe zones and natural displacement of the next module. Inspect joins and repetition artifacts visually.
4. Exercise a wrapping heading, a long token, an optional missing image, a repeated body block, and removal/reordering of compatible modules. Check for duplicate IDs, orphaned connectors and inconsistent section spacing.
5. Inspect the full composed long image for density and rhythm. An overflow-free page can still fail visually through monotonous framing, weak hierarchy or excessive uninterrupted body length. Set split guidance accordingly.

Use temporary test copies or browser DOM mutations; restore the delivered sample content afterward. State actual test coverage and remaining limits. Browser canvas limits and export slicing are separate from document height; do not promise unlimited single-bitmap export. Deliver an export pipeline only when requested.
