"""
Simple two-player Ping Pong (turtle)

Usage
- Run: python main.py
- Controls:
    - Right paddle: i (up), k (down)
    - Left paddle: w (up), s (down)

Summary
- Sets up Screen, two Paddles (±350,0), a Ball, and a Scoreboard.
- Main loop: sleep(ball.ball_speed) → screen.update() → ball.move()
- Collisions: bounce_y on top/bottom, bounce_x on paddles.
- Score when ball.xcor() passes ±380 → reset ball and update scoreboard.

Expected APIs
- Paddle((x,y)): go_up(), go_down()
- Ball: ball_speed, move(), bounce_x(), bounce_y(), reset_position()
- Scoreboard: update_scoreboard(), l_point(), r_point()
"""
