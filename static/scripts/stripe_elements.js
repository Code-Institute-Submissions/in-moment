const stripe_public_key = $("#id_stripe_public_key").text().slice(1, -1);
const client_secret = $("#id_client_secret").text().slice(1, -1);
const stripe = Stripe(stripe_public_key);
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