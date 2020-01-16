$(document).ready(function(){
    var sum = 0
    for (let i = 0; i < Number($('#count').text()); i++) {
        var a = i;
        var p = '#result'+a;
        var t ='#value'+a;
        var mult = '#'+a;
        var a = Number($(t).text())*Number($(mult).val());
        $(p).html(a+' Lei')
        sum += a
    }
    $('#total').html('Total: '+sum+ ' Lei')
})
$('input').change(function(){
    var sum = 0
    for (let i = 0; i < Number($('#count').text()); i++) {
        var a = i;
        var p = '#result'+a;
        var t ='#value'+a;
        var mult = '#'+a;
        var a = Number($(t).text())*Number($(mult).val());
        $(p).html(a+' Lei')
        sum += a
    }
    $('#total').html('Total: '+sum+ ' Lei')
})