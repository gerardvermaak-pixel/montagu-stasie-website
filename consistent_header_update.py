import pathlib, re
root=pathlib.Path(r'C:/Users/ACER/Desktop/Montagu-Stasie-Website')
html_files=sorted(root.glob('*.html'))
nav_markup='''<nav class="fixed-header">
    <a href="landing.html"><img src="Stsielogojpeg.png" alt="Montagu Stasie"></a>
    <a href="https://wa.me/27662665145" class="bg-[#9f1239] whatsapp-center"><i class="fa-brands fa-whatsapp"></i></a>
    <div class="nav-links" id="nav-links">
        <a href="main.html">HOME</a>
        <a href="menu.html">MENUS</a>
        <div class="nav-dropdown" onmouseover="this.querySelector('.dropdown-content').style.display='block'" onmouseout="this.querySelector('.dropdown-content').style.display='none'" style="position:relative; display:inline-block;">
            <a href="#">STASIE</a>
            <div class="dropdown-content" style="display:none; position:absolute; background:rgba(5,5,5,0.95); min-width:160px; right:0; box-shadow:0 8px 16px rgba(0,0,0,0.6); z-index:1001;">
                <a href="konkelwyn.html" style="display:block; padding:8px 12px; color:var(--khaki); text-decoration:none;">Konkelwyn</a>
                <a href="the-shack.html" style="display:block; padding:8px 12px; color:var(--khaki); text-decoration:none;">The Shack</a>
                <a href="the-showroom.html" style="display:block; padding:8px 12px; color:var(--khaki); text-decoration:none;">The Showroom</a>
                <a href="Wing-It.html" style="display:block; padding:8px 12px; color:var(--khaki); text-decoration:none;">Wing It</a>
                <a href="Nursery.html" style="display:block; padding:8px 12px; color:var(--khaki); text-decoration:none;">Nursery</a>
            </div>
        </div>
        <a href="events.html">EVENTS</a>
        <a href="crypto.html">CRYPTO</a>
    </div>
    <div class="mobile-toggle" onclick="toggleMenu()"><span></span><span></span><span></span></div>
</nav>'''
style_snippet='''
        nav.fixed-header {
            position: fixed;
            top: 0;
            width: 100%;
            background: rgba(5, 5, 5, 0.95) !important;
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            z-index: 1000;
            border-bottom: 1px solid rgba(176, 169, 144, 0.15);
            padding: 1rem 6%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: 0.3s ease;
        }
        nav.fixed-header img { height: 50px; }
        .whatsapp-center {
            position: absolute;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1rem;
            border-radius: 999px;
            background: #9f1239;
            color:white;
            text-decoration:none;
        }
        .nav-links { display: flex; gap: 25px; align-items: center; }
        .nav-links a { color: var(--khaki, #b0a990); font-size: 0.8rem; letter-spacing: 2px; text-transform: uppercase; text-decoration: none; transition: 0.3s; }
        .nav-links a:hover, .nav-links a.current { color: var(--text-color, #f8f8f8); }
        .nav-links.active { right: 0; }
        .mobile-toggle { display: none; cursor: pointer; flex-direction: column; gap: 6px; }
        .mobile-toggle span { width: 25px; height: 2px; background: var(--khaki, #b0a990); transition: 0.3s; }

        @media (max-width: 768px) {
            .nav-links { position: fixed; top: 0; right: -100%; width: 70%; height: 100vh; background: rgba(5,5,5,0.98); flex-direction: column; justify-content: center; padding-left: 2rem; border-left: 1px solid rgba(176,169,144,0.1); transition: 0.4s; }
            .nav-links.active { right: 0; }
            .mobile-toggle { display: flex; }
            .nav-links a { font-size: 1rem; padding: 1rem 0; }
        }
'''
script_snippet='''
    <script>
    function toggleMenu(){
        const links = document.getElementById('nav-links');
        if(!links) return;
        links.classList.toggle('active');
    }
    document.addEventListener('DOMContentLoaded', function(){
        const btn = document.querySelector('.mobile-toggle');
        if(btn) btn.addEventListener('click', toggleMenu);
    });
    </script>
'''

for file in html_files:
    text = file.read_text(encoding='utf-8')
    # Replace first nav block
    if '<nav ' in text:
        text = re.sub(r'<nav[\s\S]*?</nav>', nav_markup, text, count=1)
    # Add style snippet if missing
    if 'nav.fixed-header' not in text:
        m = re.search(r'<style[^>]*>', text)
        if m:
            insert_at = m.end()
            text = text[:insert_at] + style_snippet + text[insert_at:]
    # Add script snippet before </body>
    if 'function toggleMenu' not in text:
        text = re.sub(r'(</body>)', script_snippet + r'\1', text, count=1, flags=re.IGNORECASE)
    file.write_text(text, encoding='utf-8')
    print('Updated', file.name)
print('Done')
