function message_error(obj) {
    let html = '';
    if (typeof (obj) === 'object') {
        html = '<ul>';
        $.each(obj, function (key, value) {
            html += '<li style="text-align: left">' + key + ': ' + value + '</li>'
        })
        html += '</ul>'
    } else {
        html = '<p>' + obj + '</p>'
    }

    toastr.error(
        html,
        "Error!",
        {
            positionClass: "toastr toast-top-right",
            containerId: "toast-top-right",
            closeButton: true,
            progressBar: true,
            timeOut: 3000,
        }
    );
}

function submit_with_ajax(url, title, content, parameters, callback, cancel) {

    $.confirm({
        theme: 'supervan',
        title: title,
        icon: 'fa fa-info',
        content: content,
        columnClass: 'medium',
        typeAnimated: true,
        cancelButtonClass: 'btn-primary',
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: "Si",
                btnClass: 'btn-blue',
                action: function () {
                    $.ajax({
                        url: url,
                        type: 'POST',
                        data: parameters,
                        dataType: 'json',
                        processData: false,
                        contentType: false,
                    }).done(function (data) {
                        if (!data.hasOwnProperty('error')) {
                            callback(data);
                            return false;
                        }
                        message_error(data.error);
                    }).fail(function (jqXHR, textSatus, errorThrown) {
                        console.log(jqXHR)
                        console.log(textSatus)
                        console.log(errorThrown)

                        toastr.error(
                            errorThrown,
                            "Error!",
                            {
                                positionClass: "toastr toast-top-right",
                                containerId: "toast-top-right",
                                closeButton: true,
                                progressBar: true,
                                timeOut: 3000,
                            }
                        );
                    })
                }
            },
            danger: {
                text: "No",
                btnClass: 'btn-red',
                action: function () {
                    cancel()
                    return false;
                }
            },
        }
    })

}

function alert_action(title, content, callback, cancel) {

    $.confirm({
        theme: 'supervan',
        title: title,
        icon: 'fa fa-info',
        content: content,
        columnClass: 'medium',
        typeAnimated: true,
        cancelButtonClass: 'btn-primary',
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: "Si",
                btnClass: 'btn-primary',
                action: function () {
                    callback();
                }
            },
            danger: {
                text: "No",
                btnClass: 'btn-red',
                action: function () {
                    cancel();
                }
            },
        }
    })

}