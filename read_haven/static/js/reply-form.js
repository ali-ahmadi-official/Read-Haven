const ReplysBtn = document.querySelectorAll("#btn");

ReplysBtn.forEach((button) => {
    const ReplyForm = button.nextElementSibling;
    button.addEventListener('click', () => {
        ReplyForm.classList.toggle("flex");
    });
});