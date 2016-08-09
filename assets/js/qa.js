/**
 * Created by Zudog on 2016. 8. 2..
 */

$('#qna').on('show.bs.modal', function (event) {
    var modal = $(this);
    var button = modal.find('.submit-button');
    button.click(function (e) {
        if ( document.getElementById('input-query').value == "" ){
            document.getElementById('input-label').innerHTML = "문의사항을 입력해주세요.";
            $('#popup').modal('show');
            return;
        }

        $data = {
                'username' : document.getElementById('input-username').value,
                'query' : document.getElementById('input-query').value,
                'csrfmiddlewaretoken': '{{ csrf_token }}'
            };

        $.ajax(
        {
            method:'get',
            dataType : 'json',
            url:'/qa/oneqa/',
            data: $data,
            success: function(e)
            {
                if ( e.success ){
                    document.getElementById('input-label').innerHTML = "등록되었습니다.";
                    $('#qna').modal('hide');
                    $('#popup').modal('show');
                }
                else {
                    document.getElementById('input-label').innerHTML = "문제가 발생했습니다.1";
                    $('#popup').modal('show');
                }
            },
            error: function(e)
            {
                document.getElementById('input-label').innerHTML = "문제가 발생했습니다.2";
                $('#popup').modal('show');
            }
        });
    })
});

function ClickGoLogin() {
    location.href = '/login';
}

function ClickEvent(index){
    for ( var i = 0; i < 5; i++ ){
        var classname = "hidden" + i;
        var docu = document.getElementById(classname)
        if ( index == i ){
            if ( docu.style.display == "-webkit-box" ){
                docu.style.display = "none";
            }
            else {
                docu.style.display = "-webkit-box";
            }
        }
        else {
            docu.style.display = "none";
        }
    }
}

function ClickEventClose(index){
    document.getElementById("hidden" + index).style.display = "none";
}