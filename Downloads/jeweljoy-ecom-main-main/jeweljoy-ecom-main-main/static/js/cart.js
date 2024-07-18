document.addEventListener('DOMContentLoaded', () => {
    renderCart();

    function renderCart() {
        let cart = JSON.parse(localStorage.getItem('cart')) || [];
        let cartContainer = document.getElementById('cart-container');

        if (cart.length === 0) {
            cartContainer.innerHTML = '<p>Su carrito está vacío.</p>';
            return;
        }

        let total = 0;
        let cartHTML = `
            <table class="cart-table">
                <thead>
                    <tr>
                        <th>Producto</th>
                        <th>Imagen</th>
                        <th>Cantidad</th>
                        <th>Precio Unitario</th>
                        <th>Total</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
        `;

        cart.forEach((item, index) => {
            total += item.price * item.quantity;
            cartHTML += `
                <tr>
                    <td>${item.name}</td>
                    <td><img src="${item.image}" alt="${item.name}"></td>
                    <td>
                        <input type="number" value="${item.quantity}" min="1" data-index="${index}" class="quantity-input">
                    </td>
                    <td>$${item.price}</td>
                    <td>$${item.price * item.quantity}</td>
                    <td><button onclick="removeFromCart(${index})">Eliminar</button></td>
                </tr>
            `;
        });

        cartHTML += `
                </tbody>
            </table>
            <div class="cart-total">
                <h3>Total: $${total}</h3>
                <a href="/checkout/" class="checkout-btn">Ir a Pagar</a>
            </div>
        `;

        cartContainer.innerHTML = cartHTML;

        // Agregar eventos de cambio a los campos de entrada de cantidad
        document.querySelectorAll('.quantity-input').forEach(input => {
            input.addEventListener('change', updateQuantity);
        });
    }

    function updateQuantity(event) {
        let index = event.target.getAttribute('data-index');
        let newQuantity = parseInt(event.target.value);
        let cart = JSON.parse(localStorage.getItem('cart')) || [];

        if (newQuantity > 0) {
            cart[index].quantity = newQuantity;
            localStorage.setItem('cart', JSON.stringify(cart));
            renderCart(); // Volver a renderizar el carrito
        }
    }

    window.removeFromCart = function(index) {
        let cart = JSON.parse(localStorage.getItem('cart')) || [];
        cart.splice(index, 1); // Eliminar el producto del carrito
        localStorage.setItem('cart', JSON.stringify(cart));
        renderCart(); // Volver a renderizar el carrito
    };
});

