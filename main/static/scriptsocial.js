$(document).ready(function() {
  $('.menu-btn').on('click', function(e) {
    e.preventDefault();
    $('.menu').toggleClass('menu-active');
    $('.content').toggleClass('content-active');
  });

  $('.sign-up').on('click', function(r) {
    r.preventDefault();
    $('.modal').toggleClass('open');
    $('.modal-window').toggleClass('modal-window-open');
    $('.menu').toggleClass('menu-active');
    $('.content').toggleClass('content-active');
    $('.overlay').toggleClass('.overlay-open');
  });

  // Добавим обработчик события на кнопку закрытия модального окна
  $('.close-modal-btn').on('click', function(e) {
    e.preventDefault();
    $('.modal').removeClass('open');
    $('.modal-window').removeClass('modal-window-open');
  });
});


