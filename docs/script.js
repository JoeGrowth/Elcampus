console.log('Platform Loaded');

let uploadedImageData = "";

// Show image preview when file selected
document.addEventListener("DOMContentLoaded", function () {
  const fileInput = document.getElementById("picFile");
  const previewImage = document.getElementById("previewImage");

  if (fileInput) {
    fileInput.addEventListener("change", function () {
      const file = this.files[0];
      if (file && file.type.startsWith("image/")) {
        const reader = new FileReader();
        reader.onload = function (e) {
          uploadedImageData = e.target.result;
          previewImage.src = uploadedImageData;
          previewImage.style.display = "block";
        };
        reader.readAsDataURL(file);
      }
    });
  }
});

function openModal() {
  document.getElementById("personModal").style.display = "flex";
}

function closeModal() {
  document.getElementById("personModal").style.display = "none";
}

function addPerson() {
  const name = document.getElementById("name").value;
  const role = document.getElementById("role").value;
  const link = document.getElementById("link").value;

  if (!name || !role || !link || !uploadedImageData) {
    alert("Please fill all fields and upload a picture!");
    return;
  }

  const container = document.getElementById("peopleGrid");

  const card = document.createElement("div");
  card.className = "person-card";

  card.innerHTML = `
    <img src="${uploadedImageData}" alt="${name}">
    <div class="person-name">${name}</div>
    <div class="person-role">${role}</div>
    <div class="person-link">
      <a href="${link}" target="_blank">Know the person</a>
    </div>
  `;

  container.appendChild(card);

  closeModal();

  // Reset form
  document.getElementById("name").value = "";
  document.getElementById("role").value = "";
  document.getElementById("link").value = "";
  document.getElementById("picFile").value = "";
  document.getElementById("previewImage").style.display = "none";
  uploadedImageData = "";
}
