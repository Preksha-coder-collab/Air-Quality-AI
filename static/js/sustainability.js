function calculateScore() {

    let score = 0;

    document
    .querySelectorAll(
        '.form-check-input:checked'
    )
    .forEach(item => {

        score +=
        parseInt(item.value);

    });

    document.getElementById(
        "greenScore"
    ).innerHTML =

    `Green Score : ${score}/100`;

    let badge = "";

    if(score >= 80)
        badge =
        "🏆 Sustainability Champion";

    else if(score >= 50)
        badge =
        "🌿 Green Citizen";

    else
        badge =
        "🌱 Eco Beginner";

    document.getElementById(
        "badge"
    ).innerHTML = badge;

}

const challenges = [

"Use public transport today",

"Carry a reusable water bottle",

"Avoid single-use plastic",

"Plant one tree",

"Switch off unused lights"

];

const day =
new Date().getDate();

document.getElementById(
"challengeText"
).innerHTML =

challenges[
day % challenges.length
];