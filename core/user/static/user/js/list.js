console.log('list.js loaded')

$(function () {
    const dt_users_table = $('#tbl_user');

    if (dt_users_table.length) {
        dt_users = dt_users_table.DataTable({
            ajax: {
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'searchdata',
                }, // parametros
                dataSrc: "",
                // success: function(data) {
                //     console.log(data);
                // }
            },
            columns: [
                {"data": "id"},
                {"data": "full_name"},
                {"data": "username"},
                {"data": "date_joined"},
                {"data": "image"},
                {"data": "groups"},
                {"data": "id"},
            ],
            columnDefs: [
                {
                    targets: [-3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<img src="' + row.image + '" class="rounded-circle mx-auto d-block" style="width: 45px; height: 45px;">'
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        let buttons = '<a href="/user/update/' + row.id + '" class="btn btn-light-primary btn-circle btn-lg item-edit"><i class="text-primary ti ti-pencil"></i></a> ';
                        buttons += '<a href="/user/delete/' + row.id + '" class="btn btn-light-danger btn-circle btn-lg item-delete"><i class="text-danger ti ti-trash"></i></a>';
                        return buttons
                    }
                },
            ],
            order: [[0, 'asc']],
            orderable: true,
            dom: "<'row'<'col-sm-6'l><'col-sm-6'f>>" + "rtip",
            displayLength: 10,
            lengthMenu: [10, 25, 50, 75, 100],
            language: {
                processing: "Procesando...",
                search: "Buscar:",
                lengthMenu: "Mostrar _MENU_ elementos",
                info: "Mostrando de _START_ a _END_ de _TOTAL_ elementos",
                infoEmpty: "Mostrando 0 elementos",
                infoFiltered: "(filtrado de _MAX_ elementos en total)",
                infoPostFix: "",
                loadingRecords: "Cargando registros...",
                zeroRecords: "No se encontraron registros",
                emptyTable: "No hay datos disponibles en la tabla",
                paginate: {
                    first: "Primero",
                    previous: "Anterior",
                    next: "Siguiente",
                    last: "Último"
                },
                aria: {
                    sortAscending: ": activar para ordenar la columna de manera ascendente",
                    sortDescending: ": activar para ordenar la columna de manera descendente"
                }
            }
        });
    }

    $('#btn-add-new-user').on('click', function () {
        window.location.href = '/users/add/'
    });

    // $('.refresh-category').on('click', function () {
    //     window.location.reload()
    // });

});