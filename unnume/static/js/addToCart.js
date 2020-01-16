$('#add-button').click(function(){
    var url = window.location.pathname;
    var x = url.split('/');
    if(Cookies.get('cart')){
        var a = Cookies.get('cart').split('/');
        var s = "";
        var alreadyadded = false;
        for (let i = 0; i < a.length; i++) {
            if(a[i]!=""){
                var aux = a[i];
                if (aux.split(':')[0] == x[2]) {
                    var count = Number(aux.split(':')[1])+1;
                    s+=aux.split(':')[0]+":"+count+"/";
                    alreadyadded = true
                }
                else{
                    s+=a[i]+"/"
                }
            }
        }
        if(!alreadyadded)
            s+= x[2]+":1/";
        Cookies.set('cart',s)
    }
    else{
        Cookies.set('cart',x[2]+":1/")
    }
})