let form = document.querySelector('form')

form.addEventListener('submit', (event) => {
    event.preventDefault()
    let formData = new FormData(form)
    let data = {}
    console.log(formData.get('hobbies'))
    formData.forEach((value, key) => {
        data[key] = value
    })
    if (!data.name) {
        alert("You can't submit the form like that, mr. Anonymous!")
        return
    }
    if (!data.email) {
        alert("We don't want to lose you, please provide an email, so we can contact you!")
        return;
    }
    if (data.color === '#000000') {
        alert("Hey, don't be shy, choose a favourite color!")
        return;
    }
    if (!data.hobbies) {
        if (!confirm('Are you sure you have no hobbies?')) {
            return;
        }
    }
    form.submit()
})