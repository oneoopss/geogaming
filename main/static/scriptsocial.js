$(document).ready(function() {
  $('.menu-btn').on('click', function(e) {
    e.preventDefault();
    $('.menu').toggleClass('menu-active');
    $('.content').toggleClass('content-active');
  });
/** Всплывающее окно с кнопками РЕГИСТРАЦИЯ**/
  $('.sign-up').on('click', function(r) {
    r.preventDefault();
    $('.modal').toggleClass('open');
    $('.modal-window').toggleClass('modal-window-open');
    $('.menu').toggleClass('menu-active');
    $('.content').toggleClass('content-active');
    $('.overlay').toggleClass('overlay-open'); 
  });
  
  // Добавим обработчик события на кнопку закрытия модального окна
  $('.close-modal-btn').on('click', function(e) {
    e.preventDefault();
    $('.modal').removeClass('open');
    $('.modal-window').removeClass('modal-window-open');
  });
/** Всплывающее окно с кнопками ВХОД **/
  
});
$(document).ready(function() {
  $('.login-btn').on('click', function(l) {
    l.preventDefault();
    $('.login').toggleClass('open');
    $('.window-login').toggleClass('window-login-open');
    $('.menu').toggleClass('menu-active');
    $('.content').toggleClass('content-active');
    $('.overlay').toggleClass('overlay-open');
  });

  // Добавим обработчик события на кнопку закрытия модального окна
  $('.close-modal-btn-login').on('click', function(g) {
    g.preventDefault();
    $('.login').removeClass('open');
    $('.window-login').removeClass('window-login-open');
  });
});
