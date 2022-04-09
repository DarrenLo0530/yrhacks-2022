const meetCodeInput = document.getElementById('meet-code');
const meetCodeForm = document.getElementById('meet-code-form');

meetCodeForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const meetCode = meetCodeInput.value;
  meetCodeInput.value = '';
  eel.monitor_meet(meetCode);
});