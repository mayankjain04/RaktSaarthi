displayHospitals();  
  // Load more hospitals when the button is clicked
  document.getElementById("load-more").addEventListener("click", () => {
    currentPage++;
    displayHospitals();
  });