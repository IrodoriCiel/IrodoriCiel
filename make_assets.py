"""Genera los SVG animados del README de perfil (mismo estilo que irodoriciel.dev).

Los SVG no pueden cargar fuentes externas dentro de GitHub, así que usan fuentes del sistema.
Uso: python make_assets.py  (escribe en ./assets)
"""
import base64, io
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parent
ASSETS = HERE / 'assets'
ASSETS.mkdir(exist_ok=True)
SITE_IMG = HERE.parent / 'img'

SANS = "'Segoe UI', 'Helvetica Neue', system-ui, -apple-system, Arial, sans-serif"
MONO = "'JetBrains Mono', 'Cascadia Code', Consolas, 'SFMono-Regular', Menlo, monospace"

ROLES = ['Desarrollador NetSuite', 'Apps Android nativas', 'Extensiones de Chrome', 'Sitios web',
         'Traductor de videojuegos', 'Canciones japonés → español', 'Editor de Japan Pulse']


def avatar_data_uri():
    im = Image.open(SITE_IMG / 'avatar-mate.webp').convert('RGB').resize((240, 240), Image.LANCZOS)
    buf = io.BytesIO(); im.save(buf, 'JPEG', quality=84)
    return 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()


def banner():
    n = len(ROLES); step = 3  # segundos por rol
    total = n * step
    roles_css = '\n'.join(
        f'.r{i} {{ animation: role {total}s infinite; animation-delay: {i * step}s; }}' for i in range(n))
    a = 100 / n  # porcentaje del ciclo que dura cada rol
    # El cursor va dentro de cada texto, así siempre queda pegado al final del rol
    roles_svg = '\n'.join(f'<text class="role r{i}" x="0" y="0">{r}<tspan class="caret" dx="4">▌</tspan></text>' for i, r in enumerate(ROLES))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="1200" height="400" role="img" aria-label="Hola, soy Miguel García. Desarrollador NetSuite · Iro Dev">
<defs>
  <linearGradient id="g" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#8b7bff"/><stop offset=".55" stop-color="#3ee7c4"/><stop offset="1" stop-color="#8b7bff"/>
  </linearGradient>
  <linearGradient id="ring" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8b7bff"/><stop offset="1" stop-color="#3ee7c4"/></linearGradient>
  <radialGradient id="b1" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#8b7bff" stop-opacity=".45"/><stop offset="1" stop-color="#8b7bff" stop-opacity="0"/></radialGradient>
  <radialGradient id="b2" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#3ee7c4" stop-opacity=".25"/><stop offset="1" stop-color="#3ee7c4" stop-opacity="0"/></radialGradient>
  <clipPath id="face"><circle cx="180" cy="200" r="104"/></clipPath>
  <clipPath id="card"><rect width="1200" height="400" rx="28"/></clipPath>
