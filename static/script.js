
    var foc= 0
        var count = 0
        document.addEventListener("visibilitychange", () => {
            if (document.visibilityState === "hidden") {
              count+=1;
              if (count === 1){
                window.alert("if you change the tab again...you will get blocked from this site")
              }
              if (count===2){
                console.log("seedc")
              document.getElementById("fraud").submit();
              window.location.href = "fraud"
              }
            }
          });
    window.addEventListener('blur', function () {
        foc+=1;
              if (foc === 1){
                window.alert("if you change the tab again...you will get blocked from this site")
              }
              if (foc===2){
              document.getElementById("fraud").submit();
              window.location.href = "fraud"
              }
        console.log('Window/tab lost focus');
    });
    var timer = document.getElementById('timer')
    var countdownElement = document.getElementById('timer');
        var totalTime = 45 * 60; 

        function updateTimer() {
            var minutes = Math.floor(totalTime / 60);
            var seconds = totalTime % 60;
            countdownElement.textContent = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
        }

        function startTimer() {
            updateTimer();
            var timerInterval = setInterval(function () {
                totalTime--;
                if (totalTime <= 0) {
                    clearInterval(timerInterval);
                    document.getElementById('fraud').submit(); 
                }
                updateTimer();
            }, 1000);
        }

        startTimer();
        