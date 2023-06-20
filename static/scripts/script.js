$('#submit').click(function () {
    var queryText = $('#query').val();
    $('#chatbox').append('<p><strong>You:</strong> ' + queryText + '</p>');
    $.ajax({
        url: '/query',
        contentType: 'application/json',
        data: JSON.stringify({ 'query': queryText }),
        type: 'POST',
        success: function (response) {
            $('#chatbox').append('<p><strong>Bot:</strong> ' + response.result + '</p>');
            $('#query').val('');
        },
        error: function (error) {
            console.log(error);
        }
    });
});

$('#append').click(function () {
    var appendDataText = $('#appendData').val();
    $.ajax({
        url: '/append',
        contentType: 'application/json',
        data: JSON.stringify({ 'data': appendDataText }),
        type: 'POST',
        success: function (response) {
            $('#appendData').val('');
        },
        error: function (error) {
            console.log(error);
        }
    });
});
