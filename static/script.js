// ---------------- CREATE ------------------ //
function submitCreateForm() {
    const data = {
        catalogue_name: document.getElementById("catalogueName").value,
        catalogue_description: document.getElementById("catalogueDescription").value,
        start_date: document.getElementById("startDate").value,
        end_date: document.getElementById("endDate").value
    };

    fetch("/catalogues", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
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

// ------------------ UPDATE ------------------ //
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
        headers: { "Content-Type": "application/json" },
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

// ------------------ DELETE ------------------ //
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

// ------------------ VIEW ALL (FILTER BY ID + PAGINATION) ------------------ //

function fetchAllCatalogues(page = 1, limit = 5) {
    const isHomePage = window.location.pathname === "/index";
    const finalLimit = isHomePage ? 1000 : limit;

    const url = `/catalogues?page=${page}&limit=${finalLimit}`;

    fetch(url)
    .then(res => res.json())
    .then(data => {
        const tableDiv = document.getElementById("catalogueTable");
        const paginationDiv = document.getElementById("pagination");

        if (!Array.isArray(data.data)) {
            tableDiv.innerHTML = `<p>Error: ${data.error}</p>`;
            return;
        }

        if (data.data.length === 0) {
            tableDiv.innerHTML = "<p>No catalogues found.</p>";
            if (!isHomePage) paginationDiv.innerHTML = "";
            return;
        }

        let html = `
            <table>
                <thead>
                    <tr><th>ID</th><th>Name</th><th>Description</th><th>Start Date</th><th>End Date</th></tr>
                </thead>
                <tbody>
        `;
        data.data.forEach(cat => {
            html += `
                <tr>
                    <td>${cat.catalogue_id}</td>
                    <td>${cat.catalogue_name}</td>
                    <td>${cat.catalogue_description}</td>
                    <td>${cat.start_date}</td>
                    <td>${cat.end_date}</td>
                </tr>
            `;
        });
        html += "</tbody></table>";
        tableDiv.innerHTML = html;

        // ------------------ PAGINATION ------------------ //
        if (!isHomePage) {
            const total = data.total || 0;
            const totalPages = Math.ceil(total / limit);
            let paginationHtml = "";

            for (let i = 1; i <= totalPages; i++) {
                paginationHtml += `<button onclick="fetchAllCatalogues(${i}, ${limit})">${i}</button> `;
            }

            paginationDiv.innerHTML = paginationHtml;
        } else {
            paginationDiv.innerHTML = ""; // Hide pagination on homepage
        }
    })
    .catch(error => {
        document.getElementById("catalogueTable").innerText = "Error: " + error;
    });
}
       
// ------------------ FILTER BY ID ------------------ //
function filterById() {
    const id = document.getElementById("searchInput").value.trim();

    if (!id) {
        fetchAllCatalogues(); // Reset to full list
        return;
    }

    fetch(`/catalogues/${id}`)
    .then(res => res.json())
    .then(data => {
        const tableDiv = document.getElementById("catalogueTable");
        const paginationDiv = document.getElementById("paginationContainer");
        paginationDiv.innerHTML = ""; // hide pagination on filtered view

        if (data.status === "success") {
            const cat = data.data;
            const html = `
                <table>
                    <thead>
                        <tr><th>ID</th><th>Name</th><th>Description</th><th>Start Date</th><th>End Date</th></tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>${cat.catalogue_id}</td>
                            <td>${cat.catalogue_name}</td>
                            <td>${cat.catalogue_description}</td>
                            <td>${cat.start_date}</td>
                            <td>${cat.end_date}</td>
                        </tr>
                    </tbody>
                </table>
            `;
            tableDiv.innerHTML = html;
        } else {
            tableDiv.innerHTML = `<p>${data.error || "No data found"}</p>`;
        }
    })
    .catch(error => {
        document.getElementById("catalogueTable").innerText = "Error: " + error;
    });
}

// ------------------ LOGIN ------------------ //
function submitLoginForm() {
    const credentials = {
        username: document.getElementById("username").value,
        password: document.getElementById("password").value
    };

    fetch("/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(credentials)
    })
    .then(res => res.json())
    .then(response => {
        const msgDiv = document.getElementById("loginResponse");
        if (response.token) {
            msgDiv.style.color = "green";
            msgDiv.innerText = "Login successful!";
            // redirect after success
            setTimeout(() => {
                
                window.location.href = "/index";

            }, 1500);
        } else {
            msgDiv.style.color = "red";
            msgDiv.innerText = response.error || "Login failed";
        }
    })
    .catch(error => {
        document.getElementById("loginResponse").innerText = "Error: " + error;
    });
}

// ------------------ INIT ------------------ //
document.addEventListener("DOMContentLoaded", () => {
    const path = window.location.pathname;

    if (path === "/view") {
        fetchAllCatalogues();  // Paginated version for view_all
        const searchBtn = document.getElementById("searchBtn");
        if (searchBtn) {
            searchBtn.addEventListener("click", filterById);
        }
    } else if (path === "/index") {
        // Fetch all catalogues without pagination (high limit)
        fetchAllCatalogues(1, 1000);
    }
});
