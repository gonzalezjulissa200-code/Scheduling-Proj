// checks for all inputs that are under business time
const input = document.querySelectorAll(".business-time");

//adds an event listener for each of the numbers changed
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

//creates the rows on my week table
function addScheduleRow(hour) {
    const scheduleBody = document.getElementById("schedule-body");

    const row = document.createElement("div");
    row.classList.add("schedule-row");

    const time = document.createElement("div");
    time.classList.add("schedule-time");
    time.textContent = hour;
    row.appendChild(time);

    for (let i = 0; i < 7; i++) {
        const dayCell = document.createElement("div");
        row.appendChild(dayCell);
    }

    scheduleBody.appendChild(row);
}

//gets all opening hours
const openInputs = document.querySelectorAll(
    '.business-time[data-field="open"]'
);
//put all actual values in an array i can manipulate
const morninghours = []
for(let i = 0; i <= openInputs.length - 1; i++)
{
    const temp = openInputs[i].value
    morninghours.push(temp)
    //console.log(temp);
}
//console.log(morninghours);
morninghours.sort((a, b) => a.localeCompare(b, undefined, { numeric: true }));
console.log(morninghours);
earlyhours = morninghours[0]
console.log(earlyhours)



//gets the closing hours inputs and sorts them
const closinghours = []
const closeInputs = document.querySelectorAll(
    '.business-time[data-field="close"]'
);
for(let i = 0; i <= closeInputs.length - 1; i++)
{
    const temp2 = closeInputs[i].value
    closinghours.push(temp2)
    //console.log(temp2);
}
// = [//].sort((a,b) => b-a);
closinghours.sort((a, b) => a.localeCompare(b, undefined, { numeric: true }));
console.log(closinghours);
latehours = closinghours[closinghours.length - 1]
console.log(latehours)

//helper def
const makemin = (timed) => 
{
    const hours = parseInt(timed.substring(0,2),10);
    const minutes = parseInt(timed.substring(3,5),10);
    return hours * 60 + minutes;
};



//used to find the gap inbetween a start and end time
function timeConversion(constart, conend)
{
    let starting = makemin(constart);
    let ending = makemin(conend);
    
    const diffMinutes = ending - starting
    const diffHours = Math.floor(diffMinutes / 60);
    const remainingMins = diffMinutes % 60;

    const pad = (num) => String(num).padStart(2, '0');
    return `${pad(diffHours)}:${pad(remainingMins)}`;
}

//shows the difference by calling timeConversion and console logging it
//complete = timeConversion(earlyhours, latehours)
//console.log(complete)

let beginning = makemin(earlyhours)
const ending = makemin(latehours)

while(beginning <= ending)
{
    const hourtime = Math.floor(beginning / 60)
    const minutetime = (beginning % 60)
    const pad2 = (num) => String(num).padStart(2, '0');
    let showing = `${pad2(hourtime)}:${pad2(minutetime)}`
    addScheduleRow(showing)
    beginning += 60
}

