// Очистка полей ввода при нажатии кнопки
const btn_clear = document.getElementById('btn-clear')
const clsFieldsInput = document.querySelectorAll("input[type='text']");
const clsFieldsTextArea = document.querySelectorAll('textarea');
const selectsOption = document.querySelectorAll('select');

const btn_next = document.getElementById('btn-next')

btn_clear.addEventListener('click', (event) => {
    clsFieldsInput.forEach(input => {
        input.value = '';
    });
    clsFieldsTextArea.forEach(textarea => {
        textarea.value = '';
    });
    selectsOption.forEach(select => {
        select.options.selectedIndex = 0;
    });
})

btn_next.addEventListener('click', (event) => {
    const currentUrl = window.location.href;
    const part_url = currentUrl.slice(currentUrl.lastIndexOf('/') + 1, currentUrl.length);
    let next_url = '';
    switch (part_url){
        case 'add_tests_employees':
            next_url = 'add_questions';
            break;
        case 'add_questions':
            next_url = 'add_answers_questions';
            break;
        case 'add_answers_questions':
            next_url = 'add_tests_employees';
            break;
        case 'add_employees':
            next_url = 'add_nominated_test';
            break;
        case 'add_nominated_test':
            next_url = 'add_employees';
            break;
        default:
            console.log('Следующий адрес не распознан!')
    }
    if(next_url !== '') window.location.replace(next_url);
})
