document.addEventListener('DOMContentLoaded', () => {
  const btnIrArriba = document.getElementById('btnIrArriba');

  if (!btnIrArriba) return;

  btnIrArriba.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
});