</defs>
<style>
  .blob1 {{ animation: drift1 14s ease-in-out infinite alternate; }}
  .blob2 {{ animation: drift2 18s ease-in-out infinite alternate; }}
  @keyframes drift1 {{ to {{ transform: translate(120px, 60px) scale(1.1); }} }}
  @keyframes drift2 {{ to {{ transform: translate(-140px, -50px); }} }}
  .spin {{ transform-box: fill-box; transform-origin: center; animation: spin 8s linear infinite; }}
  @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
  .kicker {{ font: 600 20px {MONO}; fill: #3ee7c4; letter-spacing: 2px; }}
  .hello {{ font: 700 64px {SANS}; fill: #ededf2; letter-spacing: -1.5px; }}
  .name {{ font: 800 78px {SANS}; letter-spacing: -2px; }}
  .gl1 {{ fill: #3ee7c4; opacity: 0; animation: gla 6s steps(1) infinite 1.5s; }}
  .gl2 {{ fill: #ff5ca0; opacity: 0; animation: glb 6s steps(1) infinite 1.5s; }}
  @keyframes gla {{ 0%, 90%, 100% {{ opacity: 0; transform: none; clip-path: inset(0); }}
    91% {{ opacity: .75; transform: translate(-4px, 0); clip-path: inset(10% 0 60% 0); }}
    93% {{ transform: translate(4px, 0); clip-path: inset(55% 0 20% 0); }}
    95% {{ transform: translate(-2px, 0); clip-path: inset(30% 0 45% 0); }}
    97% {{ opacity: 0; }} }}
  @keyframes glb {{ 0%, 90%, 100% {{ opacity: 0; transform: none; clip-path: inset(0); }}
    91% {{ opacity: .6; transform: translate(4px, 0); clip-path: inset(65% 0 10% 0); }}
    93% {{ transform: translate(-4px, 0); clip-path: inset(20% 0 60% 0); }}
    95% {{ transform: translate(2px, 0); clip-path: inset(45% 0 30% 0); }}
    97% {{ opacity: 0; }} }}
  .prompt {{ font: 600 26px {MONO}; fill: #8b7bff; }}
  .role {{ font: 500 26px {MONO}; fill: #ededf2; opacity: 0; }}
  @keyframes role {{ 0% {{ opacity: 0; }} 1.5% {{ opacity: 1; }} {a - 1.5:.2f}% {{ opacity: 1; }} {a:.2f}%, 100% {{ opacity: 0; }} }}
{roles_css}
  .caret {{ fill: #8b7bff; animation: blink 1s steps(1) infinite; }}
  @keyframes blink {{ 50% {{ opacity: 0; }} }}
  .chip {{ font: 600 16px {MONO}; fill: #a3a3b2; }}
  .beam {{ animation: beam 4.5s ease-in-out infinite; }}
  @keyframes beam {{ from {{ transform: translateX(-200px); }} to {{ transform: translateX(1250px); }} }}
  @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} .r0 {{ opacity: 1; }} }}
</style>
<g clip-path="url(#card)">
  <rect width="1200" height="400" fill="#08080c"/>
  <circle class="blob1" cx="160" cy="40" r="360" fill="url(#b1)"/>
  <circle class="blob2" cx="1080" cy="380" r="320" fill="url(#b2)"/>
  <rect x="0" y="398" width="1200" height="2" fill="#ffffff" opacity=".08"/>
  <rect class="beam" x="0" y="398" width="200" height="2" fill="url(#g)"/>
</g>
<rect x=".5" y=".5" width="1199" height="399" rx="28" fill="none" stroke="#ffffff" stroke-opacity=".1"/>

<!-- Foto con aro de color girando -->
<circle class="spin" cx="180" cy="200" r="114" fill="none" stroke="url(#ring)" stroke-width="6" stroke-dasharray="520 200" stroke-linecap="round"/>
<image href="{avatar_data_uri()}" x="76" y="96" width="208" height="208" clip-path="url(#face)" preserveAspectRatio="xMidYMid slice"/>

<g transform="translate(350, 0)">
  <text class="kicker" x="0" y="104">IRO DEV · MÉXICO</text>
  <text class="hello" x="0" y="176">Hola, soy</text>
  <text class="name" x="0" y="260" fill="url(#g)">Miguel García.</text>
  <text class="name gl1" x="0" y="260">Miguel García.</text>
  <text class="name gl2" x="0" y="260">Miguel García.</text>
  <text class="prompt" x="0" y="322">&gt;</text>
  <g transform="translate(30, 322)">
{roles_svg}
  </g>
</g>
</svg>
'''


def title(text, num, icon_path, name):
    """Encabezado de sección: icono en cuadro, número en mono y título, con un glitch breve."""
    w = 900
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} 84" width="{w}" height="84" role="img" aria-label="{text}">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8b7bff"/><stop offset="1" stop-color="#3ee7c4"/></linearGradient></defs>
<style>
  .num {{ font: 600 15px {MONO}; fill: #8b7bff; letter-spacing: 1.5px; }}
  .t {{ font: 800 38px {SANS}; fill: #8b7bff; letter-spacing: -.8px; }}
  .t2 {{ font: 800 38px {SANS}; letter-spacing: -.8px; opacity: 0; }}
  .c {{ fill: #3ee7c4; animation: ga 7s steps(1) infinite 2s; }}
  .p {{ fill: #ff5ca0; animation: gb 7s steps(1) infinite 2s; }}
  @keyframes ga {{ 0%, 92%, 100% {{ opacity: 0; transform: none; }} 93% {{ opacity: .7; transform: translate(-3px, 0); clip-path: inset(15% 0 55% 0); }} 95% {{ transform: translate(3px, 0); clip-path: inset(60% 0 15% 0); }} 97% {{ opacity: 0; }} }}
  @keyframes gb {{ 0%, 92%, 100% {{ opacity: 0; transform: none; }} 93% {{ opacity: .6; transform: translate(3px, 0); clip-path: inset(55% 0 20% 0); }} 95% {{ transform: translate(-3px, 0); clip-path: inset(20% 0 60% 0); }} 97% {{ opacity: 0; }} }}
  .line {{ animation: grow 1.6s ease-out both; transform-origin: 84px 0; }}
  @keyframes grow {{ from {{ transform: scaleX(0); }} }}
  @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
</style>
<rect x="2" y="12" width="60" height="60" rx="16" fill="#8b7bff" fill-opacity=".12" stroke="#8b7bff" stroke-opacity=".35"/>
<g transform="translate(17, 27)" fill="none" stroke="#8b7bff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><g transform="scale(1.25)">{icon_path}</g></g>
<text class="num" x="84" y="32">{num}</text>
<text class="t" x="84" y="70" fill="url(#g)" style="fill:url(#g)">{text}</text>
<text class="t2 c" x="84" y="70">{text}</text>
<text class="t2 p" x="84" y="70">{text}</text>
</svg>
'''


ICONS = {
    'about': '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
    'projects': '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 13h18"/>',
    'journey': '<circle cx="6" cy="19" r="2"/><circle cx="18" cy="5" r="2"/><path d="M8 19h7.5a3.5 3.5 0 0 0 0-7h-7a3.5 3.5 0 0 1 0-7H16"/>',
    'stack': '<path d="m12 3 9 5-9 5-9-5 9-5Z"/><path d="m3 13 9 5 9-5M3 17.5l9 5 9-5"/>',
    'contact': '<path d="M21 3 10 14M21 3l-6.5 18-4.5-7-7-4.5L21 3Z"/>',
}


def footer():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" width="1200" height="120" role="img" aria-label="irodoriciel.dev">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8b7bff"/><stop offset=".5" stop-color="#3ee7c4"/><stop offset="1" stop-color="#8b7bff"/></linearGradient></defs>
<style>
  .d {{ font: 600 30px {MONO}; letter-spacing: 1px; }}
  .s {{ font: 500 15px {MONO}; fill: #8f8fa1; letter-spacing: 2px; }}
  .beam {{ animation: beam 4.5s ease-in-out infinite; }}
  @keyframes beam {{ from {{ transform: translateX(-220px); }} to {{ transform: translateX(1250px); }} }}
  @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
</style>
<rect x="0" y="20" width="1200" height="1" fill="#8f8fa1" opacity=".35"/>
<rect class="beam" x="0" y="19.5" width="220" height="2" fill="url(#g)"/>
<text class="d" x="600" y="78" text-anchor="middle" fill="url(#g)">irodoriciel.dev</text>
<text class="s" x="600" y="106" text-anchor="middle">PORTAFOLIO · PROYECTOS · CONTACTO</text>
</svg>
'''


BTN_ICONS = {
    'web': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
    'linkedin': '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 10v7M8 7v.01M12 17v-4a2 2 0 0 1 4 0v4M12 10v7"/>',
    'instagram': '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5h.01"/>',
    'facebook': '<path d="M15 3h-2.5A4.5 4.5 0 0 0 8 7.5V10H5.5v4H8v7h4v-7h3l.5-4H12V7.8c0-.5.4-.8.8-.8H15V3Z"/>',
    'youtube': '<rect x="2.5" y="5.5" width="19" height="13" rx="4"/><path d="m10 9 5 3-5 3V9Z"/>',
    'x': '<path d="M4 4h4.5L20 20h-4.5L4 4ZM20 4l-6.6 7.4M4 20l6.6-7.4"/>',
    'twitch': '<path d="M4 3h16v11l-5 5h-4l-3 3H6v-3H4V3Z"/><path d="M10.5 8v4.5M15 8v4.5"/>',
    'tiktok': '<path d="M14 3v11.5a3.5 3.5 0 1 1-3.5-3.5M14 3c.4 2.6 2.4 4.6 5 4.8"/>',
    'steam': '<circle cx="12" cy="12" r="9"/><circle cx="15.5" cy="9.5" r="2.5"/><circle cx="9" cy="15" r="1.8"/><path d="m3.6 13.6 3.8 1.5M10.6 14l3.2-2.7"/>',
    'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    'coffee': '<path d="M4 9h13v4a6 6 0 0 1-6 6h-1a6 6 0 0 1-6-6V9Z"/><path d="M17 10h1.5a2.5 2.5 0 0 1 0 5H17M7 2.5v3M10.5 2.5v3M14 2.5v3"/>',
    'netsuite': '<ellipse cx="12" cy="5.5" rx="8" ry="3"/><path d="M4 5.5v13c0 1.7 3.6 3 8 3s8-1.3 8-3v-13M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/>',
}


def button(label, icon, primary=False, accent='#8b7bff'):
    """Botón en forma de píldora como los de la página (ancho calculado para la fuente monoespaciada)."""
    w = 58 + int(len(label) * 9.6)
    bg, fg, border = ('#ededf2', '#08080c', '#ededf2') if primary else ('#11111a', '#ededf2', '#2e2e3a')
    ic = '#08080c' if primary else accent
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} 44" width="{w}" height="44" role="img" aria-label="{label}">
<style>.l {{ font: 600 16px {MONO}; fill: {fg}; }}</style>
<rect x="1" y="1" width="{w - 2}" height="42" rx="21" fill="{bg}" stroke="{border}"/>
<g transform="translate(18, 12) scale(.83)" fill="none" stroke="{ic}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">{BTN_ICONS[icon]}</g>
<text class="l" x="46" y="28">{label}</text>
</svg>
'''


if __name__ == '__main__':
    (ASSETS / 'banner.svg').write_text(banner(), encoding='utf-8')
    for name, label, icon, primary, accent in [
        ('web', 'irodoriciel.dev', 'web', True, '#8b7bff'), ('linkedin', 'LinkedIn', 'linkedin', False, '#8b7bff'),
        ('instagram', 'Instagram', 'instagram', False, '#8b7bff'), ('facebook', 'Facebook', 'facebook', False, '#8b7bff'),
        ('youtube', 'YouTube', 'youtube', False, '#8b7bff'), ('x', 'X', 'x', False, '#8b7bff'),
        ('twitch', 'Twitch', 'twitch', False, '#8b7bff'), ('tiktok', 'TikTok', 'tiktok', False, '#8b7bff'),
        ('steam', 'Steam', 'steam', False, '#8b7bff'), ('mail', 'Correo', 'mail', False, '#8b7bff'),
        ('coffee', 'Invítame un café', 'coffee', False, '#ffdd00'), ('netsuite', 'NetSuite · SuiteScript · SuiteQL', 'netsuite', False, '#3ee7c4')]:
        (ASSETS / f'btn-{name}.svg').write_text(button(label, icon, primary, accent), encoding='utf-8')
    for key, (text, num) in {'about': ('Sobre mí', '01 — SOBRE MÍ'), 'projects': ('Proyectos', '02 — PROYECTOS'),
                             'journey': ('Trayectoria', '03 — TRAYECTORIA'), 'stack': ('Con qué trabajo', '04 — HABILIDADES'),
                             'contact': ('¿Construimos algo?', '05 — CONTACTO')}.items():
        (ASSETS / f'title-{key}.svg').write_text(title(text, num, ICONS[key], key), encoding='utf-8')
    (ASSETS / 'footer.svg').write_text(footer(), encoding='utf-8')
    for f in ('nsft.webp', 'japanpulse.webp', 'lgts-app.webp'):
        Image.open(SITE_IMG / f).convert('RGB').save(ASSETS / f.replace('.webp', '.jpg'), 'JPEG', quality=84, optimize=True)
    print('ok', sorted(p.name for p in ASSETS.iterdir()))
