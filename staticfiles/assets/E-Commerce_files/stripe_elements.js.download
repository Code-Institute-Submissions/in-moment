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
    const saveInfo = Boolean($("#id-save-info").attr("cheked"));
    const csrfToken = $("input[name='csrfmiddlewaretoken']").val();
    const postData = {
        "csrfmiddlewaretoken": csrfToken,
        "client_scret": clientSecret,
        "save_info": saveInfo
    };
    const url = "/checkout/cache_checkout_data/";
    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_detail: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address: {
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        county: $.trim(form.county.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    postcode: $.trim(form.postcode.value),
                    county: $.trim(form.county.value),
                }
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
    }).fail(function () {
        location.reload();
    });
});