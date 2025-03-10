document.addEventListener("DOMContentLoaded", () => {
    const noBox = document.getElementById("noBox");
    const yesBtn = document.getElementById("yesBtn");
    const love = document.getElementById("love");


    noBox.addEventListener("mouseenter", () => {
        noBox.classList.toggle("move-up");
    });

    yesBtn.addEventListener("click", () => {
        love.innerText = "I love you too ❤️";
        love.style.opacity = "1";
    });
});
