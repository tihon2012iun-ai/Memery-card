from PyQt5.QtCore import Qt
from random import shuffle, randint
from PyQt5.QtWidgets import (QApplication, 
                            QWidget, QLabel, QRadioButton, QPushButton, 
                            QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup)

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1 
        self.wrong2 = wrong2 
        self.wrong3 = wrong3 

questions = list()
questions.append(Question("Государственный язык Бразилии", "Португальский", "Испанский", 'Итальянский', 'Бразильский'))
questions.append(Question("Сколько стран находится в Европе?", "46", "40", "50", "35"))
questions.append(Question("Какая страна самая большая в мире?", "Росиия", "Китай", "Казахстан", "США"))
questions.append(Question("Сколько стран в мире?", "195", "200", "211", "256"))
questions.append(Question("Сколько людей живёт на планете?", "7,5 милиардов", "7 милиардов", " 5 милиардов", "6 милиардов"))
questions.append(Question("Государственный язык России?", "Русский", "Китайский", "Аглийский", "Беларуский"))
questions.append(Question("Столица Египта?", "Каир", "Пекин", "Париж", "Бразилиа"))

app = QApplication([])
window = QWidget()
window.total = 0
window.score = 0
window.setWindowTitle("Memory Card")
window.resize(500, 350)

lb_question = QLabel("Какой национальности не существует?")
btn_answer = QPushButton('Ответить')
radionbuttonGrup = QGroupBox("Варианты ответов")
radionbutton = QButtonGroup()

ans1 = QRadioButton('Энцы')
ans2 = QRadioButton('Смурфы')
ans3 = QRadioButton('Чулымцы') 
ans4 = QRadioButton('Алеуты')

radionbutton.addButton(ans1)
radionbutton.addButton(ans2)
radionbutton.addButton(ans3)
radionbutton.addButton(ans4)

vlay1 = QVBoxLayout()
vlay2 = QVBoxLayout()
hlay = QHBoxLayout()

vlay1.addWidget(ans1)
vlay1.addWidget(ans2)
vlay2.addWidget(ans3)
vlay2.addWidget(ans4)
hlay.addLayout(vlay1)
hlay.addLayout(vlay2)

radionbuttonGrup.setLayout(hlay)
radionbuttonGrup.show()

ans_group_box = QGroupBox("Результат теста")
result = QLabel("Правильно/Неправильно")
res_answer = QLabel('Правильный ответ')
statistic = QLabel(" ")

ans_lay = QVBoxLayout()

ans_lay.addWidget(result)
ans_lay.addWidget(res_answer, alignment = Qt.AlignCenter)
ans_lay.addWidget(statistic, alignment = Qt.AlignCenter)
ans_group_box.setLayout(ans_lay)
ans_group_box.hide()

hlay1 = QHBoxLayout()
hlay2 = QHBoxLayout()
hlay3 = QHBoxLayout()

hlay1.addWidget(lb_question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
hlay2.addWidget(radionbuttonGrup)
hlay2.addWidget(ans_group_box)
hlay3.addStretch(1)
hlay3.addWidget(btn_answer, stretch = 2)
hlay3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.setSpacing(5)

layout_card.addLayout(hlay1, stretch = 2)
layout_card.addLayout(hlay2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(hlay3, stretch = 1)
layout_card.addStretch(1)

window.setLayout(layout_card)

def show_result():
    ans_group_box.show()
    radionbuttonGrup.hide()
    btn_answer.setText("Следующий вопрос")
    
def show_question():
    ans_group_box.hide()
    radionbuttonGrup.show()
    btn_answer.setText("Ответить")
    radionbutton.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    radionbutton.setExclusive(True)

def start_test():
    if btn_answer.text() == 'Ответить': 
        show_result()
    else:
        show_question()

answers = [ans1, ans2, ans3, ans4]

def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2) 
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    res_answer.setText(q.right_answer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        window.score += 1
        result.setText('Правильно')
    if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        result.setText('Неправильно')
    show_result()
    statistic.setText("Всего вопросов: "+ str(window.total) + "\nПравильных ответов:"+ str(window.score))
    print("Статистика:")
    print("Всего вопросов:", window.total)
    print("Правильных ответов:", window.score)
    print("Рейтинг:", window.score / window.total * 100)

def next_questions():
    cur_question = randint(0,len(questions)- 1)
    window.total += 1
    ask(questions[cur_question])
    print("Статистика:")
    print("Всего вопросов:", window.total)
    print("Правильных ответов:", window.score)

def click_OK():
    if btn_answer.text() == 'Следующий вопрос':
        next_questions()
    else:
        check_answer()

next_questions()
btn_answer.clicked.connect(click_OK)

window.show()
app.exec()
