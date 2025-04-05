document.addEventListener('DOMContentLoaded', function() {
    // Show validation messages
    function showValidationMessage(field, message) {
        const errorDiv = document.createElement('div');
        errorDiv.className = 'invalid-feedback';
        errorDiv.textContent = message;
        field.parentNode.appendChild(errorDiv);
        field.classList.add('is-invalid');
    }

    // Clear validation messages
    function clearValidationMessages() {
        document.querySelectorAll('.invalid-feedback').forEach(el => el.remove());
        document.querySelectorAll('.is-invalid').forEach(el => el.classList.remove('is-invalid'));
    }
    const form = document.getElementById('carbonForm');
    const sections = document.querySelectorAll('.form-section');
    const nextButtons = document.querySelectorAll('.btn-next');
    const prevButtons = document.querySelectorAll('.btn-prev');
    const progressBar = document.querySelector('.progress-bar');
    const totalSections = sections.length;

    let currentSection = 0;

    // Initialize first section
    updateFormDisplay();

    // Next button click handler
    nextButtons.forEach(button => {
        button.addEventListener('click', () => {
            if (validateCurrentSection()) {
                currentSection++;
                updateFormDisplay();
            }
        });
    });

    // Previous button click handler
    prevButtons.forEach(button => {
        button.addEventListener('click', () => {
            currentSection--;
            updateFormDisplay();
        });
    });

    // Update form display
    function updateFormDisplay() {
        sections.forEach((section, index) => {
            if (index === currentSection) {
                section.style.display = 'block';
            } else {
                section.style.display = 'none';
            }
        });

        // Update progress bar
        const progress = ((currentSection + 1) / totalSections) * 100;
        progressBar.style.width = `${progress}%`;
        progressBar.setAttribute('aria-valuenow', progress);

        // Update button visibility
        updateNavigationButtons();
    }

    // Update navigation buttons
    function updateNavigationButtons() {
        prevButtons.forEach(button => {
            button.style.display = currentSection === 0 ? 'none' : 'block';
        });

        nextButtons.forEach(button => {
            if (currentSection === totalSections - 1) {
                button.textContent = 'Calculate';
                button.classList.remove('btn-next');
                button.classList.add('btn-submit');
            } else {
                button.textContent = 'Next';
                button.classList.add('btn-next');
                button.classList.remove('btn-submit');
            }
        });
    }

    // Validate current section
    function validateCurrentSection() {
        clearValidationMessages();
        const currentFields = sections[currentSection].querySelectorAll('input, select');
        let isValid = true;

        currentFields.forEach(field => {
            if (!field.value || field.value === '') {
                isValid = false;
                showValidationMessage(field, 'This field is required');
            }

            // Additional validation for numeric fields
            if (field.type === 'number' || field.type === 'float') {
                const value = parseFloat(field.value);
                if (isNaN(value) || value < 0) {
                    isValid = false;
                    showValidationMessage(field, 'Please enter a valid positive number');
                }
            }
        });

        if (!isValid) {
            const sectionTitle = sections[currentSection].querySelector('.section-title').textContent;
            alert(`Please complete all fields in the ${sectionTitle} section`);
        }

        return isValid;
    }

    // Form submission handler
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Validate all sections
        let allValid = true;
        sections.forEach((section, index) => {
            currentSection = index;
            if (!validateCurrentSection()) {
                allValid = false;
            }
        });

        if (allValid) {
            // Convert form data to JSON
            const formData = new FormData(form);
            const jsonData = {};
            formData.forEach((value, key) => {
                jsonData[key] = value;
            });

            // Submit form data via AJAX
            fetch('/results', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(jsonData)
            })
            .then(response => response.json())
            .then(data => {
                if (data.redirect) {
                    window.location.href = data.redirect;
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('There was an error submitting the form. Please try again.');
            });
        } else {
            alert('Please complete all required fields before submitting.');
        }
    });
});
