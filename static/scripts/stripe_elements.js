const stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
const clientSecret = $("#id_client_secret").text().slice(1, -1);
const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();
var card = elements.create('card', {
    'style': {
        'base': {
            'fontFamily': 'Arial, sans-serif',
            'fontSize': '1rem',
            'color': '#C1C7CD',
        },
        'invalid': {
            'color': 'red',
        },
    }
});
card.mount("#card-element");

// Handle realtime validation errors on the card element
card.addEventListener('change', function (e) {
    const errorDiv = document.getElementById('card-errors');
    if (e.error) {
        const html = `<span>${e.error.message}</span>`;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
const form = document.getElementById('payment-form');

form.addEventListener('submit', function (e) {
    ev.preventDefault();
    card.update({ 'disabled': true });
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function (result) {
        if (result.error) {
            const errorDiv = document.getElementById('card-errors');
            const html = `<span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false });
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});