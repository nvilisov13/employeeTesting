// Очистка полей ввода при нажатии кнопки
const clsFieldsInput = document.querySelectorAll("input[type='text']");
const clsFieldsTextArea = document.querySelectorAll('textarea');
const btn_clear = document.getElementById('btn-clear')

btn_clear.addEventListener('click', (event) => {
    clsFieldsInput.forEach(input => {
        input.value = '';
    });
    clsFieldsTextArea.forEach(textarea => {
        textarea.value = '';
    });
});
