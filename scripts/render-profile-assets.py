"""Generate dependency-free SVG assets for the GitHub profile's two themes."""
from html import escape
from pathlib import Path
from textwrap import wrap

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
PALETTES = {
    'light': dict(ink='#20242b', muted='#59636e', faint='#d1d9e0', accent='#bb482f'),
    'dark': dict(ink='#f0f3f6', muted='#b1bac4', faint='#454c56', accent='#f6a18b'),
}
PROJECTS = [
    ('BurnBox', 'File sharing, with an off switch.', 'Private storage. Expiring, revocable links.', '01'),
    ('VeilHub', 'A little privacy between links.', 'Self-hosted redirects. Encrypted destinations.', '02'),
    ('Arclane', 'Routes you can reason about.', 'Routing policies and compatibility research.', '03'),
    ('TradeMind', 'From market data to a readable report.', 'Equities, indicators, and backtest calculations.', '04'),
    ('RealCarrier', 'Find the carrier behind the number.', 'U.S. carrier, type, and portability lookup.', '05'),
    ('esimswap', 'Make that eSIM QR code work.', 'Parse, generate, and repair in your browser.', '06'),
]
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"


def svg(width, height, title, desc, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
  <title id="title">{escape(title)}</title>
  <desc id="desc">{escape(desc)}</desc>
  <g font-family="{FONT}">{body}</g>
</svg>
'''


PROJECT_SUMMARIES = {
    'BurnBox': 'Private file sharing with expiring, revocable links.',
    'VeilHub': 'Self-hosted redirects with encrypted destinations.',
    'Arclane': 'Routing policies and compatibility research.',
    'TradeMind': 'Market reports, indicators, and backtest calculations.',
    'RealCarrier': 'U.S. carrier, line type, and portability lookup.',
    'esimswap': 'Parse, generate, and repair eSIM QR codes in your browser.',
}


def project(c, name, line1, line2, number):
    lines = wrap(PROJECT_SUMMARIES[name], 39)
    description = ''.join(f'<text x="18" y="{65+i*25}" fill="{c["ink"]}" font-size="18">{escape(line)}</text>' for i, line in enumerate(lines))
    body = f'''<rect x=".5" y=".5" width="389" height="115" rx="8" fill="{c['accent']}" fill-opacity=".025" stroke="{c['faint']}" stroke-opacity=".7"/>
    <text x="18" y="33" fill="{c['ink']}" font-size="22" font-weight="600">{name}</text>
    <path d="M355 21h9v9m0-9-11 11" fill="none" stroke="{c['accent']}" stroke-width="1.5"/>
    {description}'''
    return svg(390, 116, name, f'{line1} {line2}', body)


PANELS = [
    ('intro-build', 'Building in the open', [
        'I research, write, and build software with AI as part of my everyday practice. I like understanding how things work and making tools I want to use.',
        'My projects begin with practical needs: sharing files privately, understanding my network, or making a small task easier. I share the work so others can inspect, adapt, and improve it.',
    ]),
    ('intro-notes', 'A notebook, kept in public', [
        'Field Notes is my ongoing notebook: observations from building, questions I am still working through, and things I have learned along the way.',
        'Lately, I am thinking about agent memory, permissions, and verification. I come back to these questions as I build, and revise my notes as my understanding changes.',
    ]),
    ('ai-practice', 'How I work', [
        'I move between research, code, and writing with agents in the loop. I set the problem and bring the context; they help explore, implement, and iterate.',
        'Tests and real outputs tell me what holds up. I decide what ships.',
    ]),
    ('ai-learning', 'What I care about', [
        "I'm interested in workflows that get better with use: reusable tools, useful memory, and enough visibility to understand a failure and keep going.",
    ]),
    ('contact-public', 'A small decryption puzzle', [
        'For general questions, ideas, or feedback — GitHub issues are the right place.',
        'If you need to reach me privately, I only accept contact through GPG-encrypted channels. No plain email, no DMs.',
        'Think of it as a small decryption puzzle — if you can play this game, we already speak the same language.',
    ]),
    ('contact-steps', 'To request a private channel', [
        '1. Click the GPG button below to open an issue.',
        '2. Share your GPG public key block or 40-character fingerprint (must be on keys.openpgp.org).',
        "3. I'll reply with my GPG fingerprint encrypted to your key — import it from keys.openpgp.org to find my address, then send encrypted email only.",
    ]),
]


def panel_lines(paragraphs):
    lines = []
    for paragraph in paragraphs:
        if lines:
            lines.append('')
        lines.extend(wrap(paragraph, 34, break_long_words=False, break_on_hyphens=False))
    return lines


def panel(c, slug, title, paragraphs, height):
    body = f'''<path d="M14 20h18" stroke="{c['accent']}" stroke-width="3" stroke-linecap="round"/>
    <text x="14" y="53" fill="{c['ink']}" font-size="22" font-weight="600">{escape(title)}</text>'''
    for i, line in enumerate(panel_lines(paragraphs)):
        body += f'<text x="14" y="{91+i*28}" fill="{c["ink"]}" font-size="21">{escape(line)}</text>'
    return svg(390, height, title, ' '.join(paragraphs), body)


ACTIONS = [
    ('gpg', 'GPG', 'Request encrypted contact', 320,
     '<rect x="4" y="10" width="16" height="13" rx="3"/><path d="M7 10V6a5 5 0 0 1 10 0v4m-5 6v3"/>'),
    ('kofi', 'Ko-fi', 'Support my work', 240,
     '<path d="M3 7h15v10a6 6 0 0 1-6 6H9a6 6 0 0 1-6-6V7Zm15 1h2a4 4 0 0 1 0 8h-2M2 26h20"/>'),
    ('patreon', 'Patreon', 'Become a patron', 240,
     '<path d="M12 24 3 15C-5 5 7-1 12 7c5-8 17-2 9 8Z"/>'),
]


def action(c, slug, name, label, width, icon):
    visible = 'GPG · Private contact' if slug == 'gpg' else name
    width = 268 if slug == 'gpg' else 164
    body = f'''<rect x=".5" y=".5" width="{width-1}" height="51" rx="8" fill="{c['accent']}" fill-opacity=".055" stroke="{c['faint']}"/>
    <g transform="translate(16 15) scale(.8)" stroke="{c['accent']}" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round">{icon}</g>
    <text x="48" y="33" fill="{c['ink']}" font-size="19" font-weight="500">{visible}</text>'''
    return svg(width, 52, name, label, body)


NAVIGATION = [
    ('notes', 'Field Notes', '<rect x="3" y="2" width="14" height="17" rx="2"/><path d="M7 7h6M7 11h6M7 15h3"/>'),
    ('projects', 'Projects', '<rect x="2" y="2" width="6" height="6" rx="1"/><rect x="12" y="2" width="6" height="6" rx="1"/><rect x="2" y="12" width="6" height="6" rx="1"/><rect x="12" y="12" width="6" height="6" rx="1"/>'),
    ('ai', 'Working with AI', '<path d="m7 5-5 5 5 5m6-10 5 5-5 5M11 3l-2 14"/>'),
    ('contact', 'Contact', '<rect x="1" y="3" width="18" height="14" rx="2"/><path d="m2 5 8 6 8-6"/>'),
]


def navigation(c, slug, label, icon):
    body = f'''<rect x=".5" y=".5" width="199" height="47" rx="9" fill="{c['accent']}" fill-opacity=".045" stroke="{c['faint']}"/>
    <g transform="translate(14 14)" fill="none" stroke="{c['accent']}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">{icon}</g>
    <text x="44" y="30" fill="{c['ink']}" font-size="18" font-weight="500">{label}</text>'''
    return svg(200, 48, label, f'Jump to {label}', body)


if __name__ == '__main__':
    import hashlib
    import re
    ASSETS.mkdir(exist_ok=True)
    generated = {}
    for theme, palette in PALETTES.items():
        items = [(f'action-{item[0]}', action(palette, *item)) for item in ACTIONS]
        items += [(f'nav-{item[0]}', navigation(palette, *item)) for item in NAVIGATION]
        items += [(f'project-{item[0].lower()}', project(palette, *item)) for item in PROJECTS]
        for i in range(0, len(PANELS), 2):
            pair = PANELS[i:i+2]
            height = 108 + 28 * max(len(panel_lines(item[2])) for item in pair)
            items += [(f'panel-{item[0]}', panel(palette, *item, height)) for item in pair]
        for slug, content in items:
            digest = hashlib.sha256(content.encode()).hexdigest()[:10]
            filename = f'{slug}-{theme}-{digest}.svg'
            (ASSETS / filename).write_text(content)
            generated[f'{slug}-{theme}'] = filename
    readme = ROOT / 'README.md'
    text = readme.read_text()
    for key, filename in generated.items():
        text = re.sub(r'(?:(?:https://raw.githubusercontent.com/yagami1997/yagami1997/[^/]+/)?assets/)' + re.escape(key) + r'(?:-[a-f0-9]{10})?\.svg', f'assets/{filename}', text)
    readme.write_text(text)
    print(f'Generated {len(generated)} versioned assets and updated README references.')
