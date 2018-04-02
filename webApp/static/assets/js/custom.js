$(document).ready(function() {
    $('#side-menu').stop().animate({'margin-right':'-250px'},1000);

    function toggleDivs() {
        var $inner = $("#side-menu");
        if ($inner.css("margin-right") == "-250px") {
            $inner.animate({'margin-right': '0'});
        }
        else {
            $inner.animate({'margin-right': "-250px"}); 
        }
    }
    $(".side-menu-btn").bind("click", function(){
        toggleDivs();
    });
});