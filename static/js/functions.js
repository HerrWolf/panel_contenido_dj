document.body.addEventListener('htmx:afterRequest', function (event) {
    const trigger = event.detail.xhr.getResponseHeader('HX-Trigger');
    if (trigger) {
        const triggers = JSON.parse(trigger);
        if (triggers['show-toast']) {
            const toast = triggers['show-toast'];
            // Usar toastr con título y mensaje
            toastr[toast.type](toast.message, toast.title);
        }
    }
});

document.body.addEventListener('htmx:responseError', function (event) {
    const response = event.detail.xhr.response;
    try {
        const data = JSON.parse(response);
        if (data.errors) {
            for (const [field, error] of Object.entries(data.errors)) {
                toastr.error(`${field}: ${error}`);
            }
        }
    } catch (e) {
        console.error("Error parsing response:", e);
    }
});

document.body.addEventListener('htmx:afterRequest', function (event) {
  // Verifica si la solicitud fue exitosa y corresponde a una eliminación
  if (event.detail.successful && event.detail.elt.closest('form[hx-delete]')) {
    const userId = event.detail.elt.closest('tr').id;
    const row = document.getElementById(userId);
    if (row) row.remove();  // Elimina la fila manualmente
  }

  // Notificaciones con Toastr
  const trigger = event.detail.xhr.getResponseHeader('HX-Trigger');
  if (trigger) {
    const triggers = JSON.parse(trigger);
    if (triggers['show-toast']) {
      const toast = triggers['show-toast'];
      toastr[toast.type](toast.message, toast.title);
    }
  }
});





