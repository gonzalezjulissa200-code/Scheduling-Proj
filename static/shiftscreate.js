
const popup = document.getElementById("shiftadding_button");
const createshift = document.getElementById("finish_shift");

popup.addEventListener("click", function() 
{
    ShiftsEdits = document.querySelector("#PopUP_shifts");

    ShiftsEdits.classList.toggle("hidden")

});

createshift.addEventListener("click", function()
{
    const newShift = {};

    const shift= document.querySelectorAll(".shiftDate");
    for (let i = 0; i < shift.length; i++) 
    {
        const field = shift[i].dataset.field
        const time = shift[i].value
        const amount = shift[i].dataset.capacity
        console.log(field)
        console.log(time)
        console.log(amount)

        newShift[field] = time;
    }

    console.log(newShift);

    fetch("/create-shift", {
        method: "POST",
            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(newShift)
    });

});

