
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
        console.log(field)
        console.log(time)

        newShift[field] = time;
    }

    console.log(newShift);


});

