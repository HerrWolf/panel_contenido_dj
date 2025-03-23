$(document).ready(function () {
    // Inicializa Select2 cuando el documento esté listo
    // initializeSelect2();

    document.body.addEventListener('close-modal', function () {
        var modal = bootstrap.Modal.getInstance(document.getElementById('movie-modal'));
        modal.hide();
    });
});

// Función para inicializar Select2
function initializeSelect2() {
    const selectElement = document.getElementById('id_categories');
    if (!selectElement) {
        console.error("Select element not found!");
        return;
    }

    console.log("Initializing Select2...");

    // Destruir instancia previa si existe
    try {
        $('#id_categories').select2('destroy');
    } catch (e) {
        console.log("No hay instancia previa para destruir");
    }

    // Importante: guarda los valores seleccionados antes de reinicializar
    const selectedValues = Array.from(selectElement.options)
        .filter(opt => opt.selected)
        .map(opt => opt.value);

    console.log("Valores seleccionados antes de inicializar:", selectedValues);

    // Reinicializar Select2
    $('#id_categories').select2({
        width: '100%',
        dropdownParent: $("#movie-modal"),
        placeholder: "Selecciona categorías"
    });

    // Restaurar los valores seleccionados después de inicializar
    if (selectedValues.length > 0) {
        $('#id_categories').val(selectedValues).trigger('change');
        console.log("Valores restaurados después de inicializar Select2");
    }
}

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

