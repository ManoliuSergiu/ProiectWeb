$(document).ready(function(){
    
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