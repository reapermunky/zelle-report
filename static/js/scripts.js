document.addEventListener("DOMContentLoaded", function () {
    const reportForm = document.querySelector("#reportForm");

    if (reportForm) {
        reportForm.addEventListener("submit", function (event) {
            let bank = document.querySelector("input[name='bank']").value.trim();
            let issue = document.querySelector("input[name='issue']").value.trim();

            if (!bank || !issue) {
                event.preventDefault();
                alert("Please fill in all required fields (Bank & Issue).");
            }
        });
    }

    // Fetch reports dynamically
    fetch("/get_reports")
        .then(response => response.json())
        .then(data => {
            const reportsList = document.querySelector("#reportsList");
            if (reportsList) {
                reportsList.innerHTML = ""; // Clear existing content
                data.forEach(report => {
                    let listItem = document.createElement("li");
                    listItem.innerHTML = `<strong>${report.bank}</strong> - ${report.issue} (Reported by: ${report.name})`;
                    reportsList.appendChild(listItem);
                });
            }
        })
        .catch(error => console.error("Error fetching reports:", error));
});
