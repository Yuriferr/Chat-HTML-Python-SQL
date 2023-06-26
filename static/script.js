$(document).ready(function() {
    setInterval(fetchMessages, 1000);
});

function fetchMessages() {
    $.ajax({
        url: '/fetch_messages',
        type: 'GET',
        success: function(response) {
            $('#message-container').html(response);
            scrollChat();
        }
    });
}

function sendMessage() {
    var userInput = $('#user-input').val();
    
    if (userInput.trim() !== '') {
        $.ajax({
            url: '/send_message',
            type: 'POST',
            data: {message: userInput},
            success: function() {
                $('#user-input').val('');
                fetchMessages();
            }
        });
    }
}

function scrollChat() {
    $('#message-container').scrollTop($('#message-container')[0].scrollHeight);
}
