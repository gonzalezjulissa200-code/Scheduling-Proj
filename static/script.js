// checks for all inputs that are under business time
const input = document.querySelectorAll(".business-time");

//adds an event listener for each of them
for (let i = 0; i < input.length; i++) {
    input[i].addEventListener("change", function() 
    {
        const day = this.dataset.day;
        const field = this.dataset.field;
        const time = this.value;
        fetch("/update-hours", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                day: day,
                field: field,
                time: time
            })
        });
    });
}
