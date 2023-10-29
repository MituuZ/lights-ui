function selectOption(selectedCell) {
    const row = selectedCell.parentElement;
    const buttons = row.getElementsByClassName('button');
    for (const button of buttons) {
        button.classList.remove('selected');
    }
    selectedCell.classList.add('selected');
}
