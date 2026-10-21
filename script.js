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

  /* Formulaire de contact : validation et récapitulatif */
  var form = document.getElementById('form');
  if (form) {
    var TELH = '+33605507947', MAIL = 'andreipintilii96@gmail.com';
    var recap = document.getElementById('recap'), rtxt = document.getElementById('recap-txt');
    function val(id) { return document.getElementById(id).value.trim(); }
    function setErr(id, eid, msg) {
      var f = document.getElementById(id), e = document.getElementById(eid);
      if (e) e.textContent = msg || '';
      if (msg) { f.setAttribute('aria-invalid', 'true'); f.setAttribute('aria-describedby', eid); } else { f.removeAttribute('aria-invalid'); f.removeAttribute('aria-describedby'); }
      return !msg;
    }
    function validPhone(v) { var d = v.replace(/[\s.\-()]/g, ''); return /^(\+33|0033|0)[1-9]\d{8}$/.test(d); }
    function validate() {
      var ok = [
        setErr('f-nom', 'e-nom', val('f-nom').length < 2 ? 'Indiquez votre nom.' : ''),
        setErr('f-tel', 'e-tel', validPhone(val('f-tel')) ? '' : 'Indiquez un numéro de téléphone valide (10 chiffres).'),
        setErr('f-mail', 'e-mail', !val('f-mail') || /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(val('f-mail')) ? '' : 'Cette adresse e-mail semble incorrecte.'),
        setErr('f-sujet', 'e-sujet', val('f-sujet') ? '' : 'Choisissez le type de demande.'),
        setErr('f-msg', 'e-msg', val('f-msg').length < 10 ? 'Décrivez votre projet en quelques mots.' : '')
      ];
      return ok.every(Boolean);
    }
    ['f-nom', 'f-tel', 'f-mail', 'f-sujet', 'f-msg'].forEach(function (id) {
      document.getElementById(id).addEventListener('blur', function () { if (this.value) validate(); });
    });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!validate()) { var bad = form.querySelector('[aria-invalid="true"]'); if (bad) bad.focus(); return; }
      var t = 'Bonjour Andrei, je suis ' + val('f-nom') + '.\nDemande : ' + val('f-sujet') + '.\n' + val('f-msg');
      if (val('f-ville')) t += '\nCommune : ' + val('f-ville');
      t += '\nMon numéro : ' + val('f-tel');
      if (val('f-mail')) t += '\nMon e-mail : ' + val('f-mail');
      rtxt.textContent = t;
      document.getElementById('r-sms').href = 'sms:' + TELH + '?&body=' + encodeURIComponent(t);
      var m = document.getElementById('r-mail');
      m.href = 'mailto:' + MAIL + '?subject=' + encodeURIComponent('Demande : ' + val('f-sujet')) + '&body=' + encodeURIComponent(t);
      m.hidden = false;
      recap.hidden = false; recap.focus();
      recap.scrollIntoView({ behavior: 'smooth', block: 'center' });
    });
    document.getElementById('r-copy').addEventListener('click', function () { copyText(rtxt.textContent, rtxt); });
  }

  var cb = document.getElementById('copy');
  if (cb) cb.addEventListener('click', function () { copyText('06 05 50 79 47', document.getElementById('tel-txt')); });
})();
