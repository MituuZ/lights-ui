function selectOption(selectedCell, comment, updateType) {
    const row = selectedCell.parentElement;
    const buttons = row.getElementsByClassName('button');
    for (const button of buttons) {
        button.classList.remove('selected');
    }
    selectedCell.classList.add('selected');
    console.log('Pressed button: ' + comment + ". With updateType: " + updateType);
    if (updateType === 'disable') {
        disableCronJob(comment);
    } else {
        updateCronJob(updateType, comment)
    }
}

function updateCronJob(updateType, comment) {
    fetch('/update_cron', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=UTF-8'
        },
        body: JSON.stringify({
            schedule: updateType,
            job_comment: comment
        })
    })
    .then(response => response.json())
    .catch(error => alert('Failed to update cron job'));
}

function disableCronJob(comment) {
    fetch('/disable_cron', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=UTF-8'
        },
        body: JSON.stringify({
            job_comment: comment
        })
    })
    .then(response => response.json())
    .catch(error => alert('Failed to update cron job'));
}
