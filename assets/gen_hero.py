#!/usr/bin/env python3
"""Generate the profile hero SVG in light and dark variants from one geometry source."""
import os

W, H = 960, 150
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'DejaVu Sans Mono', monospace"

THEMES = {
    "light": dict(surface="#FFFFFF", ink="#0F172A", muted="#64748B", accent="#B45309", rule="#E2E8F0"),
    "dark":  dict(surface="#0D1117", ink="#E6EDF3", muted="#8B949E", accent="#E8A33D", rule="#21262D"),
}

# ---- handwritten expression: authored strokes, no font involved -------------
# integral sign: top hook right, long lean, bottom hook left
HAND = [
    ("M 118 47 C 118 33 102 31 100 46 C 97 66 95 86 93 106 C 91 120 76 121 76 107", 3.6),
    # subscript 0
    ("M 128 106 C 134 105 138 111 138 118 C 138 125 134 130 128 130 C 122 130 118 125 118 118 C 118 111 122 106 128 106", 2.4),
    # superscript 1
    ("M 122 47 L 128 41 L 128 68", 2.4),
    # x  (first)
    ("M 160 76 C 169 86 179 95 187 103", 3.4),
    ("M 187 76 C 179 86 169 95 160 103", 3.4),
    # superscript 2
    ("M 194 62 C 196 55 207 54 208 62 C 209 70 198 75 193 82 L 209 82", 2.4),
    # d : bowl + ascender
    ("M 250 80 C 242 74 230 78 228 89 C 226 100 235 107 243 102 C 248 99 250 92 251 84", 3.4),
    ("M 253 52 C 251 70 249 90 249 99 C 249 104 253 106 258 103", 3.4),
    # x  (second) — kerned tight against the d, as "dx" is one unit
    ("M 266 76 C 275 86 285 95 293 103", 3.4),
    ("M 293 76 C 285 86 275 95 266 103", 3.4),
]

# ---- LaTeX token strip: amber = structural, ink = content -------------------
FS = 26
ADV = 15.6
X0 = 530
BASE = 100  # optically aligned with the handwritten baseline, not with the box
TOKENS = [  # (text, n_chars_before, role)
    ("\\int_{", 0,  "accent"),
    ("0",       6,  "ink"),
    ("}^{",     7,  "accent"),
    ("1",       10, "ink"),
    ("}",       11, "accent"),
    ("x",       13, "ink"),
    ("^{",      14, "accent"),
    ("2",       16, "ink"),
    ("}",       17, "accent"),
    ("\\,",     18, "accent"),
    ("dx",      20, "ink"),
]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build(theme):
    t = THEMES[theme]
    o = []
    o.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
             f'role="img" aria-label="A handwritten integral expression transformed into its LaTeX token sequence">')
    o.append(f'<rect width="{W}" height="{H}" fill="{t["surface"]}"/>')

    # hairline baseline under the whole strip
    o.append(f'<rect x="0" y="{H-1}" width="{W}" height="1" fill="{t["rule"]}"/>')

    # --- left: handwriting in ink — this is the human's input, so it reads as pen
    o.append('<g transform="rotate(-1.2 190 90)" fill="none" stroke-linecap="round" stroke-linejoin="round">')
    for d, sw in HAND:
        o.append(f'  <path d="{d}" stroke="{t["ink"]}" stroke-width="{sw}"/>')
    o.append('</g>')

    # --- middle: the transformation arrow + what performs it. Amber from here on:
    #     one colour, one meaning — machine-produced structure.
    o.append(f'<text x="425" y="72" font-family="{MONO}" font-size="12" letter-spacing="2.5" '
             f'fill="{t["accent"]}" text-anchor="middle" textLength="52" '
             f'lengthAdjust="spacingAndGlyphs">HMER</text>')
    o.append(f'<path d="M 372 90 L 470 90" stroke="{t["accent"]}" stroke-width="1.5"/>')
    o.append(f'<path d="M 462 84 L 471 90 L 462 96" stroke="{t["accent"]}" stroke-width="1.5" '
             f'fill="none" stroke-linecap="round" stroke-linejoin="round"/>')

    # --- right: LaTeX tokens, coloured by structural vs content
    for text, before, role in TOKENS:
        x = X0 + ADV * before
        tl = ADV * len(text)
        o.append(f'<text x="{x:.1f}" y="{BASE}" font-family="{MONO}" font-size="{FS}" '
                 f'fill="{t[role]}" textLength="{tl:.1f}" lengthAdjust="spacingAndGlyphs" '
                 f'xml:space="preserve">{esc(text)}</text>')

    o.append('</svg>')
    return "\n".join(o) + "\n"


dest = "/home/purin-xeon/Documents/Purin1410/assets"
os.makedirs(dest, exist_ok=True)
for name in THEMES:
    p = os.path.join(dest, f"hero-{name}.svg")
    open(p, "w", encoding="utf-8").write(build(name))
    print("wrote", p)
