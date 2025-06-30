// CREATE catalogue
function submitCreateForm() {
    const data = {
        catalogue_name: document.getElementById("catalogueName").value,
        catalogue_description: document.getElementById("catalogueDescription").value,
        start_date: document.getElementById("startDate").value,
        end_date: document.getElementById("endDate").value
    };

    fetch("/catalogues", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(response => {
        document.getElementById("createResponse").innerText = response.message || response.error;
    })
    .catch(error => {
        document.getElementById("createResponse").innerText = "Error: " + error;
    });
}

// UPDATE catalogue
function submitUpdateForm() {
    const catalogueId = document.getElementById("catalogueId").value;
    const data = {
        catalogue_name: document.getElementById("catalogueName").value,
        catalogue_description: document.getElementById("catalogueDescription").value,
        start_date: document.getElementById("startDate").value,
        end_date: document.getElementById("endDate").value
    };

    fetch(`/catalogues/${catalogueId}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(response => {
        document.getElementById("updateResponse").innerText = response.message || response.error;
    })
    .catch(error => {
        document.getElementById("updateResponse").innerText = "Error: " + error;
    });
}

// DELETE catalogue
function submitDeleteForm() {
    const catalogueId = document.getElementById("catalogueId").value;

    fetch(`/catalogues/${catalogueId}`, {
        method: "DELETE"
    })
    .then(res => res.json())
    .then(response => {
        document.getElementById("deleteResponse").innerText = response.message || response.error;
    })
    .catch(error => {
        document.getElementById("deleteResponse").innerText = "Error: " + error;
    });
}

// VIEW ALL catalogues
function fetchAllCatalogues() {
    fetch("/catalogues")
    .then(res => res.json())
    .then(data => {
        const tableDiv = document.getElementById("catalogueTable");
        if (!Array.isArray(data)) {
            tableDiv.innerHTML = `<p>Error: ${data.error}</p>`;
            return;
        }

        if (data.length === 0) {
            tableDiv.innerHTML = "<p>No catalogues found.</p>";
            return;
        }

        let html = "<table><thead><tr><th>ID</th><th>Name</th><th>Description</th><th>Start Date</th><th>End Date</th></tr></thead><tbody>";
        data.forEach(cat => {
            html += `<tr>
                        <td>${cat.catalogue_id}</td>
                        <td>${cat.catalogue_name}</td>
                        <td>${cat.catalogue_description}</td>
                        <td>${cat.start_date}</td>
                        <td>${cat.end_date}</td>
                     </tr>`;
        });
        html += "</tbody></table>";
        tableDiv.innerHTML = html;
    })
    .catch(error => {
        document.getElementById("catalogueTable").innerText = "Error: " + error;
    });
}
