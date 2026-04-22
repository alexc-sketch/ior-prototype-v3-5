/* ============================================================
   IOR MOTION & INTERACTION SYSTEM — ior-motion.js
   Version: 2.0 | IntersectionObserver | No dependencies
   Scroll animations, counter animations, FMT accordion,
   mobile drawer, nav scroll behaviour
   ============================================================ */

(function () {
  'use strict';

  /* ── SCROLL ANIMATION ENGINE ── */
  const animStyles = document.createElement('style');
  animStyles.textContent = `
    [data-animate] {
      opacity: 0;
      transition-property: opacity, transform;
      transition-timing-function: cubic-bezier(0.22, 1, 0.36, 1);
      transition-duration: 700ms;
    }
    [data-animate="fade-up"]    { transform: translateY(32px); }
    [data-animate="fade-down"]  { transform: translateY(-24px); }
    [data-animate="fade-left"]  { transform: translateX(32px); }
    [data-animate="fade-right"] { transform: translateX(-32px); }
    [data-animate="fade-in"]    { transform: none; }
    [data-animate="scale-up"]   { transform: scale(0.94); }
    [data-animate].animated {
      opacity: 1;
      transform: none;
    }
    [data-stagger] > * {
      opacity: 0;
      transform: translateY(24px);
      transition: opacity 600ms cubic-bezier(0.22,1,0.36,1),
                  transform 600ms cubic-bezier(0.22,1,0.36,1);
    }
    [data-stagger] > *.animated {
      opacity: 1;
      transform: none;
    }
  `;
  document.head.appendChild(animStyles);

  const scrollObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const delay = el.dataset.delay || 0;
        setTimeout(() => el.classList.add('animated'), parseInt(delay));
        scrollObserver.unobserve(el);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

  const staggerObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const children = Array.from(entry.target.children);
        children.forEach((child, i) => {
          setTimeout(() => child.classList.add('animated'), i * 80);
        });
        staggerObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

  function initScrollAnimations() {
    document.querySelectorAll('[data-animate]').forEach(el => scrollObserver.observe(el));
    document.querySelectorAll('[data-stagger]').forEach(el => staggerObserver.observe(el));
  }

  /* ── COUNTER ANIMATION ── */
  function animateCounter(el) {
    const raw = el.dataset.target || el.textContent;
    const suffix = raw.replace(/[\d.]/g, '');
    const target = parseFloat(raw.replace(/[^\d.]/g, ''));
    if (isNaN(target)) return;
    const duration = 1800;
    const start = performance.now();
    const isFloat = raw.includes('.');
    function step(now) {
      const progress = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = target * eased;
      el.textContent = (isFloat ? current.toFixed(1) : Math.round(current)) + suffix;
      if (progress < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        counterObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  function initCounters() {
    document.querySelectorAll('[data-count]').forEach(el => {
      el.dataset.target = el.textContent;
      counterObserver.observe(el);
    });
  }

  /* ── FMT ACCORDION ── */
  function initFMTAccordion() {
    const rows = document.querySelectorAll('.fmt-row');
    if (!rows.length) return;

    const imagePanel = document.querySelector('.fmt-accordion__image-panel');

    rows.forEach((row, index) => {
      const header = row.querySelector('.fmt-row__header');
      if (!header) return;

      // Open first row by default
      if (index === 0) {
        row.classList.add('open');
        updateImagePanel(row, imagePanel);
      }

      header.addEventListener('click', () => {
        const isOpen = row.classList.contains('open');
        rows.forEach(r => r.classList.remove('open'));
        if (!isOpen) {
          row.classList.add('open');
          updateImagePanel(row, imagePanel);
        }
      });
    });
  }

  function updateImagePanel(row, panel) {
    if (!panel) return;
    const imgData = row.dataset.image;
    const imgTitle = row.querySelector('.fmt-row__title')?.textContent || '';
    const imgDesc = row.dataset.imageDesc || '';
    panel.innerHTML = `
      <div class="img-placeholder" style="width:100%;height:100%;min-height:400px;">
        <strong>${imgTitle}</strong>
        <span>IMAGE PLACEHOLDER</span>
        <em>${imgDesc}</em>
        <em style="margin-top:8px;font-size:10px;opacity:0.5;">Image updates as you explore each service</em>
      </div>
    `;
  }

  /* ── MOBILE DRAWER ── */
  function initDrawer() {
    const hamburger = document.querySelector('.nav-hamburger');
    const drawer = document.querySelector('.drawer');
    const overlay = document.querySelector('.drawer-overlay');
    const closeBtn = document.querySelector('.drawer__close');

    if (!hamburger || !drawer) return;

    function openDrawer() {
      drawer.classList.add('open');
      overlay.classList.add('open');
      document.body.style.overflow = 'hidden';
    }
    function closeDrawer() {
      drawer.classList.remove('open');
      overlay.classList.remove('open');
      document.body.style.overflow = '';
    }

    hamburger.addEventListener('click', openDrawer);
    closeBtn?.addEventListener('click', closeDrawer);
    overlay?.addEventListener('click', closeDrawer);
  }

  /* ── NAV SCROLL BEHAVIOUR ── */
  function initNavScroll() {
    const nav = document.querySelector('.primary-nav');
    if (!nav) return;
    let lastY = 0;
    window.addEventListener('scroll', () => {
      const y = window.scrollY;
      if (y > 80) {
        nav.style.boxShadow = '0 4px 24px rgba(0,0,0,0.12)';
      } else {
        nav.style.boxShadow = '0 2px 16px rgba(0,0,0,0.06)';
      }
      lastY = y;
    }, { passive: true });
  }

  /* ── PARALLAX HERO ── */
  function initParallax() {
    const heroes = document.querySelectorAll('.hero-split__right, .hero-full');
    if (!heroes.length) return;
    window.addEventListener('scroll', () => {
      const y = window.scrollY;
      heroes.forEach(el => {
        el.style.transform = `translateY(${y * 0.18}px)`;
      });
    }, { passive: true });
  }

  /* ── ACTIVE NAV LINK ── */
  function initActiveNav() {
    const current = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav-links a, .drawer__link').forEach(link => {
      const href = link.getAttribute('href')?.split('/').pop();
      if (href === current) link.classList.add('active');
    });
  }

  /* ── QUICK LINKS ACTIVE STATE ── */
  function initQuickLinks() {
    const current = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.ql-item').forEach(item => {
      const href = item.getAttribute('href')?.split('/').pop();
      if (href === current) item.classList.add('active');
    });
  }

  /* ── HUBSPOT FORM PLACEHOLDER ── */
  function initHubSpotPlaceholders() {
    document.querySelectorAll('[data-hubspot-form]').forEach(el => {
      el.innerHTML = `
        <div style="background:var(--off-white);border:2px dashed var(--border-light);border-radius:var(--radius-md);padding:40px 32px;text-align:center;">
          <div style="font-size:28px;margin-bottom:12px;">📋</div>
          <strong style="display:block;font-size:16px;color:var(--ior-charcoal);margin-bottom:8px;">HubSpot Form — ${el.dataset.hubspotForm}</strong>
          <p style="font-size:13px;color:var(--mid-grey);">Embed HubSpot form ID: <code style="background:#e2e8f0;padding:2px 6px;border-radius:4px;">${el.dataset.formId || 'FORM_ID_TBC'}</code></p>
          <p style="font-size:12px;color:var(--mid-grey);margin-top:8px;">In production: replace this div with the HubSpot embed script</p>
        </div>
      `;
    });
  }

  /* ── INIT ALL ── */
  function init() {
    initScrollAnimations();
    initCounters();
    initFMTAccordion();
    initDrawer();
    initNavScroll();
    initParallax();
    initActiveNav();
    initQuickLinks();
    initHubSpotPlaceholders();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
