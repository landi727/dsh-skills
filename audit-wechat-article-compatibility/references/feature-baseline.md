# Feature review baseline

Use this as a risk-routing guide. Current first-party rules and real-route tests take precedence.

## Static images and baked text

- Treat uploaded raster images as the safest base for image-led longform.
- Verify actual post-upload sharpness, mobile reading size, crop, transparency, color shift, and top/bottom seams.
- Keep production text editable upstream when useful; audit the final PNG/JPG/GIF that enters WeChat.
- Avoid relying on external image URLs. Confirm that the saved draft uses resources accepted by the final WeChat route.
- Check that critical text is readable without zoom and remains present when optional motion is unavailable.

## GIF

- Treat GIF as conditional enhancement until the final uploaded file passes preview.
- Put complete essential information in the first frame or a persistent layer.
- Test first-load state, animation start, loop, duration, frame order, compression damage, dropped frames, and low-performance behavior.
- Replace long or heavy sequences with a shorter loop, fewer frames, or a static frame when motion does not carry essential meaning.
- Keep module joins stable when the GIF's rendered dimensions differ from its local preview.

## SVG and CSS interaction

- Treat imported SVG, SVG animation, CSS animation, tap-state changes, and reveal effects as conditional.
- Inspect the saved/reopened draft because unsupported markup or attributes may be cleaned.
- Keep essential copy and actions visible in the initial or static state.
- Provide a static-image or GIF fallback for decorative animation.
- Do not generalize from one published SVG article to a different editor, account, source, or date.
- Record which exact gestures are required. Hover is not a mobile interaction.

## JavaScript, iframe, custom players, and web-page behavior

- Do not plan JavaScript, iframe content, a custom player, arbitrary web forms, or local-browser scroll logic as the article's main implementation without E3 proof through the final route.
- Treat scroll-triggered effects, internal anchors, and other browser-page behaviors as `应降级` when essential reading depends on them.
- Preserve the experience with ordered static modules, GIF, platform-native cards, or visible links.

## Native video and audio

- Treat native media as a platform-controlled component. Do not assume autoplay, custom controls, silent playback, looping, or seamless full-bleed styling.
- Verify insertion permission, poster, tap behavior, playback, return position, caption visibility, and layout on both mobile systems.
- Supply a poster and nearby summary that communicate the point before playback.
- When visual continuity is more important than playback, use a short GIF for optional motion and place full media behind a visible native route.

## Links, tap areas, and mini-program entry points

- Treat external links, image links, mini-program cards, and other destinations as account- and route-dependent.
- Verify the account permission, saved destination, client behavior, and return path.
- Use a visible label or platform-native entry. Do not rely on an invisible or transparent hot area for a critical action.
- Test tap-target position after save/reopen and on both mobile systems.
- Give the reader a visible destination name, account name, QR code, or other suitable fallback when the route is optional and may be unavailable.

## Continuous long-image modules

- Test the actual saved draft for gaps, hairlines, unexpected margins, scaling differences, transparent-edge artifacts, and module reordering.
- Check the full article at normal reading scale and inspect joins at high zoom.
- Keep top and bottom transition artwork inside each exported asset. Do not rely only on local negative margins or browser-specific overlap.
- Verify long-page loading order and ensure delayed modules do not leave critical context stranded.

## Local HTML and third-party editors

- Use local HTML/CSS for production and editable layout when useful, while treating it as an upstream source.
- Compare three states separately: local render, WeChat saved/reopened draft, and device preview.
- Audit the transformed state after copy/import. Never infer that browser support equals article support.
- When a package references remote assets, confirm that every required asset is available and transferred through the final route.
