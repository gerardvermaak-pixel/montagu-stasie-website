import pathlib, re
root = pathlib.Path(r'C:/Users/ACER/Desktop/Montagu-Stasie-Website')
html_files = sorted(root.glob('*.html'))
style_snippet = '''
        /* Mobile soft border and safe viewport */
        @media (max-width: 768px) {
            html, body { min-height: 100%; width: 100%; overflow-x: hidden; }
            body { padding: 0 14px 20px; margin: 0; }
            nav#main-nav { left: 0; right: 0; width: calc(100% - 28px); margin: 0 auto; border-left: 1px solid rgba(176,169,144,0.25); border-right: 1px solid rgba(176,169,144,0.25); }
            #mobile-menu { border-left: 1px solid rgba(176,169,144,0.25); border-right: 1px solid rgba(176,169,144,0.25); }
            .mobile-layout, .mobile-hero, .content-split, .menu-gallery, .editorial-container, .grid-layout, .product-flex { max-width: 100%; margin: 0 auto; padding: 0; }
        }
'''.strip()
script_snippet = '''
    <script>
    (function(){
        if (window._stasieResponsiveInit) return;
        window._stasieResponsiveInit = true;

        window.toggleMenu = window.toggleMenu || function() {
            const menu = document.getElementById('mobile-menu');
            if (!menu) return;
            menu.classList.toggle('hidden');
        };

        document.addEventListener('DOMContentLoaded', function() {
            const btn = document.getElementById('mobile-menu-btn');
            if (btn) btn.addEventListener('click', window.toggleMenu);
        });
    })();
    </script>
'''.strip()
for path in html_files:
    text = path.read_text(encoding='utf-8')
    changed = False
    if 'Mobile soft border and safe viewport' not in text:
        m = re.search(r'</style>', text, re.IGNORECASE)
        if m:
            text = text[:m.start()] + '\n' + style_snippet + '\n' + text[m.start():]
            changed = True
    if 'window._stasieResponsiveInit' not in text:
        m = re.search(r'</body>', text, re.IGNORECASE)
        if m:
            text = text[:m.start()] + '\n' + script_snippet + '\n' + text[m.start():]
            changed = True
    if changed:
        path.write_text(text, encoding='utf-8')
        print('Updated', path.name)
print('Done')
