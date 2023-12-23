(function ($) {
    "use strict";

    // Initiate the wowjs
    new WOW().init();


    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.sticky-top').addClass('shadow-sm').css('top', '0px');
        } else {
            $('.sticky-top').removeClass('shadow-sm').css('top', '-100px');
        }
    });


    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({ scrollTop: 0 }, 1500, 'easeInOutExpo');
        return false;
    });


    // Header carousel
    $(".header-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        items: 1,
        dots: true,
        loop: true,
        nav: true,
        navText: [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ]
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        margin: 24,
        dots: false,
        loop: true,
        nav: true,
        navText: [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
        responsive: {
            0: {
                items: 1
            },
            992: {
                items: 2
            }
        }
    });




})(jQuery);


function openConfirmDialog(title, message) {

    alertify.confirm(title, message,
        function () {
            // Action when confirmed
        },
        function () {
            // Action when cancelled
        }
    ).set({
        labels: { ok: 'OK', cancel: '' }, // Customize button labels if needed
        defaultFocus: 'ok', // Set default focus to the 'OK' button
        show: {
            cancel: false // Hide the cancel button
        },
        reverseButtons: true
    });

    $(".alertify .ajs-footer .ajs-buttons .ajs-button.ajs-ok").css({
        "background-color": "rgb(254, 93, 55)",
        "border-color": "rgb(254, 93, 55)",
        "border-radius": "50rem",
        "width": "135px",
        "height": "50px",
        "color": "#fff"
    });

}

function msg(event, element) {
    event.preventDefault();

    //work
    openConfirmDialog('test1', 'test2 loooong message')
    //alert("Appointment successfully made! we will contact you as soon as possible!");


}




