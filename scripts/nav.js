if (!window._stasieNavInit) {
  window._stasieNavInit = true;

  function toggleMenu() {
    const links = document.getElementById('nav-links');
    if (links) links.classList.toggle('active');
  }

  // expose toggleMenu for inline handlers or existing references
  window.toggleMenu = toggleMenu;

  (function initNav() {
    const currentPage = location.pathname.split('/').pop() || 'landing.html';
    document.querySelectorAll('.nav-links a').forEach(link => {
      if (link.getAttribute('href') === currentPage) link.classList.add('current');
    });

    // mobile: make dropdown taps toggle content
    document.querySelectorAll('.nav-dropdown > a').forEach(trigger => {
      trigger.addEventListener('click', function(e) {
        if (window.innerWidth <= 768) {
          e.preventDefault();
          const content = this.nextElementSibling;
          if (!content) return;
          content.style.display = (content.style.display === 'block') ? 'none' : 'block';
        }
      });
    });

    // close dropdowns when clicking outside on mobile
    document.addEventListener('click', function(e){
      if (window.innerWidth <= 768) {
        document.querySelectorAll('.nav-dropdown .dropdown-content').forEach(function(c){
          const parent = c.parentElement;
          if (!parent.contains(e.target) && c.style.display === 'block') c.style.display = 'none';
        });
      }
    });
  })();
}
