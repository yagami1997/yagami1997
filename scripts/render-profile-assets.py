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


def header(c, theme):
    start, end = ('#f8f5f0', '#f0f3f5') if theme == 'light' else ('#292b30', '#222b32')
    body = f'''<defs>
      <linearGradient id="paper" x1="0" y1="0" x2="1" y2=".3">
        <stop stop-color="{start}"/><stop offset="1" stop-color="{end}"/>
      </linearGradient>
    </defs>
    <rect x=".5" y=".5" width="439" height="169" rx="12" fill="url(#paper)" stroke="{c['faint']}" stroke-opacity=".5"/>
    <rect x="24" y="28" width="20" height="3" rx="1.5" fill="{c['accent']}"/>
    <text x="56" y="37" fill="{c['muted']}" font-size="22">Independent builder</text>
    <text x="24" y="92" fill="{c['ink']}" font-size="38" font-weight="500" letter-spacing="-1">yagami1997</text>
    <text x="24" y="136" fill="{c['ink']}" font-size="22">Code, notes &amp; experiments.</text>'''
    return svg(440, 170, 'yagami1997 — independent builder',
               'Code, notes and experiments.', body)



def project(c, name, line1, line2, number):
    lines = [(line, c['ink']) for line in wrap(line1, 32)]
    lines += [(line, c['muted']) for line in wrap(line2, 32)]
    description = ''.join(
        f'<text x="16" y="{100 + i * 27}" fill="{color}" font-size="20">{escape(line)}</text>'
        for i, (line, color) in enumerate(lines))
    body = f'''
    <text x="16" y="30" fill="{c['accent']}" font-size="18">{number}</text>
    <text x="16" y="65" fill="{c['ink']}" font-size="27" font-weight="600">{name}</text>
    <path d="M320 49h10v10m0-10-12 12" fill="none" stroke="{c['muted']}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
    {description}
    <path d="M16 206H344" stroke="{c['faint']}"/>
    '''
    return svg(360, 220, name, f'{line1} {line2}', body)


ACTIONS = [
    ('gpg', 'GPG', 'Request encrypted contact', 320,
     '<rect x="4" y="10" width="16" height="13" rx="3"/><path d="M7 10V6a5 5 0 0 1 10 0v4m-5 6v3"/>'),
    ('kofi', 'Ko-fi', 'Support my work', 240,
     '<path d="M3 7h15v10a6 6 0 0 1-6 6H9a6 6 0 0 1-6-6V7Zm15 1h2a4 4 0 0 1 0 8h-2M2 26h20"/>'),
    ('patreon', 'Patreon', 'Become a patron', 240,
     '<path d="M12 24 3 15C-5 5 7-1 12 7c5-8 17-2 9 8Z"/>'),
]


def action(c, slug, name, label, width, icon):
    body = f'''<rect x=".5" y=".5" width="{width-1}" height="75" rx="8" fill="none" stroke="{c['faint']}"/>
    <g transform="translate(16 24) scale(.9)" stroke="{c['accent']}" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round">{icon}</g>
    <text x="50" y="30" fill="{c['ink']}" font-size="20" font-weight="600">{name}</text>
    <text x="50" y="56" fill="{c['muted']}" font-size="18">{label}</text>'''
    return svg(width, 76, name, label, body)


NAVIGATION = [
    ('notes', 'Field Notes', '<rect x="3" y="2" width="14" height="17" rx="2"/><path d="M7 7h6M7 11h6M7 15h3"/>'),
    ('projects', 'Projects', '<rect x="2" y="2" width="6" height="6" rx="1"/><rect x="12" y="2" width="6" height="6" rx="1"/><rect x="2" y="12" width="6" height="6" rx="1"/><rect x="12" y="12" width="6" height="6" rx="1"/>'),
    ('ai', 'Working with AI', '<path d="m7 5-5 5 5 5m6-10 5 5-5 5M11 3l-2 14"/>'),
    ('contact', 'Contact', '<rect x="1" y="3" width="18" height="14" rx="2"/><path d="m2 5 8 6 8-6"/>'),
]


def navigation(c, slug, label, icon):
    body = f'''<rect x=".5" y=".5" width="199" height="57" rx="9" fill="{c['accent']}" fill-opacity=".045" stroke="{c['faint']}"/>
    <g transform="translate(14 19)" fill="none" stroke="{c['accent']}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">{icon}</g>
    <text x="44" y="35" fill="{c['ink']}" font-size="20" font-weight="500">{label}</text>'''
    return svg(200, 58, label, f'Jump to {label}', body)


if __name__ == '__main__':
    ASSETS.mkdir(exist_ok=True)
    for theme, palette in PALETTES.items():
        (ASSETS / f'profile-header-{theme}.svg').write_text(header(palette, theme))
        for item in ACTIONS:
            (ASSETS / f'action-{item[0]}-{theme}.svg').write_text(action(palette, *item))
        for item in NAVIGATION:
            (ASSETS / f'nav-{item[0]}-{theme}.svg').write_text(navigation(palette, *item))
        for item in PROJECTS:
            (ASSETS / f'project-{item[0].lower()}-{theme}.svg').write_text(project(palette, *item))
    print('Generated 28 SVG assets: header, navigation, projects, and contact/support actions in both themes.')
