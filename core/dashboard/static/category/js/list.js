document.body.addEventListener('close-modal', function () {
    var modal = bootstrap.Modal.getInstance(document.getElementById('category-modal'));
    modal.hide();
});

function confirmDelete(event) {
    event.preventDefault();  // Detener el envío inmediato

    Swal.fire({
        title: '¿Estás seguro?',
        text: "¡No podrás revertir esto!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, eliminar',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            // Si confirma, dispara el evento HTMX manualmente
            event.target.closest('form').dispatchEvent(new Event('deleteConfirmed'));
        }
    });
}