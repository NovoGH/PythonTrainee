$(document).ready(function () {
  $('#btnCambiarColor').on("click", function () {
    $('#miLista li').css("color", "#1900ff");
  });

  let contador = 4


  $('#btnAgregarElelmento').on("click", function () {
      let nuevoElemento=$("<li></li>").text("elemento " + contador).css("color", "#00ffe1ff");

    $('#miLista').append(nuevoElemento)
    contador++;
  });;


});






//$(document).ready(function () {
  //$('#miLista li').eq(0).css('color', 'red');
  //$('#miLista li').eq(1).css('color', 'red');
  //$('#miLista li').eq(2).css('color', 'yellow');
  //$('#miLista').append('<li>Elemento 4</li>').eq(3).css('color', 'yellow')
//});

  
$(document).ready(function (){
  //Ocultar lista al hacer click
  $("#ocultarLista").click(function(){
    if($('#miLista').is(':visible')){
      $('#miLista').hide();
      $("#ocultarLista").text('Mostrar Lista')
      //$('[data-bs-toggle="tooltip"]').tooltip().title('Al presionar se mostrará la lista')
    } else {
      $('#miLista').show();
      $("#ocultarLista").text('Ocultar Lista')
    
      //$('[data-bs-toggle="tooltip"]').tooltip().title('Al presionar se ocultará la lista')
    }
  })
});


  $(function () {
    $('[data-bs-toggle="tooltip"]').tooltip()
  });


  //$(function () {
  //$('#ocultarLista').tooltip(); // inicializar tooltip

  //$('#ocultarLista').on('click', function () {
    //$(this)
      //.attr('data-original-title', 'Guardado correctamente') // cambio texto
      //.tooltip('show'); // opcional: mostrar de inmediato
  //});
//});


  //const btn = document.getElementById('ocultarLista');

  //btn.addEventListener('click', () => {
    //btn.title = 'Guardado correctamente'; // nuevo texto del tooltip
    //btn.tooltip().title('Al presionar se ocultará la lista')

    //$('[data-bs-toggle="tooltip"]').tooltip().title('Al presionar se mostrará la lista')
  //});


//$(document).ready(function (){
  ////Mostratr lista al hacer click
  //$("#mostrarLista").click(function(){
    //$('#miLista').show();
    //$("#mostrarLista").text('Ocultar Lista')
  //})
//});


