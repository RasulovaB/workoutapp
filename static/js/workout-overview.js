if(document.readyState === "loading") {
    document.addEventListener('DOMContentLoaded', ready)
} else {
    ready()
}


function ready() {
    fetch('/get_exercises')
        .then(response => {
            if (response.ok) {
                response.json().then((data) => {
                    console.log('Success:', response);
                })
            } else {
                console.error('Error:', response);
            }

        })
        .catch((error) => {
            console.error('Error:', error);
        });
}