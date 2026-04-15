<script>
  const btnIrArriba = document.getElementById('btnIrArriba');

  btnIrArriba.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
</script>
