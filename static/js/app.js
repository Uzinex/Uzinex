document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.flash-messages .message').forEach(m => {
    setTimeout(() => m.remove(), 4000);
  });
  document.querySelectorAll('[data-logout]').forEach(el => {
    el.addEventListener('click', e => {
      if(!confirm('Logout?')) e.preventDefault();
    });
  });
});

function getCookie(name){
  let value = `; ${document.cookie}`;
  let parts = value.split(`; ${name}=`);
  if(parts.length === 2) return parts.pop().split(';').shift();
}

function csrfFetch(url, options={}){
  options.method = options.method || 'POST';
  options.headers = options.headers || {};
  options.headers['X-CSRFToken'] = getCookie('csrftoken');
  return fetch(url, options);
}
