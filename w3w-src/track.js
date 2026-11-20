/* W3W — origem dos leads (first/last touch) + etiqueta no WhatsApp + eventos GA4 */
(function () {
  var KEY = 'w3w_src', ls = {};
  try { ls = window.localStorage; } catch (e) { ls = null; }
  function get(k) { try { return JSON.parse(ls.getItem(k)); } catch (e) { return null; } }
  function set(k, v) { try { ls.setItem(k, JSON.stringify(v)); } catch (e) {} }
  var q = new URLSearchParams(location.search);
  var us = (q.get('utm_source') || '').toLowerCase(), um = (q.get('utm_medium') || '').toLowerCase(),
      uc = q.get('utm_campaign') || '', ref = document.referrer ? new URL(document.referrer).hostname : '';
  var paid = /cpc|ppc|paid|ads|pago|patrocinado/.test(um);
  function label() {
    if (q.get('gclid') || q.get('gbraid') || q.get('wbraid') || (us === 'google' && paid)) return 'Google Ads';
    if (q.get('fbclid') && paid) return 'Meta Ads';
    if (/instagram|ig/.test(us)) return paid ? 'Instagram Ads' : 'Instagram';
    if (/facebook|fb|meta/.test(us)) return paid ? 'Meta Ads' : 'Facebook';
    if (/whats/.test(us)) return 'WhatsApp';
    if (/lp|landing/.test(um) || /lp|landing/.test(us)) return 'Landing page';
    if (/email|newsletter/.test(us + um)) return 'E-mail';
    if (us) return us.charAt(0).toUpperCase() + us.slice(1);
    if (/instagram/.test(ref)) return 'Instagram';
    if (/facebook|fb\.com/.test(ref)) return 'Facebook';
    if (/google\./.test(ref)) return 'Google (orgânico)';
    if (/bing|yahoo|duckduckgo/.test(ref)) return 'Busca (outros)';
    if (ref && ref !== location.hostname) return 'Site: ' + ref;
    return '';
  }
  var now = { o: label(), c: uc, p: location.pathname, t: Date.now() };
  var first = get(KEY);
  if (!first && now.o) { first = now; set(KEY, now); }
  if (!first) { first = { o: 'Direto', c: '', p: location.pathname, t: Date.now() }; set(KEY, first); }
  var last = now.o ? now : (get(KEY + '_last') || first);
  if (now.o) set(KEY + '_last', now);
  function ev(name, params) { try { if (window.gtag) window.gtag('event', name, params); } catch (e) {} }
  function page() {
    var h = document.querySelector('h1'); return (h ? h.textContent.trim() : document.title).slice(0, 60);
  }
  var wo = window.open;
  window.open = function (url) {
    try {
      if (typeof url === 'string' && url.indexOf('wa.me/') > -1 && url.indexOf('%5Bref%3A') < 0) {
        var tag = (last.o || first.o) + ((last.c || first.c) ? ' / ' + (last.c || first.c) : '');
        url += encodeURIComponent('\n\n[ref: ' + tag + ' · formulário]');
        arguments[0] = url;
      }
    } catch (e) {}
    return wo.apply(window, arguments);
  };
  window.W3W_ORIGEM = function () { return { primeira: first, ultima: last }; };
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href*="wa.me/"]');
    if (!a) return;
    try {
      var u = new URL(a.href), txt = u.searchParams.get('text') || '';
      if (txt.indexOf('[ref:') < 0) {
        var tag = last.o || first.o;
        if (last.c || first.c) tag += ' / ' + (last.c || first.c);
        u.searchParams.set('text', txt + '\n\n[ref: ' + tag + ' · ' + page() + ']');
        a.href = u.toString();
      }
    } catch (err) {}
    ev('generate_lead', { method: 'whatsapp', origem: last.o || first.o, campanha: last.c || first.c, pagina: location.pathname });
  }, true);
  document.addEventListener('submit', function (e) {
    ev('generate_lead', { method: 'formulario', origem: last.o || first.o, campanha: last.c || first.c, pagina: location.pathname });
  }, true);
  document.addEventListener('click', function (e) {
    var g = e.target.closest && e.target.closest('[data-slug]');
    if (g) ev('view_item', { item_id: g.getAttribute('data-slug'), origem: last.o || first.o });
  }, true);
})();
