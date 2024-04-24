//  Define a JavaScript function to navigate to the previous page
function goBack() {
    window.history.back();
}

// Flash message time out
$(document).ready(function() {
    // Select the flash message element
    var flashMessage = $('.flash-message');

    // Set a timeout function to hide the flash message
    setTimeout(function() {
        flashMessage.fadeOut('slow'); // Fade out the flash message
    }, 3500); // 3500 milliseconds = 3.5 seconds
});
