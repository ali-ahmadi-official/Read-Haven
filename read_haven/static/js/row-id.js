const rows = Array.from(document.querySelectorAll("#row")).reverse();

rows.forEach((row, index) => {
    index++;
    row.innerHTML = index;
});