document.addEventListener('htmx:afterSwap', function (event) {
    // Añade este log para verificar qué se está intercambiando
    console.log("HTMX afterSwap - Target ID:", event.detail.target.id);

    // Solo inicializa Select2 cuando el formulario de película se carga
    if (event.detail.target.id === "movie-form") {
        console.log("Formulario cargado por HTMX, inicializando Select2...");

        // Espera un poco más para asegurar que el DOM esté completamente listo
        setTimeout(function() {
            initializeSelect2();
        }, 200);
    }

    // Flag to prevent recursive searches
    let isAutoFilling = false;

    // Event handler for TMDB ID search (existing functionality)
    $('#id_tmdb_id').on('keyup', function () {
        if (isAutoFilling) return; // Skip if auto-filling

        const tmdb_id = $(this).val().trim();

        // Validar que sea un ID válido
        if (!tmdb_id || isNaN(tmdb_id)) return;

        // Añadir un retraso para evitar múltiples solicitudes
        clearTimeout($(this).data('timer'));
        $(this).data('timer', setTimeout(function () {
            // Mostrar un indicador de carga
            $('#movie-list-results').html('<div class="text-center"><i class="fas fa-spinner fa-spin"></i> Buscando película...</div>');

            // Realizar la solicitud AJAX
            $.ajax({
                url: '/dashboard/movie/fetch/',
                data: {tmdb_id: tmdb_id},
                success: function (movie_data) {

                    console.log('movie_data', movie_data);

                    isAutoFilling = true; // Set flag before auto-filling

                    // Actualizar campos del formulario directamente
                    $('#id_tmdb_id').val(movie_data.tmdb_id);
                    $('#id_title').val(movie_data.title);
                    $('#id_original_title').val(movie_data.original_title);
                    $('#id_poster_url').val(movie_data.poster_url);
                    $("#id_backdrop_url").val(movie_data.backdrop_url);
                    $('#id_overview').val(movie_data.overview);
                    $('#id_release_date').val(movie_data.release_date.substring(0, 4));
                    $('#id_video_path').val(movie_data.video_path || '');

                    isAutoFilling = false; // Reset flag after auto-filling

                    updateMoviePreview(movie_data);
                },
                error: function (xhr) {
                    const errorData = JSON.parse(xhr.responseText);
                    $('#movie-list-results').html(`<div class="alert alert-danger">Error: ${errorData.error}</div>`);
                }
            });
        }, 800));
    });

    // New event handler for title search
    $('#id_title').on('keyup', function () {
        if (isAutoFilling) return; // Skip if auto-filling

        const title = $(this).val().trim();

        // Validate title has enough characters
        if (!title || title.length < 3) return;

        // Delay to avoid multiple requests
        clearTimeout($(this).data('timer'));
        $(this).data('timer', setTimeout(function () {
            // Show loading indicator
            $('#movie-list-results').html('<div class="text-center"><i class="fas fa-spinner fa-spin"></i> Buscando películas...</div>');

            // Make AJAX request
            $.ajax({
                url: '/dashboard/movie/search/',
                data: {title: title},
                success: function (results) {


                    // Display search results
                    if (results.length === 0) {
                        $('#movie-list-results').html('<div class="alert alert-warning">No se encontraron películas con ese título</div>');
                        return;
                    }

                    let resultHtml = '<div class="list-group mb-3">';
                    results.forEach(function (movie) {
                        let year = movie.release_date ? ` (${movie.release_date.substring(0, 4)})` : '';
                        resultHtml += `
                            <a href="#" class="list-group-item list-group-item-action movie-result" data-tmdb-id="${movie.tmdb_id}">
                                <div class="d-flex align-items-center">
                                    ${movie.poster_path ?
                            `<img src="${movie.poster_path}" class="me-3" style="width: 50px; height: auto;">` :
                            `<div class="me-3" style="width: 50px; height: 75px; background: #eee; display: flex; align-items: center; justify-content: center;"><i class="ti ti-photo-off"></i></div>`
                        }
                                    <div>
                                        <h6 class="mb-1">${movie.title}${year}</h6>
                                        <small>${movie.original_title || ''}</small>
                                    </div>
                                </div>
                            </a>
                        `;
                    });
                    resultHtml += '</div>';

                    $('#movie-list-results').html(resultHtml);

                    // Add click event to results
                    $('.movie-result').on('click', function (e) {
                        e.preventDefault();
                        const tmdbId = $(this).data('tmdb-id');

                        // Clear results and set TMDB ID field
                        $('#movie-list-results').html('<div class="text-center"><i class="fas fa-spinner fa-spin"></i> Cargando información de película...</div>');
                        isAutoFilling = true;
                        $('#id_tmdb_id').val(tmdbId);
                        isAutoFilling = false;

                        // Fetch complete movie data
                        $.ajax({
                            url: '/dashboard/movie/fetch/',
                            data: {tmdb_id: tmdbId},
                            success: function (movie_data) {
                                isAutoFilling = true;

                                // Update form fields
                                $('#id_tmdb_id').val(movie_data.tmdb_id);
                                $('#id_title').val(movie_data.title);
                                $('#id_original_title').val(movie_data.original_title);
                                $('#id_poster_url').val(movie_data.poster_url);
                                $("#id_backdrop_url").val(movie_data.backdrop_url);
                                $('#id_overview').val(movie_data.overview);
                                $('#id_video_path').val(movie_data.video_path || '');

                                isAutoFilling = false;

                                updateMoviePreview(movie_data);
                            },
                            error: function (xhr) {
                                const errorData = JSON.parse(xhr.responseText);
                                $('#movie-list-results').html(`<div class="alert alert-danger">Error: ${errorData.error}</div>`);
                            }
                        });
                    });
                },
                error: function (xhr) {
                    const errorData = JSON.parse(xhr.responseText);
                    $('#movie-list-results').html(`<div class="alert alert-danger">Error: ${errorData.error}</div>`);
                }
            });
        }, 800));
    });

    // Helper function to update movie preview
    function updateMoviePreview(movie_data) {
        // Update poster preview
        if (movie_data.poster_url) {
            $('#poster-view').html(`
                <div class="d-flex my-3" style="max-height: 400px; overflow: hidden;">
                    <div class="w-35 pe-2 d-flex align-items-center justify-content-center">
                        <img src="${movie_data.poster_url}" class="img-fluid rounded h-auto" style="object-fit: contain; max-height: 400px;" alt="Poster">
                    </div>
                    <div class="w-auto ps-2 pe-2 d-flex align-items-center justify-content-center">
                        <img src="${movie_data.backdrop_url}" class="img-fluid rounded h-auto" style="object-fit: contain; max-height: 400px;" alt="Backdrop">
                    </div>
                </div>
            `);
        }

        // Update category badges
        if (movie_data.categories && movie_data.categories.length > 0) {
            let categoryBadges = '';

            movie_data.categories.forEach(function (category) {
                categoryBadges += `<span class="mb-1 badge font-medium bg-light-secondary text-secondary">${category.name}</span> `;
            });

            $('#movie-category-example').html(`
                <div class="card w-100">
                  <div class="card-body">
                    <h6>Categorías recomendadas</h6>
                    ${categoryBadges}
                  </div>
                </div>
            `);
        }

        // Clear results list after successful fetch
        $('#movie-list-results').html('');
    }
});