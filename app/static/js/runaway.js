const runawayBtn = document.querySelector('#runawayBtn');

const moveNoButton = () => {
    const x = Math.random() * (window.innerWidth - runawayBtn.offsetWidth);
    const y = Math.random() * (window.innerHeight - runawayBtn.offsetHeight);

    runawayBtn.style.left = `${x}px`;
    runawayBtn.style.top = `${y}px`;
}



runawayBtn.addEventListener('click', () => {
    alert('Congratulations, you clicked the surprise button!')
});
runawayBtn.addEventListener('mouseenter', moveNoButton);