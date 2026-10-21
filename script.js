(function () {
  var burger = document.querySelector('.burger'), menu = document.getElementById('menu'), toast = document.getElementById('toast'), timer;

  function setMenu(open) {
    menu.classList.toggle('open', open);
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    burger.setAttribute('aria-label', open ? 'Fermer le menu' : 'Ouvrir le menu');
  }
  if (burger && menu) {
    burger.addEventListener('click', function () { setMenu(!menu.classList.contains('open')); });
    menu.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('open')) { setMenu(false); burger.focus(); }
    });
    window.addEventListener('resize', function () { if (window.innerWidth > 980) setMenu(false); });
  }

  function say(t) {
    if (!toast) return;
    toast.textContent = t; toast.classList.add('on');
    clearTimeout(timer); timer = setTimeout(function () { toast.classList.remove('on'); }, 3200);
  }

  function copyText(text, node) {
    function fallback() {
      var r = document.createRange(); r.selectNodeContents(node);
      var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
      try { if (document.execCommand('copy')) { say('Copié dans le presse-papiers.'); return; } } catch (e) {}
      say('Texte sélectionné : copiez-le avec Ctrl+C.');
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () { say('Copié dans le presse-papiers.'); }, fallback);
    } else { fallback(); }
  }

  /* Pages pas encore créées (maquette de l'accueil seul) */
  document.addEventListener('click', function (e) {
    var a = e.target.closest('[data-soon]');
    if (a) { e.preventDefault(); say('La page « ' + a.getAttribute('data-soon') + ' » sera créée après validation de la maquette.'); }
  });

  var cb = document.getElementById('copy');
  if (cb) cb.addEventListener('click', function () { copyText('06 05 50 79 47', document.getElementById('tel-txt')); });
})();
