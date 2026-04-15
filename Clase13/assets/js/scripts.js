$(function () {
  $('p').on({
    click: function () {
      console.log('clickeado');
    },
    mouseover: function () {
      console.log('sobrepasado');
    }
  });
});
