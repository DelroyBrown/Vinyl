$(document).ready(function () {
    $('.alert').alert();
    $('.modal').modal();
    $('.sidenav').sidenav();
    $('.tooltipped').tooltip({
        'inDuration': 300,
        'transitionMovement': 5,
        'exitDelay': 0,
    });


    AOS.init({
        duration: 800,
        easing: 'slide',
        once: true
    });


    // Scrollbar animation
    $(document).scroll(function (e) {
        var scrollAmount = $(window).scrollTop();
        var documentHeight = $(document).height();
        var windowHeight = $(window).height();
        var scrollPercent = (scrollAmount / (documentHeight - windowHeight)) * 100;

        // For scrollbar 1
        $(".scrollBar1").css("width", scrollPercent + "%");

        // For scrollbar 2
        $(".scrollBar2").css("width", scrollPercent + "%");
    });



});