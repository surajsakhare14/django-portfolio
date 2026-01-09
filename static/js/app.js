document.querySelectorAll("[data-reveal]").forEach(el => {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        el.classList.add("reveal-active");
      }
    });
  }, { threshold: 0.15 });

  observer.observe(el);
});
