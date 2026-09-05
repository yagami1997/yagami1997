"""Generate dependency-free SVG assets for the GitHub profile's two themes."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
PALETTES = {
    'light': dict(ink='#20242b', muted='#59636e', faint='#d1d9e0', accent='#bb482f', soft='#f9ede8'),
    'dark': dict(ink='#f0f3f6', muted='#b1bac4', faint='#454c56', accent='#f6a18b', soft='#382d2b'),
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


def header(c):
    # Transparent canvas also blends into GitHub's dimmed and high-contrast themes.
    body = f'''
    <text x="20" y="88" fill="{c['ink']}" font-size="76" font-weight="600" letter-spacing="-3">yagami1997<tspan fill="{c['accent']}">.</tspan></text>
    <text x="24" y="141" fill="{c['ink']}" font-size="32">A person building with agents.</text>
    <g transform="translate(686 90)" fill="none" stroke-linecap="round" stroke-linejoin="round">
      <circle r="58" fill="{c['soft']}" stroke="none"/>
      <path d="M-55 18C-25-51 29-46 47-13C71 31 12 72-23 42C-52 17-11-29 26-15C64 0 20 50-9 22C-32 0-3-31 22-48" stroke="{c['accent']}" stroke-width="2.6"/>
      <circle cx="22" cy="-48" r="4.5" fill="{c['accent']}" stroke="none"/>
      <path d="M-57 17l2 7 7-3" stroke="{c['accent']}" stroke-width="2.6"/>
    </g>
    <path d="M24 188H776" stroke="{c['faint']}"/>
    <path d="M24 188H64" stroke="{c['accent']}" stroke-width="2"/>
    '''
    return svg(800, 202, 'yagami1997 — a person building with agents',
               'Independent builder in Del Mar, California. Systems over hype. Curiosity intact.', body)


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


if __name__ == '__main__':
    ASSETS.mkdir(exist_ok=True)
    for theme, palette in PALETTES.items():
        (ASSETS / f'profile-header-{theme}.svg').write_text(header(palette))
        for item in PROJECTS:
            (ASSETS / f'project-{item[0].lower()}-{theme}.svg').write_text(project(palette, *item))
    print('Generated 14 SVG assets: 2 headers and 6 projects in both themes.')
