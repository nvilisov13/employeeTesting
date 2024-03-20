function JSONParsing(url_server, callback) {
    return fetch(url_server)
        .then(response => {
            if (!response.ok) {
                throw new Error('Ответ по сети не в порядке!');
            }
            return response.json();
        }).then(data => {
            callback(data);
        }).catch(error => {
            console.error('Возникла проблема с операцией получения: ', error);
        });
}

const ShowTestEmployees = (data) => {
    document.getElementById('test-employees-name').innerHTML = "<h2>" + data['NameTest'] + "</h2>";
    document.getElementById('test-employees-description').innerHTML =
        "<blockquote>" + data['DescriptionTest'] + "</blockquote>";
}

const ShowQuestions = (data) => {
    document.getElementById('question').innerHTML = '<h4>' + data['5'][0] + '</h4>';
    console.log(data);
}

const ShowQuestionsCount = (data) => {
    document.getElementById('questions-test').innerHTML += '<p>Общее количество вопросов тесте: ' +
        data['QuestionCount'] + '</p>';
    const btn_answered = document.getElementById('btn-answered');
    let current_question = 1
    btn_answered.addEventListener('click', function (){
        if (current_question < data['QuestionCount']){
            ++current_question;
        } else {
            current_question = 1;
        }
        console.log(current_question);
    });
}

function ShowAnswers(data) {
    let scores = {};

    for (let key in data) {
        if (data.hasOwnProperty(key)) {
            let score = data[key][1];
            if (score !== 0) {
                scores[score] = (scores[score] || 0) + 1;
            }
        }
        document.getElementById("answer-question").innerHTML +=
            "<p><input type='radio' name='answers' value=" + data[key][1] + ">&ensp;" + (data[key][0]) + "</p>";
    }

    let uniqueScoresCount = Object.keys(scores).length;
// --- проверяем если может быть несколько правильных ответов меняем radiobutton на checkbox ---
    if (uniqueScoresCount !== Object.values(scores)[0]) {
        let elements = document.querySelectorAll('input[name="answers"]');
        for (let i = 0; i < elements.length; i++) {
            elements[i].setAttribute('type', 'checkbox');
        }
    }
}
