document.addEventListener("DOMContentLoaded", function () {
    // Validación del formulario de agregar producto (si es que existe)
    const form = document.querySelector("form");

    if (form) {
        form.addEventListener("submit", function(e) {
            // Obtener el valor del campo precio
            const precioInput = document.getElementById("id_precio"); // Asegúrate de que el ID sea correcto
            const precio = precioInput ? parseFloat(precioInput.value) : NaN;
            // Validar que el campo de precio solo acepte números y que el precio sea mayor a 0
            if (isNaN(precio) || precio <= 0) {
                alert("Por favor, introduce un precio válido.");
                e.preventDefault(); // Evitar el envío del formulario
            } else {
                // Mostrar mensaje de confirmación antes de agregar el producto
                if (!confirm("¿Estás seguro de que quieres agregar este producto?")) {
                    e.preventDefault(); // Evitar el envío del formulario
                }
            }
        });
    }

    // Consulta para eliminar un producto
    const deleteLinks = document.querySelectorAll(".delete-product");
    deleteLinks.forEach(link => {
        link.addEventListener("click", function (e) {
            // Mostrar mensaje de confirmación antes de eliminar el producto
            if (!confirm("¿Estás seguro de que quieres eliminar este producto?")) {
                e.preventDefault();
            }
        });
    });

  // Consulta para eliminar una característica
    const deleteCharacteristicLinks = document.querySelectorAll(".delete-characteristic");

    deleteCharacteristicLinks.forEach(link => {
        link.addEventListener("click", function (e) {
            // Mostrar este mensaje de confirmación antes de eliminar la característica
            if (!confirm("¿Estás seguro de que quieres eliminar esta característica?")) {
                e.preventDefault();
            }
        });
    });

  // Redirección al detalle del producto (en caso de ser necesario)
  const detailButtons = document.querySelectorAll(".product-actions a.btn-info");
  detailButtons.forEach(button => {
      button.addEventListener("click", function (e) {
          const productoId = button.getAttribute("href").split('/').pop(); // Obtener el id del href
          if (productoId) {
              if (!confirm("¿Deseas ver los detalles de este producto?")) {
                  e.preventDefault();
              }
          }
      });
  });
});