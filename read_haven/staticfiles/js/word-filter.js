function limitWords(event) {
    const maxWords = 800;
    const input = event.target;
    const words = input.value.split(/\s+/);
    if (words.length > maxWords) {
        input.value = words.slice(0, maxWords).join(" ");
    }
}