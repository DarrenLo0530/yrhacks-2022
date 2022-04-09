const meetCodeInput = document.getElementById('meet-code');
const meetCodeForm = document.getElementById('meet-code-form');

const homePage = document.getElementById('home');
const monitorPage = document.getElementById('monitor');

const attentionScore = document.getElementById('attention-score');
const leaveMeet = document.getElementById('leave-meet');

let updateInterval;

meetCodeForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const meetCode = meetCodeInput.value;
  meetCodeInput.value = '';
  eel.monitor_meet(meetCode); 

  homePage.classList.add('hidden');
  monitorPage.classList.remove('hidden');

  // Show scores
  updateInterval = setInterval(async () => {
    const score = await eel.get_score()();
    console.log(score);
    attentionScore.innerText = score;
  }, 1000);
});

leaveMeet.addEventListener('click', () => {
  monitorPage.classList.add('hidden');
  homePage.classList.remove('hidden');
  clearInterval(updateInterval);
  eel.close();
});