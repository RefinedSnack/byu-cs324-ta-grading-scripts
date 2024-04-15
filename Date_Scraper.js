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
        line += '\"\"';
    }
    console.log(line);
    results += line + '\n'
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
    var docName = document.querySelector('.selectedAssignment');

    // Check if the element exists
    if (docName !== null) {
        // Get the text content of the element and replace spaces with underscores
        var assignmentName = docName.textContent.trim().replace(/\s/g, '_');
    } else {
        // Set the variable to 'Submission_Dates' if the element is not found
        var assignmentName = 'Submission_Dates';
    }

    // Add .csv to the end of assignmentName
    assignmentName += '.csv';
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
    saveStringToFile(results, assignmentName)
}

// Set to a big number because it will crash
run(1000)