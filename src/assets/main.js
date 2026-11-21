(function () {
  "use strict";
  var body = document.body;
  var header = document.querySelector(".header");

  // Header border on scroll
  function onScroll() { if (header) header.classList.toggle("scrolled", window.scrollY > 8); }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // Mobile menu
  var toggle = document.querySelector(".menu-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var r = header.getBoundingClientRect();
      document.documentElement.style.setProperty("--nav-top", Math.max(0, r.bottom) + "px");
      var open = body.classList.toggle("menu-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  // Dropdowns: hover on desktop, click everywhere
  var items = document.querySelectorAll(".nav-item.has-drop");
  var desktop = window.matchMedia("(min-width: 961px)");
  items.forEach(function (item) {
    var btn = item.querySelector(".nav-link");
    var t;
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      var willOpen = !item.classList.contains("open");
      items.forEach(function (i) { i.classList.remove("open"); i.querySelector(".nav-link").setAttribute("aria-expanded", "false"); });
      if (willOpen) { item.classList.add("open"); btn.setAttribute("aria-expanded", "true"); }
    });
    item.addEventListener("mouseenter", function () { if (!desktop.matches) return; clearTimeout(t); items.forEach(function (i) { if (i !== item) i.classList.remove("open"); }); item.classList.add("open"); });
    item.addEventListener("mouseleave", function () { if (!desktop.matches) return; t = setTimeout(function () { item.classList.remove("open"); }, 140); });
  });
  document.addEventListener("click", function (e) { if (!e.target.closest(".nav-item.has-drop")) items.forEach(function (i) { i.classList.remove("open"); }); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") { items.forEach(function (i) { i.classList.remove("open"); }); body.classList.remove("menu-open"); } });

  // Reveal on scroll
  var els = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -8% 0px" });
    els.forEach(function (el) { io.observe(el); });
  } else { els.forEach(function (el) { el.classList.add("in"); }); }

  // Service search + tag filter
  var list = document.querySelector("[data-filter-list]");
  if (list) {
    var input = document.querySelector("[data-filter-input]");
    var chips = document.querySelectorAll("[data-filter-tag]");
    var empty = document.querySelector(".empty");
    var activeTag = "all";
    var apply = function () {
      var q = (input ? input.value : "").trim().toLowerCase();
      var shown = 0;
      list.querySelectorAll("[data-name]").forEach(function (card) {
        var okQ = !q || card.getAttribute("data-name").indexOf(q) > -1;
        var okT = activeTag === "all" || (card.getAttribute("data-tags") || "").split("|").indexOf(activeTag) > -1;
        var show = okQ && okT;
        card.style.display = show ? "" : "none";
        if (show) shown++;
      });
      if (empty) empty.style.display = shown ? "none" : "block";
    };
    if (input) input.addEventListener("input", apply);
    chips.forEach(function (c) {
      c.addEventListener("click", function () {
        chips.forEach(function (x) { x.classList.remove("active"); });
        c.classList.add("active");
        activeTag = c.getAttribute("data-filter-tag");
        apply();
      });
    });
  }

  // Forms: POST to data-endpoint if configured, else open the mail client
  document.querySelectorAll("form.form").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var ok = true;
      form.querySelectorAll("[required]").forEach(function (f) {
        var bad = !f.value.trim() || (f.type === "email" && !/^\S+@\S+\.\S+$/.test(f.value));
        f.closest(".field").classList.toggle("invalid", bad);
        if (bad) ok = false;
      });
      if (!ok) { var first = form.querySelector(".invalid input, .invalid textarea, .invalid select"); if (first) first.focus(); return; }
      var data = new FormData(form);
      var endpoint = form.getAttribute("data-endpoint");
      var done = function () { form.classList.add("sent"); };
      if (endpoint) {
        fetch(endpoint, { method: "POST", body: data, headers: { Accept: "application/json" } }).then(done).catch(done);
      } else {
        var lines = [];
        data.forEach(function (v, k) { if (v) lines.push(k + ": " + v); });
        var to = form.getAttribute("data-mailto");
        window.location.href = "mailto:" + to + "?subject=" + encodeURIComponent("Website enquiry") + "&body=" + encodeURIComponent(lines.join("\n"));
        done();
      }
    });
    form.querySelectorAll("input, textarea, select").forEach(function (f) {
      f.addEventListener("input", function () { var fl = f.closest(".field"); if (fl) fl.classList.remove("invalid"); });
    });
  });

  // Year
  var y = document.querySelector("[data-year]");
  if (y) y.textContent = new Date().getFullYear();
})();
