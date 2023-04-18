function handleHeatingCheckbox() {
  const heatingTempInput = document.getElementById('heating_temp');
  const heatingCheckbox = document.getElementById('heating_checkbox');
  if (heatingCheckbox.checked) {
    heatingTempInput.disabled = true;
    heatingTempInput.removeAttribute('required');
  } else {
    heatingTempInput.disabled = false;
    heatingTempInput.setAttribute('required', true);
  }
}

function handleCoolingCheckbox() {
  const coolingTempInput = document.getElementById('cooling_temp');
  const coolingCheckbox = document.getElementById('cooling_checkbox');
  if (coolingCheckbox.checked) {
    coolingTempInput.disabled = true;
    coolingTempInput.removeAttribute('required');
  } else {
    coolingTempInput.disabled = false;
    coolingTempInput.setAttribute('required', true);
  }
}

const heatingCheckbox = document.getElementById('heating_checkbox');
if (heatingCheckbox) {
  heatingCheckbox.addEventListener('change', handleHeatingCheckbox);
}

const coolingCheckbox = document.getElementById('cooling_checkbox');
if (coolingCheckbox) {
  coolingCheckbox.addEventListener('change', handleCoolingCheckbox);
}
