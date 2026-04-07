// header-loader.js — fetches shared header HTML and inserts it at top of body
(function(){
  function insertHeader(html){
    const wrapper = document.createElement('div');
    wrapper.innerHTML = html;
    const first = document.body.firstChild;
    document.body.insertBefore(wrapper, first);
    // attach mobile toggle handler
    const toggle = document.getElementById('mobile-toggle') || document.querySelector('.mobile-toggle');
    if(toggle) toggle.addEventListener('click', window.toggleMenu || function(){
      const links = document.getElementById('nav-links'); if(links) links.classList.toggle('active');
    });
    // load nav behavior
    var s = document.createElement('script'); s.src = 'scripts/nav.js'; s.defer = true; document.body.appendChild(s);
  }

  // fetch the include and insert
  fetch('includes/header.html').then(function(r){ if(!r.ok) throw r; return r.text(); }).then(insertHeader).catch(function(){
    // fallback: do nothing if includes not available
    console.warn('Failed to load shared header');
  });
})();
