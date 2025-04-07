import pygame
import sqlite3

# Criar conexão com o banco de dados
conn = sqlite3.connect('game_scores.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time_elapsed REAL
)
''')
conn.commit()
conn.close()


class Score:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/background.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save_score(self, time_elapsed):
        conn = sqlite3.connect('game_scores.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO scores (time_elapsed) VALUES (?)', (time_elapsed,))
        conn.commit()
        conn.close()

    def show_score(self):
        pygame.mixer_music.load('./asset/menu.ogg')
        pygame.mixer_music.play(-1)
        self.window.blit(self.surf, self.rect)

        # Fetch and sort scores
        conn = sqlite3.connect('game_scores.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM scores ORDER BY time_elapsed DESC LIMIT 5')
        scores = cursor.fetchall()
        conn.close()

        while True:
            self.window.blit(self.surf, self.rect)

            # Display scores on screen
            y_pos = 100  # Initial Y position
            for score in scores:
                text = f"Run: {score[0]} - Time: {score[1]:.2f}s"
                font = pygame.font.SysFont('Arial', 25)
                text_surf = font.render(text, True, (255, 255, 255))

                # Calculate X position to center text
                text_rect = text_surf.get_rect(center=(self.window.get_width() / 2, y_pos))
                self.window.blit(text_surf, text_rect)
                y_pos += 30  # Increment for the next line

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

