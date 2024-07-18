document.addEventListener('DOMContentLoaded', function() {
    const checkoutForm = document.getElementById('checkout-form');

    checkoutForm.addEventListener('submit', function(event) {
        event.preventDefault();

        // Aquí puedes añadir validaciones adicionales si es necesario
        // Por ejemplo, asegurarte de que todos los campos están llenos

        // Obtener los datos del carrito desde localStorage
        let cart = JSON.parse(localStorage.getItem('cart')) || [];

        if (cart.length === 0) {
            alert('El carrito está vacío. Añada productos antes de proceder al pago.');
            return;
        }

        // Aquí podrías integrar la lógica de procesamiento de pago con un servicio de terceros
        // Por simplicidad, solo mostraremos un mensaje de confirmación

        alert('Compra realizada con éxito. Gracias por su compra.');

        // Limpiar el carrito
        localStorage.removeItem('cart');

        // Redirigir a la página principal o a una página de confirmación
        window.location.href = '/';  // Cambia esta URL según sea necesario
    });
});
