// Get form and add event listener to submit button
const form = document.getElementById('add-doctor-form');
const submitBtn = form.querySelector('button[type="submit"]');
submitBtn.addEventListener('click', handleSubmit);

// Handle form submission
function handleSubmit(event) {
    event.preventDefault();

    // Get form data and create new doctor object
    const formData = new FormData(form);
    const newDoctor = {
        name: formData.get('name'),
        specialty: formData.get('specialty'),
        phone: formData.get('phone'),
        email: formData.get('email'),
        address: formData.get('address')
    };

    // Save new doctor to local storage
    saveDoctor(newDoctor);

    // Clear form and show success message
    form.reset();
    alert('Doctor added successfully!');
}

// Save doctor to local storage
function saveDoctor(doctor) {
    let doctors = JSON.parse(localStorage.getItem('doctors')) || [];
    doctors.push(doctor);
    localStorage.setItem('doctors', JSON.stringify(doctors));
}
