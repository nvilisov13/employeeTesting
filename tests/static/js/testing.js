const JSONParsing = (url_server, callback) => {
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

let id_test = 0, current_question = 1, count_mark = 0, max_mark = 0;
const ShowQuestions = (data) => {
    document.getElementById('question').innerHTML = '<h4>' + data[current_question][0] + '</h4>';
}

function getSelectedValue() {
    let elements = document.querySelectorAll('input[name="answers"]');
    let selectedValue = '';

    for (let i = 0; i < elements.length; i++) {
        if (elements[i].checked) {
            selectedValue = elements[i].value;
            break;
        }
    }
    count_mark += Number(selectedValue);
    return selectedValue;
}

const load_test = (num_id) =>{
    id_test = num_id;
    JSONParsing('/drf_employees_test/' + id_test + '/', ShowTestEmployees).then();
    show_question_answer();
    JSONParsing('/drf_questions/' + id_test + '/question_count/', ShowQuestionsCount).then();
}

const show_question_answer = () => {
    JSONParsing('/drf_questions/' + id_test + '/questions_test/', ShowQuestions).then();
    JSONParsing('/drf_questions/' + current_question + '/question_answers/', ShowAnswers).then();
}

const ShowQuestionsCount = (data) => {
    document.getElementById('questions-test').innerHTML += '<p>Общее количество вопросов тесте: ' +
        data['QuestionCount'] + '</p>';
    const btn_answered = document.getElementById('btn-answered');
    btn_answered.addEventListener('click', function (){
        if (getSelectedValue() !== '') {
            if (current_question < data['QuestionCount']) {
                ++current_question;
            } else {
                current_question = 1;
                alert('Набрано количество баллов: ' + count_mark + ' из максимально возможных - ' + max_mark + ' !');
                window.location.href = '/take_test';
            }
            show_question_answer();
        } else {
            alert('Необходимо ответить на текущий вопрос!');
        }
    });
}

function ShowAnswers(data) {
    const answer_question = document.getElementById("answer-question");
    let scores = {};
    answer_question.innerHTML = '';

    for (let key in data) {
        if (data.hasOwnProperty(key)) {
            let score = data[key][1];
            if (score !== 0) {
                scores[score] = (scores[score] || 0) + 1;
                max_mark += score;
            }
        }
        answer_question.innerHTML += "<p><input type='radio' name='answers' value=" + data[key][1] + ">&ensp;" +
            (data[key][0]) + "</p>";
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
