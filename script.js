window.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('secureForm');
  form.addEventListener('submit', e => {
    const token = localStorage.getItem('cap_token');
    if (!token) {
      e.preventDefault();
      alert('Capability token missing.');
      return;
    }
    fetch(form.action || '/', {
      method: 'POST',
      headers: { 'X-CAPABILITY-TOKEN': token },
      body: new FormData(form)
    }).then(r => location.reload());
  });

  // Initialize token (in production, retrieve securely)
  localStorage.setItem('cap_token', 'Q7YtYoVlmNeXsjNH4D3LReEofvhx-3z3PVbVu2Vvt_o');
});