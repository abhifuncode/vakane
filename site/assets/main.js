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

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var fine = window.matchMedia("(hover: hover) and (pointer: fine)").matches;

  // Split headings into words for on-scroll reveal
  document.querySelectorAll(".split-on-view").forEach(function (el) {
    var words = el.textContent.trim().split(/\s+/);
    el.innerHTML = words.map(function (w, i) { return '<span class="w"><span style="--i:' + i + '">' + w + "</span></span>"; }).join(" ");
  });

  // Stagger children
  document.querySelectorAll("[data-stagger]").forEach(function (wrap) {
    Array.prototype.forEach.call(wrap.children, function (c, i) { c.style.setProperty("--d", Math.min(i * 70, 700) + "ms"); });
  });

  // Count-up numbers
  function countUp(el) {
    var end = parseFloat(el.getAttribute("data-count")), suf = el.getAttribute("data-suffix") || "";
    if (reduce) { el.textContent = end + suf; return; }
    var t0 = null, dur = 1600;
    function step(t) {
      if (!t0) t0 = t;
      var p = Math.min(1, (t - t0) / dur), v = Math.round(end * (1 - Math.pow(1 - p, 3)));
      el.textContent = v + suf;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  // Reveal on scroll
  var els = document.querySelectorAll(".reveal, .reveal-img, .split-on-view, .steps-wrap, [data-count]");
  if ("IntersectionObserver" in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var t = en.target;
        if (t.hasAttribute("data-count")) countUp(t); else t.classList.add("in");
        io.unobserve(t);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.05 });
    els.forEach(function (el) { io.observe(el); });
  } else {
    els.forEach(function (el) { if (el.hasAttribute("data-count")) countUp(el); else el.classList.add("in"); });
  }

  // Scroll progress, header hide/show, parallax
  var bar = document.createElement("div"); bar.className = "progress"; body.appendChild(bar);
  var px = Array.prototype.slice.call(document.querySelectorAll("[data-parallax]"));
  var lastY = window.scrollY, ticking = false;
  function frame() {
    var y = window.scrollY, h = document.documentElement.scrollHeight - innerHeight;
    bar.style.setProperty("--p", h > 0 ? (y / h).toFixed(4) : 0);
    if (header && !body.classList.contains("menu-open")) {
      if (y > 400 && y > lastY + 4) header.classList.add("hide");
      else if (y < lastY - 4 || y < 400) header.classList.remove("hide");
    }
    lastY = y;
    if (!reduce) px.forEach(function (el) {
      var r = el.parentElement.getBoundingClientRect();
      if (r.bottom < -200 || r.top > innerHeight + 200) return;
      var off = (r.top + r.height / 2 - innerHeight / 2) * parseFloat(el.getAttribute("data-parallax"));
      el.style.transform = "translate3d(0," + (-off).toFixed(1) + "px,0)";
    });
    ticking = false;
  }
  window.addEventListener("scroll", function () { if (!ticking) { ticking = true; requestAnimationFrame(frame); } }, { passive: true });
  window.addEventListener("resize", frame);
  frame();

  if (fine && !reduce) {
    // Spotlight follows the cursor
    document.querySelectorAll(".spot").forEach(function (c) {
      c.addEventListener("mousemove", function (e) {
        var r = c.getBoundingClientRect();
        c.style.setProperty("--mx", (e.clientX - r.left) + "px");
        c.style.setProperty("--my", (e.clientY - r.top) + "px");
      });
    });
    // Hero collage depth tilt
    var col = document.querySelector("[data-tilt]");
    if (col) {
      var hero = col.closest("section");
      hero.addEventListener("mousemove", function (e) {
        var r = hero.getBoundingClientRect(), nx = (e.clientX - r.left) / r.width - .5, ny = (e.clientY - r.top) / r.height - .5;
        col.querySelectorAll("[data-depth]").forEach(function (b) {
          var d = parseFloat(b.getAttribute("data-depth"));
          b.style.transform = "translate(" + (nx * d).toFixed(1) + "px," + (ny * d).toFixed(1) + "px)";
        });
      });
    }
    // Magnetic buttons
    document.querySelectorAll(".magnetic").forEach(function (b) {
      b.addEventListener("mousemove", function (e) {
        var r = b.getBoundingClientRect();
        b.style.transform = "translate(" + ((e.clientX - r.left - r.width / 2) * .18).toFixed(1) + "px," + ((e.clientY - r.top - r.height / 2) * .3).toFixed(1) + "px)";
      });
      b.addEventListener("mouseleave", function () { b.style.transform = ""; });
    });
  }

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
