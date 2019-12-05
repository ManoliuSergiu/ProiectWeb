$(document).ready(function(){
    $('body').on('change','#id_producttype',function(event){
        var url = $(this).attr('data-url')
        console.log($(this).val())
        $.ajax({
            url:url,
            method: 'GET',
            data: {},
            success: function(data){
                console.log(data);
                $('#results-wrapper').html(data);
            },
            error: function(error){
                console.log(error);
            },
            complete: function(){},
        })
    })
});