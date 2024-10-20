import turtle

def draw_koch_segment(length, level):
    """Малює один сегмент кривої Коха з заданою довжиною та рівнем рекурсії."""
    if level == 0:
        turtle.forward(length)
    else:
        length /= 3
        draw_koch_segment(length, level - 1)
        turtle.left(60)
        draw_koch_segment(length, level - 1)
        turtle.right(120)
        draw_koch_segment(length, level - 1)
        turtle.left(60)
        draw_koch_segment(length, level - 1)

def draw_koch_snowflake(length, level):
    """Малює сніжинку Коха з трьох кривих."""
    for _ in range(3):
        draw_koch_segment(length, level)
        turtle.right(120)

def main():
    # Отримуємо рівень рекурсії від користувача
    level = int(input("Введіть рівень рекурсії (рекомендується від 0 до 5): "))
    
    # Налаштування вікна turtle
    turtle.speed(0)  # Максимальна швидкість
    turtle.penup()
    turtle.goto(-200, 100)  # Переміщення початкової позиції
    turtle.pendown()
    
    # Малюємо сніжинку Коха
    draw_koch_snowflake(400, level)
    
    # Закінчення програми
    turtle.done()

if __name__ == "__main__":
    main()
