function showApplianceTypeForm() {
  const selectedApplianceType = document.getElementById("appliance_type").value;
  const airHandlerForm = document.getElementById("air_handler_form");
  const waterHeaterForm = document.getElementById("water_heater_form");

  // Hide both forms
  airHandlerForm.style.display = "none";
  waterHeaterForm.style.display = "none";

  // Show the relevant form based on the user's selection
  if (selectedApplianceType === "Air Handler") {
    airHandlerForm.style.display = "block";

  } else if (selectedApplianceType === "Water Heater") {
    waterHeaterForm.style.display = "block";
  }
}

// Show the heating method and energy source fields if Heater checkbox is selected
var heaterCheckbox = document.getElementById("heater_method");
var airConditionerCheckbox = document.getElementById("air_conditioner_method");
var heatPumpCheckbox = document.getElementById("heatpump_method");

var energySource = document.getElementById("energy_source_entry");
var eer = document.getElementById("eer_entry");
var seer = document.getElementById("seer_entry");
var hspf = document.getElementById("hspf_entry");


heaterCheckbox.addEventListener("change", function () {
  if (this.checked) {
    energySource.style.display = "block";
  } else {
    energySource.style.display = "none";
  }
});

airConditionerCheckbox.addEventListener("change", function () {
  if (this.checked) {
    eer.style.display = "block";
  } else {
    eer.style.display = "none";
  }
});

heatPumpCheckbox.addEventListener("change", function () {
  if (this.checked) {
    seer.style.display = "block";
    hspf.style.display = "block";
  } else {
    seer.style.display = "none";
    hspf.style.display = "none";
  }
});