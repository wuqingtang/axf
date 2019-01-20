$(function () {
    $('.orderdetail').width(innerWidth)

    $('#pay').click(function () {
        var identifier = $(this).attr('identifier')
        data = {
            'identifier':identifier
        }
        $.get('/cls/pay/', data, function (response) {
            console.log(response)
            if (response.status == 1){
                window.open(response.alipayurl, target='_self')
            }
        })
    })
})