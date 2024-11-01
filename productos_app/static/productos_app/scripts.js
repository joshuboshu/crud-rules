// document.addEventListener("DOMContentLoaded", function () {
//     const form = document.querySelector("form");

//     if (form) {
//         form.addEventListener("submit", function(e) {
//             const precioInput = document.getElementById("id_precio"); 
//             const precio = precioInput ? parseFloat(precioInput.value) : NaN;
//             if (isNaN(precio) || precio <= 0) {
//                 alert("Por favor, introduce un precio válido.");
//                 e.preventDefault(); 
//             } else {
//                 if (!confirm("¿Estás seguro de que quieres agregar este producto?")) {
//                     e.preventDefault(); 
//                 }
//             }
//         });
//     }

//     const deleteLinks = document.querySelectorAll(".delete-product");
//     deleteLinks.forEach(link => {
//         link.addEventListener("click", function (e) {
//             if (!confirm("¿Estás seguro de que quieres eliminar este producto?")) {
//                 e.preventDefault();
//             }
//         });
//     });

//     const deleteCharacteristicLinks = document.querySelectorAll(".delete-characteristic");

//     deleteCharacteristicLinks.forEach(link => {
//         link.addEventListener("click", function (e) {
//             if (!confirm("¿Estás seguro de que quieres eliminar esta característica?")) {
//                 e.preventDefault();
//             }
//         });
//     });

//   const detailButtons = document.querySelectorAll(".product-actions a.btn-info");
//   detailButtons.forEach(button => {
//       button.addEventListener("click", function (e) {
//           const productoId = button.getAttribute("href").split('/').pop(); 
//           if (productoId) {
//               if (!confirm("¿Deseas ver los detalles de este producto?")) {
//                   e.preventDefault();
//               }
//           }
//       });
//   });
// });