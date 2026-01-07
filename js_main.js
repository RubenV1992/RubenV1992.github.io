// Simple client-side logic: theme toggle, menu toggle, load projects
document.addEventListener('DOMContentLoaded', () => {
  const year = document.getElementById('year');
  year.textContent = new Date().getFullYear();

  // Theme
  const themeToggle = document.getElementById('theme-toggle');
  const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  const current = localStorage.getItem('theme') || (prefersDark ? 'dark' : 'light');
  setTheme(current);
  themeToggle.addEventListener('click', () => {
    const next = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    setTheme(next);
  });

  function setTheme(t){
    if(t === 'dark'){
      document.documentElement.setAttribute('data-theme', 'dark');
      document.querySelector('meta[name="color-scheme"]')?.setAttribute('content','dark');
      themeToggle.textContent = '☀️';
    } else {
      document.documentElement.setAttribute('data-theme', 'light');
      document.querySelector('meta[name="color-scheme"]')?.setAttribute('content','light');
      themeToggle.textContent = '🌙';
    }
    localStorage.setItem('theme', t);
  }

  // Mobile menu
  const menuToggle = document.getElementById('menu-toggle');
  const nav = document.getElementById('nav');
  menuToggle?.addEventListener('click', () => {
    nav.classList.toggle('open');
    const open = nav.classList.contains('open');
    menuToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  // Load projects from JSON
  fetch('data/projects.json')
    .then(r => r.ok ? r.json() : Promise.reject('Could not load projects'))
    .then(renderProjects)
    .catch(err => {
      const grid = document.getElementById('projects-grid');
      grid.innerHTML = `<p style="color:var(--muted)">No projects to show yet. Add data/projects.json to populate this section.</p>`;
      console.warn(err);
    });

  function renderProjects(list){
    const grid = document.getElementById('projects-grid');
    if(!Array.isArray(list) || list.length === 0){
      grid.innerHTML = `<p style="color:var(--muted)">No projects found in data/projects.json.</p>`;
      return;
    }
    grid.innerHTML = '';
    list.forEach(p => {
      const el = document.createElement('article');
      el.className = 'card';
      el.innerHTML = `
        <h3>${escapeHtml(p.title)}</h3>
        <p style="color:var(--muted)">${escapeHtml(p.description || '')}</p>
        <div class="tags">
          ${(p.tags || []).map(t=>`<span class="tag">${escapeHtml(t)}</span>`).join('')}
        </div>
        <p style="margin-top:.6rem">
          ${p.live ? `<a class="btn" href="${p.live}" target="_blank" rel="noopener">Live</a>` : ''}
          ${p.repo ? `<a class="btn ghost" href="${p.repo}" target="_blank" rel="noopener">Code</a>` : ''}
        </p>
      `;
      grid.appendChild(el);
    });
  }

  function escapeHtml(s = '') {
    return s.replace(/[&<>"']/g, c => ({
      '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
    })[c]);
  }
});