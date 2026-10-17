const workloadForm = document.getElementById("workloadForm");
const workloadTable = document.getElementById("workloadTable");
const workloadMessage = document.getElementById("workloadMessage");
const userName = document.getElementById("userName");
const workloads = [];

const demoUser = JSON.parse(sessionStorage.getItem("greenscaleDemoUser") || "null");
if (demoUser && demoUser.name) {
  userName.textContent = demoUser.name;
}

function showWorkloadMessage(message, type) {
  workloadMessage.textContent = message;
  workloadMessage.className = `alert alert-${type}`;
}

function renderWorkloads() {
  workloadTable.innerHTML = "";

  if (workloads.length === 0) {
    workloadTable.innerHTML = '<tr><td colspan="4" class="text-center py-5 text-secondary">No workloads yet. Submit one using the form.</td></tr>';
  } else {
    workloads.forEach((job) => {
      const row = document.createElement("tr");

      const nameCell = document.createElement("td");
      const name = document.createElement("div");
      name.className = "fw-semibold";
      name.textContent = job.name;
      const type = document.createElement("div");
      type.className = "small text-secondary";
      type.textContent = job.type;
      nameCell.append(name, type);

      const resourceCell = document.createElement("td");
      resourceCell.textContent = `${job.cpu} CPU · ${job.ram} GB`;

      const priorityCell = document.createElement("td");
      const priorityBadge = document.createElement("span");
      priorityBadge.className = `priority-pill priority-${job.priority.toLowerCase()}`;
      priorityBadge.textContent = job.priority;
      priorityCell.appendChild(priorityBadge);

      const statusCell = document.createElement("td");
      const statusBadge = document.createElement("span");
      statusBadge.className = "status-pill";
      statusBadge.textContent = "Queued (demo)";
      statusCell.appendChild(statusBadge);

      row.append(nameCell, resourceCell, priorityCell, statusCell);
      workloadTable.appendChild(row);
    });
  }

  document.getElementById("totalCount").textContent = workloads.length;
  document.getElementById("queuedCount").textContent = workloads.length;
  document.getElementById("highCount").textContent = workloads.filter(job => ["High", "Critical"].includes(job.priority)).length;
}

workloadForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const runtime = Number(document.getElementById("runtime").value);
  if (!Number.isFinite(runtime) || runtime < 1) {
    showWorkloadMessage("Enter a runtime of at least one minute.", "danger");
    return;
  }

  const job = {
    id: Date.now(),
    name: document.getElementById("workloadName").value.trim(),
    type: document.getElementById("workloadType").value,
    cpu: document.getElementById("cpu").value,
    ram: document.getElementById("ram").value,
    priority: document.getElementById("priority").value,
    flexibility: document.getElementById("flexibility").value,
    objective: document.getElementById("objective").value,
    runtime: runtime
  };

  workloads.unshift(job);
  renderWorkloads();
  workloadForm.reset();
  showWorkloadMessage("Workload added to this demo dashboard. No cloud job was launched.", "success");
});

document.getElementById("clearBtn").addEventListener("click", () => {
  workloads.length = 0;
  renderWorkloads();
  showWorkloadMessage("The demo workload list has been cleared.", "secondary");
});

document.getElementById("logoutBtn").addEventListener("click", () => {
  sessionStorage.removeItem("greenscaleDemoUser");
  window.location.href = "index.html";
});

renderWorkloads();
