/**
 * ior-global.js
 * Shared JS for all IOR wireframe pages.
 * Handles:
 *  1. Scroll-triggered animations (data-animate, .fade-up, data-stagger)
 *  2. Sticky nav scroll state
 *  3. Mobile drawer open/close
 *  4. Stat counter animation
 */

(function () {
  'use strict';

  /* ── 1. SCROLL ANIMATIONS ─────────────────────────────────────────── */
  function initAnimations() {
    if (!('IntersectionObserver' in window)) {
      // Fallback: make everything visible immediately
      document.querySelectorAll('[data-animate], .fade-up, [data-stagger]').forEach(function (el) {
        el.classList.add('is-visible');
      });
      return;
    }

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;

        // Handle data-delay attribute for data-animate elements
        var delay = parseInt(el.getAttribute('data-delay') || '0', 10);
        setTimeout(function () {
          el.classList.add('is-visible');
        }, delay);

        observer.unobserve(el);
      });
    }, {
      threshold: 0.12,
      rootMargin: '0px 0px -40px 0px'
    });

    // Observe all animated elements
    document.querySelectorAll('[data-animate], .fade-up, [data-stagger]').forEach(function (el) {
      observer.observe(el);
    });
  }

  /* ── 2. STICKY NAV SCROLL STATE ───────────────────────────────────── */
  function initStickyNav() {
    var nav = document.querySelector('.primary-nav');
    if (!nav) return;
    window.addEventListener('scroll', function () {
      nav.classList.toggle('primary-nav--scrolled', window.scrollY > 80);
    }, { passive: true });
  }

  /* ── 3. MOBILE DRAWER ─────────────────────────────────────────────── */
  function initDrawer() {
    var hamburger = document.getElementById('mob-hamburger');
    var drawer = document.getElementById('mobileDrawer');
    var overlay = document.getElementById('drawerOverlay');
    var closeBtn = document.getElementById('drawerClose');
    if (!drawer) return;

    var isOpen = false;

    function openDrawer() {
      isOpen = true;
      drawer.classList.add('drawer--open');
      if (overlay) overlay.classList.add('drawer-overlay--open');
      drawer.removeAttribute('aria-hidden');
      if (overlay) overlay.removeAttribute('aria-hidden');
      document.body.style.overflow = 'hidden';
    }

    function closeDrawer() {
      isOpen = false;
      drawer.classList.remove('drawer--open');
      if (overlay) overlay.classList.remove('drawer-overlay--open');
      drawer.setAttribute('aria-hidden', 'true');
      if (overlay) overlay.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }

    if (hamburger) hamburger.addEventListener('click', function () { isOpen ? closeDrawer() : openDrawer(); });
    if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
    if (overlay) overlay.addEventListener('click', closeDrawer);
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && isOpen) closeDrawer(); });

    // Drawer sub-menus
    document.querySelectorAll('.drawer__link[data-sub]').forEach(function (link) {
      link.addEventListener('click', function () {
        var subId = link.getAttribute('data-sub');
        if (!subId) return;
        var subEl = document.getElementById(subId);
        if (!subEl) return;
        var chevron = link.querySelector('.drawer__link-chevron');
        var wasOpen = subEl.classList.contains('drawer__sub--open');
        // Close all
        document.querySelectorAll('.drawer__sub--open').forEach(function (s) { s.classList.remove('drawer__sub--open'); });
        document.querySelectorAll('.drawer__link-chevron--open').forEach(function (c) { c.classList.remove('drawer__link-chevron--open'); });
        // Open this one if it was closed
        if (!wasOpen) {
          subEl.classList.add('drawer__sub--open');
          if (chevron) chevron.classList.add('drawer__link-chevron--open');
        }
      });
    });
  }

  /* ── 4. STAT COUNTER ANIMATION ────────────────────────────────────── */
  function initStatCounters() {
    var counters = document.querySelectorAll('[data-count]');
    if (!counters.length) return;

    var counterObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        var text = el.textContent.trim();
        var numMatch = text.match(/[\d,]+/);
        if (!numMatch) return;
        var target = parseInt(numMatch[0].replace(/,/g, ''), 10);
        var suffix = text.replace(numMatch[0], '');
        var start = 0;
        var duration = 1200;
        var startTime = null;

        function step(timestamp) {
          if (!startTime) startTime = timestamp;
          var progress = Math.min((timestamp - startTime) / duration, 1);
          var eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
          var current = Math.round(eased * target);
          el.textContent = current.toLocaleString() + suffix;
          if (progress < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
        counterObserver.unobserve(el);
      });
    }, { threshold: 0.5 });

    counters.forEach(function (el) { counterObserver.observe(el); });
  }

  /* ── INIT ─────────────────────────────────────────────────────────── */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      initAnimations();
      initStickyNav();
      initDrawer();
      initStatCounters();
    });
  } else {
    initAnimations();
    initStickyNav();
    initDrawer();
    initStatCounters();
  }

})();

// ── Related Content Tabs ──────────────────────────────────────────────────
document.querySelectorAll('.related-content__tab').forEach(tab => {
  tab.addEventListener('click', () => {
    const parent = tab.closest('.related-content');
    const targetId = tab.getAttribute('data-tab');
    parent.querySelectorAll('.related-content__tab').forEach(t => t.classList.remove('active'));
    parent.querySelectorAll('.related-tab-panel').forEach(p => { p.classList.remove('active'); p.style.display = 'none'; });
    tab.classList.add('active');
    const panel = document.getElementById(targetId);
    if (panel) { panel.classList.add('active'); panel.style.display = 'block'; }
  });
});
