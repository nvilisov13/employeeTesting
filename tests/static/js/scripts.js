function BtnAddDB(addDB) {
    const form = document.querySelector('form');
    const formData = new FormData(form);
    fetch('add_test_form', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': '{{ csrf_token }}'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Не удалось добавить данные в базу данных');
        }
        console.log('Данные успешно добавлены в базу данных');
        form.reset();
    })
    .catch(error => {
        console.error('Ошибка добавления данных в базу данных:', error);
    });
}

document.addEventListener('DOMContentLoaded', async (event) => {
    try {
        const response = await fetch('add_employees_test');
        if (!response.ok) {
            throw new Error('Не удалось загрузить форму');
        }
        const content = await response.text();
        document.getElementById('form-input').innerHTML = content;
        // Добавление стилей для применения после загрузки элементов формы
        const addDB = document.getElementById('addDB');
        addDB.classList.toggle('btn');
        addDB.classList.toggle('btn-primary');
        addDB.addEventListener('click', (event) => {
            BtnAddDB(addDB);
            event.preventDefault();
            console.log('Нажата кнопка добавить!');
        })
        const btn_clear = document.getElementById('btn-clear');
        btn_clear.classList.toggle('btn');
        btn_clear.classList.toggle('btn-danger');
        // Очистка полей ввода при нажатии кнопки
        const clsFieldsInput = document.querySelectorAll("input[type='text']");
        const clsFieldsTextArea = document.querySelectorAll('textarea');
        btn_clear.addEventListener('click', (event) => {
            clsFieldsInput.forEach(input => {
                input.value = '';
            })
            clsFieldsTextArea.forEach(textarea => {
                textarea.value = '';
            })
        })
    } catch (error) {
        console.error('Ошибка загрузки формы:', error);
    }
})
