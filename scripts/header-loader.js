// header-loader.js — fetches shared header HTML and inserts it at top of body
(function(){
  function insertHeader(html){
    // Only insert the shared header when a placeholder exists on the page.
    // This prevents accidental injection on pages intended to be headerless (e.g., landing).
    var placeholder = document.getElementById('site-header-placeholder');
    if(!placeholder) return; // nothing to do on this page

    placeholder.innerHTML = html;

    // attach mobile toggle handler
    const toggle = document.getElementById('mobile-toggle') || document.querySelector('.mobile-toggle');
    if(toggle) toggle.addEventListener('click', window.toggleMenu || function(){
      const links = document.getElementById('nav-links'); if(links) links.classList.toggle('active');
    });

    // load nav behavior
    var s = document.createElement('script'); s.src = 'scripts/nav.js'; s.defer = true; document.body.appendChild(s);
  }

  // fetch the include and insert only if placeholder exists
  if(document.getElementById('site-header-placeholder')){
    fetch('includes/header.html').then(function(r){ if(!r.ok) throw r; return r.text(); }).then(insertHeader).catch(function(){
      console.warn('Failed to load shared header');
    });
  }
})();
