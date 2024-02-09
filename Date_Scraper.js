var num = 1;
var results = '';
function get() {
    var line = ''
    var studentElement = document.querySelector('.dropElement-' + String(num) + '.selectedStudent');
    line += String(num) + ",\"";
    if (studentElement) {
        line += studentElement.innerText + '\",';
    }
    else {
        return false;
    }
    var submissionToggleElement = document.getElementById('submission0Toggle');
    if (submissionToggleElement) {
        line += '\"' + submissionToggleElement.innerText + '\"';
    }
    else {
        line += '\"empty\"';
    }
    console.log(line);
    results += line
    num += 1;
    document.getElementById('studentNextBtn').click();
    return true;
}

function saveStringToFile(content, fileName) {
    // Create a Blob from the string content
    const blob = new Blob([content], { type: 'text/plain' });

    // Create a download link
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = fileName;

    // Append the link to the document
    document.body.appendChild(link);

    // Trigger a click on the link to start the download
    link.click();

    // Remove the link from the document
    document.body.removeChild(link);
}

function run(times) {
    num = 1;
    results = 'roleNum,Name,Date\n'
    try {
        for (let i = 0; i < times; i++) {
            if (!get()) {
                break;
            }
        }
    }
    catch (error) {
        console.log(error)
    }
    saveStringToFile(results, "Submission_Dates.csv")
}

// Set to a big number because it will crash
run(1000)