$(document).ready(function(){
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    $('body').on('change','#id_producttype',function(event){
        var url = $(this).attr('data-url');
        console.log($(this).val());
        $.ajax({
            url:url,
            method: 'GET',
            data: {
                d: $(this).val() 
            },
            success: function(data){
                $('#results-wrapper').html(data);
            },
            error: function(error){
                console.log(error);
            },
            complete: function(){},
        })
    })

    $('#id_image').change(function(event){

        var myfile = $(this).prop('files');
        var reader = new FileReader();

        reader.onload = function (e) {
           $('#image-screen').attr('src', e.target.result);
        }
        reader.readAsDataURL(myfile[0]);
        $('#image-screen').fadeIn();
    })
    $('#add-button').click(function(event){
        $('#primary-form').submit();
        $('#details-form').submit();
    })
});