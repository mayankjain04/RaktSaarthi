const donorForm = document.querySelector('.blood-donation-form-box.blood-donation-visible');
const recipientForm = document.querySelector('.blood-donation-form-box.blood-donation-recipient');

document.querySelector('.recipient-link').addEventListener('click', function(event) {
    event.preventDefault();
    switchForm(donorForm, recipientForm);
});

document.querySelector('.donor-link').addEventListener('click', function(event) {
    event.preventDefault();
    switchForm(recipientForm, donorForm);
});

function switchForm(hideForm, showForm) {
    hideForm.classList.add('blood-donation-hidden');
    setTimeout(() => {
        hideForm.style.display = 'none';
        showForm.style.display = 'block';
        setTimeout(() => {
            showForm.classList.remove('blood-donation-hidden');
            showForm.classList.add('blood-donation-visible');
        }, 50);
    }, 400); // Delay to match animation duration
}

// Close button
document.querySelector('.blood-donation-icon-close').addEventListener('click', function() {
    document.querySelector('.blood-donation-wrapper').style.display = 'none';
});

// Open form
document.querySelector('.blood-donation-btn-toggle').addEventListener('click', function() {
    document.querySelector('.blood-donation-wrapper').style.display = 'block';
});
