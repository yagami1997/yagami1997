"""Generate dependency-free SVG assets for the GitHub profile's two themes."""
from html import escape
from pathlib import Path

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
    <rect x=".5" y=".5" width="799" height="171" rx="12" fill="url(#paper)" stroke="{c['faint']}" stroke-opacity=".5"/>
    <rect x="32" y="31" width="22" height="3" rx="1.5" fill="{c['accent']}"/>
    <text x="65" y="37" fill="{c['muted']}" font-size="12" letter-spacing="1.4">INDEPENDENT BUILDER</text>
    <text x="30" y="93" fill="{c['ink']}" font-size="40" font-weight="500" letter-spacing="-1.3">yagami1997</text>
    <text x="32" y="129" fill="{c['muted']}" font-size="18">Code, notes &amp; experiments.</text>
    <path d="M535 40V132" stroke="{c['faint']}" stroke-opacity=".65"/>
    <text x="563" y="57" fill="{c['muted']}" font-size="11" letter-spacing="1.3">WRITING</text>
    <text x="563" y="80" fill="{c['ink']}" font-size="17">Field Notes</text>
    <text x="563" y="111" fill="{c['muted']}" font-size="11" letter-spacing="1.3">MAKING</text>
    <text x="563" y="134" fill="{c['ink']}" font-size="17">Open-source tools</text>'''
    return svg(800, 172, 'yagami1997 — independent builder',
               'Code, notes and experiments. Writing Field Notes. Making open-source tools.', body)


def project(c, name, line1, line2, number):
    body = f'''
    <text x="16" y="31" fill="{c['accent']}" font-size="12" letter-spacing="1.5">{number}</text>
    <text x="16" y="65" fill="{c['ink']}" font-size="25" font-weight="600" letter-spacing="-.6">{name}</text>
    <path d="M350 49h10v10m0-10-12 12" fill="none" stroke="{c['muted']}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
    <text x="16" y="95" fill="{c['ink']}" font-size="14">{escape(line1)}</text>
    <text x="16" y="117" fill="{c['muted']}" font-size="14">{escape(line2)}</text>
    <path d="M16 143H370" stroke="{c['faint']}"/>
    '''
    return svg(390, 156, name, f'{line1} {line2}', body)


ACTIONS = [
    ('gpg', 'GPG', 'Request encrypted contact', 288,
     '<rect x="4" y="10" width="16" height="13" rx="3"/><path d="M7 10V6a5 5 0 0 1 10 0v4m-5 6v3"/>'),
    ('kofi', 'Ko-fi', 'Support my work', 160,
     '<path d="M3 7h15v10a6 6 0 0 1-6 6H9a6 6 0 0 1-6-6V7Zm15 1h2a4 4 0 0 1 0 8h-2M2 26h20"/>'),
    ('patreon', 'Patreon', 'Become a patron', 160,
     '<path d="M12 24 3 15C-5 5 7-1 12 7c5-8 17-2 9 8Z"/>'),
]


def action(c, slug, name, label, width, icon):
    body = f'''<rect x=".5" y=".5" width="{width-1}" height="55" rx="8" fill="none" stroke="{c['faint']}"/>
    <g transform="translate(14 14) scale(.8)" stroke="{c['accent']}" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round">{icon}</g>
    <text x="44" y="24" fill="{c['ink']}" font-size="14" font-weight="600">{name}</text>
    <text x="44" y="42" fill="{c['muted']}" font-size="11.5">{label}</text>'''
    return svg(width, 56, name, label, body)


if __name__ == '__main__':
    ASSETS.mkdir(exist_ok=True)
    for theme, palette in PALETTES.items():
        (ASSETS / f'profile-header-{theme}.svg').write_text(header(palette, theme))
        for item in ACTIONS:
            (ASSETS / f'action-{item[0]}-{theme}.svg').write_text(action(palette, *item))
        for item in PROJECTS:
            (ASSETS / f'project-{item[0].lower()}-{theme}.svg').write_text(project(palette, *item))
    print('Generated 20 SVG assets: header, projects, and contact/support actions in both themes.')
