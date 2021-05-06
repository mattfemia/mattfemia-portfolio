// $(document).ready(function(){

//     $(document).on('click', '#contactSubmit', function(){

//         var name = $('#contactName').val();
//         var email = $('#contactEmail').val();
//         var message = $('#contactMessage').val();

//         req = $.ajax({
//             url: '/',
//             type: 'POST',
//             data: { name: name, email: email, message: message }
//         });

//         req.done(function(data) {
            
//             $('#contact').fadeOut(1000).fadeIn(1000);

//         })
//     })
// })

(function ($) {
    'use strict';
    $(window).on('load', function () {
        $('.preloader').fadeOut(100);
    });

    particlesJS("particles-js", {
        "particles": {
            "number": {
            "value": 160,
            "density": {
                "enable": true,
                "value_area": 800
            }
            },
            "color": {
            "value": "#000000"
            },
            "shape": {
            "type": "circle",
            "stroke": {
                "width": 0,
                "color": "#ffffff"
            },
            "polygon": {
                "nb_sides": 5
            },
            "image": {
                "src": "img/github.svg",
                "width": 100,
                "height": 100
            }
            },
            "opacity": {
            "value": 1,
            "random": true,
            "anim": {
                "enable": true,
                "speed": 1,
                "opacity_min": 0,
                "sync": false
            }
            },
            "size": {
            "value": 3,
            "random": true,
            "anim": {
                "enable": false,
                "speed": 4,
                "size_min": 0.3,
                "sync": false
            }
            },
            "line_linked": {
            "enable": false,
            "distance": 150,
            "color": "#000000",
            "opacity": 0.4,
            "width": 1
            },
            "move": {
            "enable": true,
            "speed": 0.5,
            "direction": "none",
            "random": true,
            "straight": false,
            "out_mode": "out",
            "bounce": false,
            "attract": {
                "enable": false,
                "rotateX": 600,
                "rotateY": 600
            }
            }
        },
        "interactivity": {
            "detect_on": "window",
            "events": {
            "onhover": {
                "enable": true,
                "mode": "grab"
            },
            "onclick": {
                "enable": true,
                "mode": "repulse"
            },
            "resize": true
            },
            "modes": {
            "grab": {
                "distance": 155.84415584415586,
                "line_linked": {
                "opacity": 0.6152301851357151
                }
            },
            "bubble": {
                "distance": 250,
                "size": 20,
                "duration": 0.5,
                "opacity": 1,
                "speed": 1
            },
            "repulse": {
                "distance": 400,
                "duration": 0.4
            },
            "push": {
                "particles_nb": 4
            },
            "remove": {
                "particles_nb": 2
            }
            }
        },
        "retina_detect": true
    });
    
})(jQuery);