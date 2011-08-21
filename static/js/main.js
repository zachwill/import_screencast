(function($) {

    // Set up animated color for hovering over navigation links.
    var links = $('header').find('a').not('.ir'),
        color = '#6b1bdf';

    links.hover(function(e) {
        var self = $(this);
        self.stop(true).animate({
            backgroundColor: color,
            color: 'white'
        }, 350)

    }, function(e) {
        var self = $(this);
        self.stop(true, true).animate({
            backgroundColor: '',
            color: '#444'
        }, 75)
    });

})(jQuery);
