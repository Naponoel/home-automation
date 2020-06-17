$(function() {
    let request = $.ajax({
        url: '/get-controllers',
        type: 'GET'
    });

    request.done(function (data) {
        console.log(data);
    });
});
